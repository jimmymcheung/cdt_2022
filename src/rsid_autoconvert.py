#!/usr/bin/env python
# Private ID auto-convert to rsid
# 2022 © Check De Test Project
# This script convert the private ID SNP records with RSID queried from ClinVar.
# The input should be tab-separated value, in the following format:
# rsid	chromosome	position	genotype

# Library
# Custom function
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

# Read file with IID

# Variable for RSID
# voor elke iid
# variable voor chromosome:position
# variable voor genotype

# send HTTP GET request
import requests
r = requests.get("")  # URL moet nog ingezet worden
# get HTTP response
print('Status Code:')
print(r.status_code)

# process HTTP response

# HTTP code 200

# other HTTP code (error handle)
