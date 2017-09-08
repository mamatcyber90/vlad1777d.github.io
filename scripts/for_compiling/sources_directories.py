#! /usr/bin/python3
""" Contains dict of sources directories.
It's calculated automatically parsing directories, which name starts with "sources".
Exapmle:
	Directory: sources___your_averters will be added as:
		{"your_averters": "/absolute/path/to/.../sources___your_averters"}
"""


def find_directories ():
	""" Automatically finds directories.
	"""
	import os, os.path

	current_files_dir = os.path.dirname (__file__)
	BASE_DIR = os.path.join (current_files_dir, '../../')

	sources_directories = {}

	for cur_name in os.listdir (BASE_DIR):
		if cur_name.startswith ("sources___"):
			name = cur_name.replace ("sources___", "")
			path = os.path.abspath (os.path.join (BASE_DIR, cur_name))
			sources_directories [name] = path
	return sources_directories



if __name__ == "__main__":  # for testing
	print (find_directories ())
