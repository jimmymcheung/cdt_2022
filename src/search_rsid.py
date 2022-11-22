#!/usr/bin/env python
# RSID Live query for PMID

# Library
import requests
from alive_progress import alive_bar
# Variables
fileinput = input('Please specify your GT file: \n')
no_rs = ""
rsandpmids = {}
rsids = []
pmids = []
# Functions


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
            r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" +str(rsidv)+ "retmode=xml")
            bar()
            data_to_database(dictionary)
            # funcie aan roepen, neem dictionary mee naar database fucntion
            dictionary = {}
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


if __name__ == '__main__':
    rsidlist, iidlist = read_gt(fileinput)
    get_id_info(rsidlist)
