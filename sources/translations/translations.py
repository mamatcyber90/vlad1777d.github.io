#! /usr/bin/python3
# -*- coding: utf-8 -*- #



def TRANSLATE(what, lang):
	"""Translates string in "what" from Russian (default language)
	to language, specified in "lang".
	"""
	if lang == 'ru':
		return what
	elif lang == 'en':
		try:
			return en[what]
		except KeyError:
			return "Not translated: " + what
	

TR = TRANSLATE  # shortcut








en = {
	"": "",  # для примера и если передали пустую строку
	
	# главное меню
	u"Твои обереги": "Your Averters",
	u"Главная": "Main",
	u"Новости": "News",
	u"Музыка": "Music",
	u"Фото и соц. сети": "Photo and soc. netw.",
	
	# заголовки страниц
	u"Что нового:": "News:",
	u"Музыка": "Music:",
	u"Фотографии и социальные сети:": "Photos and social network:",
}
