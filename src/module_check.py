#!/usr/bin/env python

# Works on Python3 >= 3.6
# check if required python modules are installed
import json
import sys

mod_list = ["requests", "pandas"]
submod_list = ["""{
    "pipName": "alive-progress",
    "parent": "alive_progress",
    "child": "alive_bar"
}"""]


# class NestMod:
#     def __int__(self, parent, child):
#         self.parent = parent
#         self.child = child


for i in mod_list:
    try:
        __import__(i)
        print("\033[0mINFO: \'" + i + "\' is found.\033[0m")
    except ModuleNotFoundError as err:
        # Error handling
        # print(err)
        print("\033[1mERROR: \'" + i + "\' is not found\033[0m")
        sys.exit(1)


# for x in submod_list:
#     submod = json.load(json.dump(x))
#     parent = submod["parent"]
#     child = submod["child"]
#     try:
#         __import__(child, fromlist=parent)
#         print("\033[0mINFO: \'" + parent + "." + child + "\' is found.\033[0m")
#     except ModuleNotFoundError as err:
#         # Error handling
#         # print(err)
#         print("\033[1mERROR: \'" + parent + "." + child + "\' is not found\033[0m")
#         sys.exit(1)


# Python3 >= 3.4 compatibility
# import importlib
# importlib.util.find_spec(name, package=None)
# submod_list = []
# for n in mod_list:
#    pkg_spec = importlib.util.find_spec()
#    found = pkg_spec is not None


# for n in submod_list:
#    pkg_spec = importlib.util.find_spec(package="alive.bar")
#    found = pkg_spec is not None
