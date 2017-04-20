get_cookie = (cookie_name) ->
	### Функция для получения значения куки.
	###
	results = document.cookie.match('(^|;) ?' + cookie_name + '=([^;]*)(;|$)')
	if results
		unescape results[2]
	else
		null




write_cookie = (cookie_name, text) ->
	### Объявим функции для записи в куки значения стиля
	(выбор пал на функцию, чтобы не сразу шла запись, а по вызову этой функции пользователем).
	###
	experation_data = new Date
	experation_data.setFullYear experation_data.getFullYear() + 1
	document.cookie = cookie_name + '=' + text + ';' + 'expires=' + experation_data + 'path=/;'
	return




is_first_start = () ->
	### Checks through cookies: does this site loads at first time, or not.
	Uses:
		get_cookie
	###
	first_start = get_cookie 'first_start'
	if (first_start == null) or (first_start == 'true')
		return true
	else
		return false




check_language = () ->
	### Asks browser about preffered language to display web-pages.
	###
	lang = (navigator.language or navigator.systemLanguage or navigator.userLanguage).substr(0, 2).toLowerCase()
	reg_expr_ru = new RegExp(/\bru\b/, 'i')
	reg_expr_en = new RegExp(/\ben\b/, 'i')

	if lang.match(reg_expr_ru)
		return 'ru'
	else if lang.match(reg_expr_en)
		return 'en'
	else
		return null




load_page_corresponding_language = ( lang ) ->
	### Вытащим из куки значение нашего стиля с помощью ранее объявленной функции и назначим переменной title
	###

	if lang == 'ru'
		#alert 'russian language'
		reg_expr = new RegExp(/en\/\w+\.html/, 'i')  # english
		reg_expr_value = document.location.href.match(reg_expr)
		if reg_expr_value != null
			reg_expr_value = document.location.href.match(reg_expr)[0]
			#alert 'matched: ' + reg_expr_value
			new_reg_expr = new RegExp(/\w+\.html/, 'i')
			new_reg_expr_value = reg_expr_value.match(new_reg_expr)[0]
			new_location = document.location.href.replace(reg_expr_value, new_reg_expr_value)
			#alert 'New location: ' + new_location
			document.location.replace new_location  # правильно

	else if lang == 'en'
		reg_expr_en = new RegExp(/en\/\w+\.html/, 'i')
		reg_expr_en_value = document.location.href.match(reg_expr_en)
		if reg_expr_en_value == null
			reg_expr = new RegExp(/\w+\.html/, 'i')
			reg_expr_value = document.location.href.match(reg_expr)[0]
			#alert 'matched: ' + reg_expr_value[0]
			new_location = document.location.href.replace(reg_expr_value, 'en/' + reg_expr_value)
			#alert 'New location: ' + new_location
			document.location.replace new_location

	else
		#alert "unknown language"
		null




switch is_first_start()
	when true
		write_cookie 'first_start', false  # сначала, ибо после загрузки страницы скрипт не пашет
		lang = check_language()
		load_page_corresponding_language lang
	when false
		null
	else
		null
