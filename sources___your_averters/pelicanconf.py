#!/usr/bin/env python3
import sys # для импорта файла с переводом
import os.path  # для совмещения строк с путями




PATH = 'sources'
STATIC_PATHS = ['images', 'music']  # я так понял, они будут внутри папки PATH
PAGE_PATHS = []
ARTICLE_PATHS = []
THEME = os.path.join(PATH, 'theme_rainbow')
DIRECT_TEMPLATES = ['index']  # здесь написать имена тех шаблонов, которые будут отрендерены
OUTPUT_PATH = '../your_averters'
DELETE_OUTPUT_DIRECTORY = True




THIS_FILES_DIR = os.path.dirname (__file__)
if not THIS_FILES_DIR: THIS_FILES_DIR = os.getcwd ()
# ^ hach to the bug, when __file__ is not abspath, but 'pelicanconf.py'
# pelican is always launched from directory with this file
ABS_OUTPUT_PATH = os.path.abspath ( os.path.join (THIS_FILES_DIR, OUTPUT_PATH))




AUTHOR = 'Vladislav (naumovvladislav@mail.ru)'
#SITENAME = 'сайт проекта Твои обереги'
SITEURL = 'file://' + ABS_OUTPUT_PATH   # вместо RELATIVE_URLS = True
VLAD1777D_SITE_PATH = 'file://' + os.path.abspath ( os.path.join (ABS_OUTPUT_PATH, '../'))




TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = 'ru'
#DL = DEFAULT_LANG  # shortcut for translating in templates
PLUGIN_PATHS = [os.path.join(PATH, 'plugins')]
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
    'en': {}
}




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
