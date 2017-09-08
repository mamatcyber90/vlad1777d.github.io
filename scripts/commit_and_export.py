#! /usr/bin/python3

import os, os.path


THIS_FILES_DIR = os.path.dirname (__file__)
BASE_DIR = os.path.join (THIS_FILES_DIR, '../')
os.chdir (BASE_DIR)

os.system('hg addremove')
os.system('hg commit')
os.system('hg push git+ssh://git@github.com:vlad1777d/vlad1777d.github.io.git')
# if there's error: ""
# then you can make "hg gc" and then repeat pushing attempt
print("Script finished.")
