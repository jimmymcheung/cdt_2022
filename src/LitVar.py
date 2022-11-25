import urllib.request


def get_terms(all_pmids):
    input_type = "pmids"
    export_type = "pubtator"
    bioconcepts = "disease,gene,mutation"
    for pmid in all_pmids:
        url = f"https://www.ncbi.nlm.nih.gov/research/litvar2-api/variant/get/litvar@{pmid}%23%23/publications"

        text = urllib.request.urlopen(url).read().decode("utf-8")

        print(text)


if __name__ == '__main__':
    all_pmids = ["rs6657048", "rs28357376", "rs3094280", "rs2853508" , "rs2853507", "rs35070048"]
    get_terms(all_pmids)
