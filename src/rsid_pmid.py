#!/usr/bin/env python
import os

import pandas as pd
import xml.etree.ElementTree as elt
from collections import defaultdict
from alive_progress import alive_bar
from tqdm import tqdm
from time import sleep
from lxml import etree as et

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


def data_to_database(dictionary):
    for key, value in dictionary.items():
        # print(key)
        for i in value:
            print("")


# Syntax xml clinvar:
# <XRef Type="rs" ID="267606900" DB="dbSNP"/>
# <ID Source="PubMed">20970105</ID>

def fn2(rsid):
    pmids = []
    no_rs_no_duplicate = ''
    dictionary2 = {}
    context = et.iterparse("../res/clinvar/clinvar_cut.xml", tag=['XRef', 'ID'])
    for event, element in context:
        print(element.attrib)
        for i in rsid:
            no_rs = i.replace("rs", "")
            for z in element.findall('[@Type = "rs"]'):
                no_rs = i.replace("rs", "")
                pmids = []
                for a in z.findall(f'[@ID = "{no_rs}"]'):
                    if a.attrib["ID"] == no_rs:
                        dictionary2.update({no_rs: ""})
                        no_rs_no_duplicate = no_rs
            for l in element.findall("[@Source='PubMed']"):
                if l.text not in pmids:
                    if no_rs_no_duplicate != "":
                        pmids.append(l.text)
                        dictionary2.update({no_rs_no_duplicate: pmids})
    return dictionary2


if __name__ == '__main__':
    rsidlist, iidlist = read_gt(
        "../res/GT_files/Original_files/uk4CA868_20180206095657(1).gt")
    print(fn2(rsidlist))
