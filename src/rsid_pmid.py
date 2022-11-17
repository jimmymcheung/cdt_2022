#!/usr/bin/env python


import pandas as pd
import xml.etree.ElementTree as elt
from collections import defaultdict

content = elt.parse("C:/Users/swans/Downloads/clinvar_cut.xml")
tree = content.getroot()
no_rs = ""
rsandpmids = {}
rsids = []
pmids = []
myDict = dict()


def get_id_info():
    dictionary = {}
    for i in rsid:
        no_rs = i.replace("rs", "")
        for s in tree.iter("ClinVarSet"):
            for movie in s.iter("XRef"):
                for i in movie.findall('[@Type = "rs"]'):
                    pmids = []
                    for a in i.findall(f'[@ID = "{no_rs}"]'):
                        if a.attrib["ID"] == no_rs:
                            no_rs_no_duplicate = no_rs
                        for t in s.iter("ID"):
                            for l in t.findall("[@Source='PubMed']"):
                                if l.text not in pmids:
                                    pmids.append(l.text)
                                    dictionary.update({no_rs_no_duplicate: pmids})
    print(dictionary)
    # return str(res)


rsid = ['rs267606900', 'rs267607078', 'rs12075']

# Syntax xml clinvar:
# <XRef Type="rs" ID="267606900" DB="dbSNP"/>
# <ID Source="PubMed">20970105</ID>


if __name__ == '__main__':
    print(get_id_info())
