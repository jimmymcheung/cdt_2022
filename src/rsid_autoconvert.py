#! /bin/python3
# Private ID auto-convert to rsid
# 2022 © Check De Test Project
# This script convert the private ID SNP records with RSID queried from ClinVar.
# The input should be tab-separated value, in the following format:
# rsid	chromosome	position	genotype

# inlezen bestanden
# variable voor rsid
# voor elke iid
# variable voor chromosome:position
# variable voor genotype

# send HTTP GET request
import requests
r = requests.get("")
# get HTTP response
print('Status Code:')
print(r.status_code)

# process HTTP response

# HTTP code 200

# other HTTP code (error handle)
