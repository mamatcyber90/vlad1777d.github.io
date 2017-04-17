#! /usr/bin/python3

import os


os.system('hg addremove')
os.system('hg commit')
os.system('hg push git+ssh://git@github.com:vlad1777d/vlad1777d.github.io.git')
print("Script finished.")
