#!/usr/bin/env python
import os

import pandas as pd
import xml.etree.ElementTree as elt
from collections import defaultdict
from alive_progress import alive_bar
from tqdm import tqdm
from time import sleep

content = elt.parse("../res/clinvar/clinvar_cut.xml")
tree = content.getroot()
no_rs = ""
rsandpmids = {}
rsids = []
pmids = []
myDict = dict()




def read_gt(filename):
    """Reads if genotype transcript file, all rules with # will not be read

    :param: filename - str
    :return: rsidlist, iidlist
    """

    rsidlist = []
    iidlist = []
    try:
        # open file
        with open(filename) as file:
            # read file per line
            for line in file:
                # checks if line does not start with #
                if line.startswith("rs"):
                    # add only the first word (rsid) to the list
                    rsidlist.append(line.split(None, 1)[0])
                elif line.startswith("i"):
                    # add only the first word (iid) to the list
                    iidlist.append(line.split(None, 1)[0])

        # return rs id and i id list
        return rsidlist, iidlist
    except FileNotFoundError:
        print("File could not be found")
    except IOError:
        print("File is not readable")
    except NameError:
        print("Name does not exist")


def get_id_info(rsid):
    dictionary = {}

    with alive_bar(len(rsid), force_tty=True) as bar:
        for i in rsid:
            no_rs = i.replace("rs", "")
            bar()
            data_to_database(dictionary)
            for s in tree.iter("ClinVarSet"):
                for movie in s.iter("XRef"):
                    for i in movie.findall('[@Type = "rs"]'):
                        pmids = []
                        for a in i.findall(f'[@ID = "{no_rs}"]'):
                            if a.attrib["ID"] == no_rs:
                                dictionary.update({no_rs: ""})
                                no_rs_no_duplicate = no_rs
                            for t in s.iter("ID"):
                                for l in t.findall("[@Source='PubMed']"):
                                    if l.text not in pmids:
                                        pmids.append(l.text)
                                        dictionary.update({no_rs_no_duplicate: pmids})

        return dictionary
def data_to_database(dictionary):

    for key, value in dictionary.items():
        #print(key)
        for i in value:
                # insert in database
            #print(i)

# Syntax xml clinvar:
# <XRef Type="rs" ID="267606900" DB="dbSNP"/>
# <ID Source="PubMed">20970105</ID>


if __name__ == '__main__':
    rsidlist, iidlist = read_gt(
         "../res/GT_files/Original_files/uk4CA868_20180206095657(1).gt")
    print(get_id_info(rsidlist))