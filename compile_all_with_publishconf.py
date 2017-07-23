#! /usr/bin/python3


import os, os.path
import sys


THIS_FILES_DIR = os.path.dirname (__file__)
DIRS_TO_COMPILE = ('./pelican_sources_vlad1777d', './pelican_sources_page_web_development')


for comp_dir in DIRS_TO_COMPILE:
	comp_dir = os.path.abspath (os.path.join (THIS_FILES_DIR, comp_dir))
	os.chdir (comp_dir)
	os.system ('pelican -s publishconf.py')
