#!/usr/bin/env python

# Works on Python3 >= 3.6
# check if required python modules are installed
import sys

mod_list = ["re", "alive_process", "requests"]

for i in mod_list:
    try:
        __import__(i)
        print("\033[0mINFO: \'" + i + "\' is found.\033[0m")
    except ModuleNotFoundError as err:
        # Error handling
        # print(err)
        print("\033[1mERROR: \'" + i + "\' is not found\033[0m")
        sys.exit(1)


# Python3 >= 3.4 compatibility
# import importlib
# importlib.util.find_spec(name, package=None)
# submod_list = []
# for n in mod_list:
#    pkg_spec = importlib.util.find_spec()
#    found = pkg_spec is not None


# for n in submod_list:
#    pkg_spec = importlib.util.find_spec(pakcage="alive.bar")
#    found = pkg_spec is not None
