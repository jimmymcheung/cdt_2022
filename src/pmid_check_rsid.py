# Library
import requests

# file input
# search qeury per rsid entry from file
for n in ...:
    rsidv=$n
    # URL not larger than 2048 char
    r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" +str(rsidv)+ "retmode=xml")
    print(r.text)
