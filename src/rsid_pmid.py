import pandas as pd
import xml.etree.ElementTree as elt

content = elt.parse("C:/Users/jaral/OneDrive/Bureaublad/clinvar_cut.xml").getroot()


def get_id_info(inputID):
    for child in content:
        if child.find('id').text == inputID:
            print(child.find('ID Source = "PubMed"').text)


rsid = ['rs267606900', 'rs267607078', 'rs12075']


# Syntax xml clinvar:
# <XRef Type="rs" ID="267606900" DB="dbSNP"/>
# <ID Source="PubMed">20970105</ID>

def read_rsid(rsid):
    for i in rsid:
        no_rs = i.replace("rs", "")
        print(no_rs)


if __name__ == '__main__':
    read_rsid(rsid)
    get_id_info('267606900')

