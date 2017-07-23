#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from __future__ import unicode_literals
import os.path
join = os.path.join
import sys




PATH = 'sources'
STATIC_PATHS = []  # будут внутри папки PATH
ARTICLE_PATHS = []
THEME = join(PATH, 'theme_general')
DIRECT_TEMPLATES = ['page_web_development']
# ^ здесь написать имена тех шаблонов, которые будут включены в постоение
OUTPUT_PATH = '../page_web_development'
DELETE_OUTPUT_DIRECTORY = True




THIS_FILES_DIR = os.path.dirname (__file__)
if not THIS_FILES_DIR: THIS_FILES_DIR = os.getcwd ()
# ^ hach to the bug, when __file__ is not abspath, but 'pelicanconf.py'
# pelican is always launched from directory with this file
ABS_OUTPUT_PATH = os.path.abspath ( os.path.join (THIS_FILES_DIR, OUTPUT_PATH))




AUTHOR = u'Vladislav'
SITENAME = u'Разработка веб-сайтов.'
SITEURL = 'file://' + ABS_OUTPUT_PATH   # вместо RELATIVE_URLS = True
VLAD1777D_SITE_PATH = 'file://' + os.path.abspath ( os.path.join (ABS_OUTPUT_PATH, '../'))




TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = u'ru'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False


JINJA_ENVIRONMENT = {}
# may be {'line_statement_prefix': '#', 'line_comment_prefix': '##'}


PLUGIN_PATHS = [join(PATH, 'plugins')]
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Web development',
    }
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
