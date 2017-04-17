#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from __future__ import unicode_literals
import os.path
join = os.path.join
import sys




AUTHOR = u'Vladislav'
SITENAME = u'Личная страница Vlad1777d.'
SITEURL = ''


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # сделал по образу и подобию Django
PATH = 'sources'
STATIC_PATHS = ['data', 'images']  # будут внутри папки PATH
ARTICLE_PATHS = ['texts']
THEME = join(PATH, 'theme_general')
DIRECT_TEMPLATES = ['index']  # здесь написать имена тех шаблонов, которые будут отрендерены
DELETE_OUTPUT_DIRECTORY = True


TIMEZONE = 'Europe/Kiev'
DEFAULT_LANG = u'ru'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATHS = [join(PATH, 'plugins')]
PLUGINS = ['i18n_subsites']
#JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Personal page Vlad1777d.',
        'DL': 'en'
    }
}
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.join(PATH, 'translations')))
from translations import *










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
