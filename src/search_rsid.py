#!/usr/bin/env python
# RSID Live query for PMID
# Copyright © 2022 CDT project
# Author: Jiaming Zhang
# See also: 'rsid_pmid.py' for querying in local database.

# Library
import json
import time
from typing import Any
import requests
from alive_progress import alive_bar
import pandas as pd

# Variables
fileInput = input('Please specify your GT file: \n')
rsandpmids = {}
rsids = []
pmids = []
# Functions


def read_gt(filename):
    """Reads if genotype transcript file, all rules with # will be ignored

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
        print("\033[1mERROR: File could not be found\033[0m")
    except IOError:
        print("\033[1mERROR: File is not readable\033[0m")
    except NameError:
        print("\033[1mERROR: Name does not exist\033[0m")


def get_id_info(rsid):
    dictionary: dict[str, Any] = {}
    rs_list = []
    rs_end = False
    http_param = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n' \
                 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15\n' \
                 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n'
    for x in rsid:
                no_rs = x.replace("rs", "")
                rs_list.append(no_rs)

    with alive_bar(len(rsid), force_tty=True) as bar:
        bar()
        # while rs_list:
        #     bar()
        #     if len(rs_list) >= 162:
        #         rsdf = pd.DataFrame(rs_list[0:161])
        #         r_rs = rsdf.to_csv(header=False, index=False)
        #         r_rs = r_rs.replace("\n", ',')
        #         r_rs = r_rs[:-1]
        #     else:
        #         rsdf = pd.DataFrame(rs_list)
        #         r_rs = rsdf.to_csv(header=False, index=False)
        #         r_rs = r_rs.replace("\n", ',')
        #         r_rs = r_rs[:-1]
        #         rs_end = True
        for r_rs in rs_list:
            # Max 1954 / 12 = 162 RSID per request with JSON
            r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" + r_rs + "&rettype=json&retmode=text", params=http_param)
            # Max 164 RSID per request with XML
            # r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" + str(r_rs) + "&retmode=xml")
            # Filter and add output to dict on HTTP 200
            if r.status_code == 200:
                # Extract HTTP response
                out = json.loads(r.text)
                # Filter and extract 'PMID' and 'Clinical significance'
                # 'refsnp_id' is rsid; 'citations' is list of PMID;
                # 'observation' is dict of mutation info (ID pos GT) can be multiple,
                # 'alleles' has collection of 'allele' each is a 'observation';
                # 'clinical' for clinical significance
                for rsEntry in out:
                    rs_out: dict[str, Any] = {'refsnp_id': rsEntry['refsnp_id'], 'citations': rsEntry['citations']}
                    dictionary.update(rs_out)
                # if not rs_end:
                #     # Clear first 162 elements in rs_list
                #     del rs_list[0:161]
                # else:
                #     rs_list.clear()
            else:
                print("\033[1mERROR: ClinVar Server return HTTP " + str(r.status_code) + ". Check Your connection or contact Server admin.\033[0m")
                print("\033[0mRetrying...")
            # Internal between request
            time.sleep(1)

        return dictionary


def get_ids_info(rsid):
    dictionary: dict[str, Any] = {}
    rs_list = []
    rs_end = False
    http_param = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n' \
                 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15\n' \
                 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n'
    for x in rsid:
                no_rs = x.replace("rs", "")
                rs_list.append(no_rs)

    while rs_list:
        if len(rs_list) >= 162:
            rsdf = pd.DataFrame(rs_list[0:161])
            r_rs = rsdf.to_csv(header=False, index=False)
            r_rs = r_rs.replace("\n", ',')
            r_rs = r_rs[:-1]
        else:
            rsdf = pd.DataFrame(rs_list)
            r_rs = rsdf.to_csv(header=False, index=False)
            r_rs = r_rs.replace("\n", ',')
            r_rs = r_rs[:-1]
            rs_end = True
        # Max 1954 / 12 = 162 RSID per request with JSON
        r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" + r_rs + "&rettype=json&retmode=text", params=http_param)
        # Max 164 RSID per request with XML
        # r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id=" + str(r_rs) + "&retmode=xml")
        # Filter and add output to dict on HTTP 200
        if r.status_code == 200:
            # Extract HTTP response
            out = json.loads(r.text)
            # Filter and extract 'PMID' and 'Clinical significance'
            # 'refsnp_id' is rsid; 'citations' is list of PMID;
            # 'observation' is dict of mutation info (ID pos GT) can be multiple,
            # 'alleles' has collection of 'allele' each is a 'observation';
            # 'clinical' for clinical significance
            for rsEntry in out:
                rs_out: dict[str, Any] = {'refsnp_id': rsEntry['refsnp_id'], 'citations': rsEntry['citations']}
                dictionary.update(rs_out)
            if not rs_end:
                # Clear first 162 elements in rs_list
                del rs_list[0:161]
            else:
                rs_list.clear()
        else:
            print("\033[1mERROR: ClinVar Server return HTTP " + str(r.status_code) + ". Check Your connection or contact Server admin.\033[0m")
            print("\033[0mRetrying...")
        # Internal between request
        time.sleep(1)
    else:
        print("\033[0mINFO: Query completed!")

    return dictionary


if __name__ == '__main__':
    rsidlist, iidlist = read_gt(fileInput)
    dict = get_id_info(rsidlist)
    print(dict)
    # Above returns empty value '{}'
