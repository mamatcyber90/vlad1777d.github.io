#! /usr/bin/python3
# -*- coding: utf-8 -*- #



def TRANSLATE(what, lang):
	"""Translates string in "what" from Russian (default language)
	to language, specified in "lang".
	"""
	try:
		if lang == 'ru':
			return translations[what]['ru']
		elif lang == 'en':
			return translations[what]['en']
		else:
			return "Unsupported language ({0}).".format(lang)
	except KeyError:
		return "Not translated: " + what
	

TR = TRANSLATE  # shortcut








translations = {
	"": {
		'en':'', 'ru':''
	},  # для примера и если передали пустую строку

	"welcome title": {
		'ru':u'Добро пожаловать на личную страницу Vlad1777d.',
		'en':'Welcome to the personal page of Vlad1777d.'
	},
}
