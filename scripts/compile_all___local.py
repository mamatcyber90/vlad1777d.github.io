#! /usr/bin/python3


if __name__ == "__main__":
	from for_compiling.sources_directories import find_directories
	from for_compiling.compile_functions import compile_project

	for cur_project in find_directories ():
		print ("")
		print ("Compiling:", cur_project)
		compile_project ('local', cur_project)
