#! /usr/bin/python3


import os, os.path
import sys


THIS_FILES_DIR = os.path.dirname (__file__)
DIRS_TO_COMPILE = ('./sources_vlad1777d', './sources_web_development', './sources_your_averters')


for comp_dir in DIRS_TO_COMPILE:
	comp_dir = os.path.abspath (os.path.join (THIS_FILES_DIR, comp_dir))
	os.chdir (comp_dir)
	os.system ('pelican -s publishconf.py')
