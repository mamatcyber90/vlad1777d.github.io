#! /usr/bin/python3
# -*- coding: utf-8 -*- #


def WRITE(what, lang):
	"""Translates string in "what" from Russian (default language)
	to language, specified in "lang".
	"""
	try:
		if lang == 'ru':
			return what_to_write[what]['ru']
		elif lang == 'en':
			return what_to_write[what]['en']
		else:
			return "Unsupported language ({0}).".format(lang)
	except KeyError:
		return "Not translated: " + what




def TRANSLATE(what, lang):
	"""Translates string in "what" from Russian (default language)
	to language, specified in "lang".
	"""
	try:
		if lang == 'ru':
			return what
		elif lang == 'en':
			return what_to_write[what]['en']
		else:
			return "Unsupported language ({0}).".format(lang)
	except KeyError:
		return "Not translated: " + what




what_to_write = {
	"": {
		'en':'', 'ru':''
	},  # для примера и если передали пустую строку
	
	
	### HEADER ###
	
	"welcome title": {
		'ru': u'Добро пожаловать на личную страницу Vlad1777d.',
		'en': 'Welcome to the personal page of Vlad1777d.'
	},
	
	
	
	
	### FOOTER ###
	
	u"Информация:": {
		'en':'Info:'
	},
	
	u"Личная страница Вконтакте": {
		'en':'Personal page on vk.com'
	},
	
	u"Страница проекта Твои обереги": {
		'en':'Page of Your Averters project'
	},
	
	u"Группа Вконтакте проекта Твои обереги": {
		'en':'Group of Your Averters project on vk.com'
	},
	
	u"Репозиторий тем рабочего окружения Cinnamon - Glass Themes": {
		'en':'Repository of Glass Themes - themes for Cinnamon desktop environment'
	},
	
	
	u"(ссылка в новой вкладке)": {
		'en':'(link in new tab)'
	},
	u"(еще не создано)": {
		'en':'(not created yet)'
	},
	
	u"С ув., Владислав.": {
		'en':'Best regards, Vladislav.'
	},
}


