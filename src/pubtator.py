
import urllib.request
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer


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

words = ["cancers", "cancerous"]
sn_stemmer = SnowballStemmer("english")

#clearfileout
with open("output_stem.txt",'w')as file:
    pass

for w in words:
    stem = print(w, " : ", sn_stemmer.stem(w))
    print(sn_stemmer.stem(w), file = open("output_stem.txt", "a"))
    f = open("output_stem.txt", "r")
    f.close()

def count_terms(terms):
    terms_occurances = {}
    for term in terms:
        if term not in terms_occurances.keys():
            occurances = terms.count(term)
            terms_occurances[term] = occurances
    print(terms_occurances)
    return terms_occurances

#count stem words
file_name = "output_stem.txt"
file_handle = open("output_stem.txt", "r")
countWord = 0
for content in file_handle:
    chk = 0
    content_length = len(content)
    for i in range (content_length):
        if content [i] ==' ':
            if chk!=0:
                countWord = countWord+1
            chk = 0
        else:
            chk = chk+1
    if chk!=0:
        countWord = countWord+1
print("\nstem word(s): " + sn_stemmer.stem(w) + ", occurance: ")
print(countWord)

if __name__ == '__main__':
    all_pmids = [20964851, 19176549, 28244479, 30713326, 31761807, 26891021]
    get_terms(all_pmids)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
