###
Uses:
	coffeescript_compiler.js
###




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





window.get_cookie = get_cookie
window.write_cookie = write_cookie
