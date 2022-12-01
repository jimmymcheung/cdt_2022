#!/usr/bin/env python

# RSID local query for PMID
# Copyright © 2022 CDT project
# Author: Jara Laureijssen, Sven Lukassen
# See also: 'search_rsid.py' for querying on ClinVar Server.

from lxml import etree as et


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

def fn2(rsid, fileInput):
    dictionary = {}
    pmids = []
    no_rs_no_duplicate = ''
    context = et.iterparse(fileInput, tag=['XRef', 'ID'])
    for event, element in context:
        for z in element.findall('[@Type = "rs"]'):
            for i in rsid:
                no_rs = i.replace("rs", "")
                pmids = []
                if z.attrib["ID"] == no_rs:
                    dictionary.update({no_rs: ""})
                    no_rs_no_duplicate = no_rs
        for l in element.findall("[@Source='PubMed']"):
            if l.text not in pmids:
                if no_rs_no_duplicate != "":
                    pmids.append(l.text)
                    dictionary.update({no_rs_no_duplicate: pmids})

    return dictionary


if __name__ == '__main__':
    fileInput = input("PathName for GT File: \n")
    clinvarfile = ("../../clinvar/ClinVarFullRelease_2022-10.xml")
    rsidlist, iidlist = read_gt(fileInput)
    dictionary = fn2(rsidlist, clinvarfile)

