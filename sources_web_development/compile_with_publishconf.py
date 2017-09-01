#! /usr/bin/python3


import os, os.path
import sys


THIS_FILES_DIR = os.path.dirname (__file__)
os.chdir (THIS_FILES_DIR)


os.system ('pelican -s publishconf.py')
