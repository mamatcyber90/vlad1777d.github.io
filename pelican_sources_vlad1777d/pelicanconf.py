#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from __future__ import unicode_literals
import os.path
join = os.path.join
import sys




AUTHOR = u'Vladislav'
SITENAME = u'Vlad1777d - личная страница.'
SITEURL = ''


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # сделал по образу и подобию Django
PATH = 'sources'
STATIC_PATHS = ['data', 'images', 'bootstrap', 'jquery']  # будут внутри папки PATH
ARTICLE_PATHS = ['texts']
THEME = join(PATH, 'theme_general')
DIRECT_TEMPLATES = ['index', 'page_glass_themes',
					'page_other_soft', 'page_web_development']
					# здесь написать имена тех шаблонов, которые будут включены в постоение
OUTPUT_PATH = '../'
DELETE_OUTPUT_DIRECTORY = True


TIMEZONE = u'Europe/Kiev'
DEFAULT_LANG = u'ru'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATHS = [join(PATH, 'plugins')]
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Vlad1777d - personal page.',
        'DL': 'en'
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
