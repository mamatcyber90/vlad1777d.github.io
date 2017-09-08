#!/usr/bin/python3




def compile_project (type = 'local', project_name = None):
	""" Compiles project with given type.
	type: 'local' / 'publish'
	Uses:
		make_copy_of_coffeescript_files ()
	"""
	if not project_name:
		raise FileNotFoundError ("Please, specify project dir first!")

	import os, os.path
	import sys
	import imp
	from .sources_directories import find_directories

	project_dir = find_directories () [project_name]
	sys.path.append (project_dir)
	os.chdir (project_dir)

	if not ("pelicanconf" in sys.modules):
		import pelicanconf
		ABS_OUTPUT_PATH = pelicanconf.ABS_OUTPUT_PATH
	else:
		import pelicanconf
		imp.reload (pelicanconf)
		ABS_OUTPUT_PATH = pelicanconf.ABS_OUTPUT_PATH
	# ^ needed when calling this function several times for different projects
	# we don't do the same for "publishconf" because it's never imported
	# pelican will import "publishconf" if needed, it will import "pelicanconf"

	if type == 'local':
		command = 'pelican'
	elif type == 'publish':
		command = 'pelican -s publishconf.py'
	os.system (command)
	make_copy_of_coffeescript_files (ABS_OUTPUT_PATH)  # needed because
	# Firefox can't receive .coffee scripts with XMLHttpRequest
	# from parent directory, as he can with .js scripts

	sys.path.remove (project_dir)  # to avoid errors importing pelicanconf
	# when using this function to compile several projects one after other



def make_copy_of_coffeescript_files (output_folder):
	""" Makes copy of all found coffeescript files
		from output_folder/theme/{'scripts' or 'js' or 'coffee'}/script.coffee to output_folder/en/theme/{corresponding_dir}/script.coffee
	It's needed because firefox bans XMLHttpRequest to parent folder, and .coffee files
		are loaded right with it.
	Launched from:
		compile_project ()
	"""
	import os, os.path
	import shutil

	theme_met = False
	en_met = False

	probably___theme___dir = os.path.join (output_folder, 'theme')
	probably___en___dir = os.path.join (output_folder, 'en')
	if os.path.exists (probably___theme___dir):
		theme_met = True
	if os.path.exists (probably___en___dir):
		en_met = True

	if theme_met and en_met:
		files_to_copy___scripts = []
		files_to_copy___js = []
		files_to_copy___coffee = []

		probably___theme___scripts___dir = os.path.join (output_folder, 'theme/scripts')
		probably___theme___js___dir = os.path.join (output_folder, 'theme/js')
		probably___theme___coffee___dir = os.path.join (output_folder, 'theme/coffee')

		if os.path.exists (probably___theme___scripts___dir):
			for cur_filename in os.listdir (probably___theme___scripts___dir):
				if cur_filename.endswith ('.coffee'):
					cur_filepath = os.path.join (probably___theme___scripts___dir, cur_filename)
					files_to_copy___scripts.append (cur_filepath)

		if os.path.exists (probably___theme___js___dir):
			for cur_filename in os.listdir (probably___theme___js___dir):
				if cur_filename.endswith ('.coffee'):
					cur_filepath = os.path.join (probably___theme___js___dir, cur_filename)
					files_to_copy___js.append (cur_filepath)

		if os.path.exists (probably___theme___coffee___dir):
			for cur_filename in os.listdir (probably___theme___coffee___dir):
				if cur_filename.endswith ('.coffee'):
					cur_filepath = os.path.join (probably___theme___coffee___dir, cur_filename)
					files_to_copy___coffee.append (cur_filepath)

		en_theme_scripts___dir = os.path.join (output_folder, 'en/theme/scripts')
		en_theme_js___dir = os.path.join (output_folder, 'en/theme/js')
		en_theme_coffee___dir = os.path.join (output_folder, 'en/theme/coffee')

		if os.path.exists (probably___theme___scripts___dir):
			if not os.path.exists (en_theme_scripts___dir):
				os.makedirs (en_theme_scripts___dir)
			for cur_file in files_to_copy___scripts:
				shutil.copy2 (cur_file, en_theme_scripts___dir)
			print ("Copied {amount} .coffee scripts to en/theme/scripts directory.".format (
				amount = len(files_to_copy___scripts))
			)

		if os.path.exists (probably___theme___js___dir):
			if not os.path.exists (en_theme_js___dir):
				os.makedirs (en_theme_js___dir)
			for cur_file in files_to_copy___js:
				shutil.copy2 (cur_file, en_theme_js___dir)
			print ("Copied {amount} .coffee scripts to en/theme/js directory.".format (
				amount = len(files_to_copy___js))
			)

		if os.path.exists (probably___theme___coffee___dir):
			if not os.path.exists (en_theme_coffee___dir):
				os.makedirs (en_theme_coffee___dir)
			for cur_file in files_to_copy___coffee:
				shutil.copy2 (cur_file, en_theme_coffee___dir)
			print ("Copied {amount} .coffee scripts to en/theme/coffee directory.".format (
				amount = len(files_to_copy___coffee))
			)
	else:
		if not theme_met:
			print ("Warning! 'theme' folder not found.")
		if not en_met:
			print ("Warning! 'en' folder not found.")
