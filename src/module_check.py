#!/usr/bin/env python

# Check existence of required python modules
# Copyright © 2022 CDT project
# Author: Jiaming Zhang
# Works on Python3 >= 3.6
import sys
import xml.etree.ElementTree

mod_list = ["requests", "pandas", "nltk"]
subMod_list = """<?xml version="1.0"?>
<modlist>
    <module>
        <pipName>alive-progress</pipName>
        <parent>alive_progress</parent>
        <child>alive_bar</child>
    </module>
    <module>
        <pipName>lxml</pipName>
        <parent>lxml</parent>
        <child>etree</child>
    </module>
    <module>
        <pipName>nltk</pipName>
        <parent>nltk.stem</parent>
        <child>PorterStemmer</child>
    </module>
    <module>
        <pipName>nltk</pipName>
        <parent>nltk.tokenize</parent>
        <child>word_tokenize</child>
    </module>
    <module>
        <pipName>nltk</pipName>
        <parent>nltk.stem.snowball</parent>
        <child>SnowballStemmer</child>
    </module>
</modlist>"""
err_count = 0


for i in mod_list:
    try:
        exec("import " + i)
        print("\033[0mINFO: \'" + i + "\' is found.\033[0m")
    # except ModuleNotFoundError as err:
    except ImportError:
        # Error handling
        print("\033[1mERROR: \'" + i + "\' is not found.\033[0m")
        err_count = err_count + 1


subMod_xml = xml.etree.ElementTree.fromstring(subMod_list)
for e in subMod_xml:
    parent = e.find('parent').text
    child_list = e.findall('child')
    for c in child_list:
        child = c.text
        try:
            exec("from " + parent + " import " + child)
            # __import__(parent, fromlist=child)
            print("\033[0mINFO: \'" + parent + '.' + child + "\' is found.\033[0m")
        except ImportError:
            # Error handling
            print("\033[1mERROR: \'" + parent + '.' + child + "\' is not found\033[0m")
            err_count = err_count + 1


if err_count > 0:
    sys.exit(1)
