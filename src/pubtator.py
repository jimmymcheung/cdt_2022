
import urllib.request



def get_terms(all_pmids):
    input_type = "pmids"
    export_type = "pubtator"
    bioconcepts = "disease,gene,mutation"

    for pmid in all_pmids:
        url = f"https://www.ncbi.nlm.nih.gov/research/" \
              f"pubtator-api/publications/export/{export_type}?" \
              f"{input_type}={pmid}&concepts={bioconcepts}"

        text = urllib.request.urlopen(url).read().decode("utf-8")

        parse_pubtator(text)


def parse_pubtator(text):
    terms = []
    bioconcepts = []
    terms_bioconcepts = {}
    lines = text.split("\n")

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
            terms.append(term_line[3].lower())
            bioconcepts.append(term_line[4].lower())
            if term_line[3] not in terms_bioconcepts.keys():
                terms_bioconcepts[
                    term_line[3].lower()] = term_line[4].lower()

    terms_occurances = count_terms(terms)
    return terms, bioconcepts, terms_occurances


def count_terms(terms):
    terms_occurances = {}
    for term in terms:
        if term not in terms_occurances.keys():
            occurances = terms.count(term)
            terms_occurances[term] = occurances
    print(terms_occurances)
    return terms_occurances


if __name__ == '__main__':
    all_pmids = [20964851, 19176549, 28244479, 30713326, 31761807, 26891021]
    get_terms(all_pmids)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
