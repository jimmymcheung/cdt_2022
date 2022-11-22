import urllib.request
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

sn_stemmer = SnowballStemmer("english")


def get_terms(pmids):
    """
    This funtion sents all the pmids to the pubtator API and gives the result to function 'analyze_pubtator'
    :param pmids: All the pmids acquired from the input files
    """
    # Declaring variables to sent to pubtator api
    input = "pmids"
    export = "pubtator"
    bioconcepts = "disease,gene,mutation"

    # Sending request to pubtator
    for pmid in pmids:
        url = f"https://www.ncbi.nlm.nih.gov/research/" \
              f"pubtator-api/publications/export/{export}?" \
              f"{input}={pmid}&concepts={bioconcepts}"

        # Get pubtator results
        pubtator_result = urllib.request.urlopen(url).read().decode("utf-8")
        analyze_pubtator(pubtator_result)


def analyze_pubtator(pubtator_result):
    """
    This function analyses the results from pubtator.
    It will filter out the terms found in pubtator, the abstract and title
    The terms will be sent to function terms_occurances to count the terms
    :param pubtator_result: Result from pubtator api
    :return terms[] = all the terms found in pubtator result
            bioconcepts[] = all the bioconcepts found in pubtator api
            terms_occurances{} = all the terms and their count
    """
    terms = []
    bioconcepts = []
    terms_bioconcepts = {}
    lines = pubtator_result.split("\n")

    try:
        title = lines[0].split('|')[2].rstrip()
    except IndexError:
        title = None
    try:
        abstract = lines[1].split('|')[2]
    except IndexError:
        abstract = None
    for line in lines:
        if len(line.split("\t")) == 6:
            term_line = line.split("\t")
            x = sn_stemmer.stem(term_line[3])
            terms.append(x.lower())
            bioconcepts.append(term_line[4].lower())
            if term_line[3] not in terms_bioconcepts.keys():
                terms_bioconcepts[
                    term_line[3].lower()] = term_line[4].lower()

    terms_occurances = count_terms(terms)
    return terms, bioconcepts, terms_occurances


def count_terms(terms):
    """
    This function counts the terms and their occurances
    :param terms: all the terms from pubtator
    :return: terms_occurances{} = terms and their occurances
    """
    terms_occurances = {}
    for term in terms:
        if term not in terms_occurances.keys():
            occurances = terms.count(term)
            terms_occurances[term] = occurances
    print(terms_occurances)
    return terms_occurances


if __name__ == '__main__':
    all_pmids = [20964851, 19176549, 28244479, 30713326, 31761807, 26891021]
    get_terms(pmids=all_pmids)
