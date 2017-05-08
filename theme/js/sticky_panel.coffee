###
Uses:
	coffeescript_compiler.js
	cookies.coffee
###




top_panel = document.getElementById('top_panel')
top_panel_current_position = top_panel.getBoundingClientRect().top + window.pageYOffset  # смещение относительно начала страницы


#if document.location.hash != ""  # чтобы не было глюков при новой загрузке страницы и хэша
#	top_panel.classList.add ( 'top_panel_sticky' )


change_panel_v2 = () ->
	if window.pageYOffset > (top_panel_current_position)  # or window.srollY
		top_panel.classList.add ( 'top_panel_sticky' )
	else
		top_panel.classList.remove ( 'top_panel_sticky' )




content_block = document.getElementById ('block_content')


scroll_to_content = () ->
	top_panel_height = top_panel.getBoundingClientRect().bottom - top_panel.getBoundingClientRect().top
	from_top_to_content = content_block.getBoundingClientRect().top + window.pageYOffset
	
	window.scrollTo( 0, from_top_to_content - top_panel_height )


move_a_bit_top = () ->
	### Needed to correct position because of panel on screen (in case of using hashes).
	(currently not used)
	###
	top_panel_height = top_panel.getBoundingClientRect().bottom - top_panel.getBoundingClientRect().top
	if location.hash == "#block_content"
		window.scrollTo( 0, window.pageYOffset - top_panel_height )


remove_hash = () ->
	new_loc = window.location.href.replace window.location.hash, ""
	history.replaceState {}, "", new_loc


add_scrolling_to_content_on_load = () ->
	window.addEventListener("load", scroll_to_content)


write_scrolling_requiest_to_cookies = () ->
	write_cookie 'move_to_content_block', "true"
	alert "writing"




window.content_block = content_block  # делаем доступными всем остальным модулям
window.top_panel = top_panel

window.change_panel_v2 = change_panel_v2
window.scroll_to_content = scroll_to_content
window.move_a_bit_top = move_a_bit_top
window.add_scrolling_to_content_on_load = add_scrolling_to_content_on_load
window.write_scrolling_requiest_to_cookies = write_scrolling_requiest_to_cookies




window.document.addEventListener("scroll", change_panel_v2)
window.addEventListener("load", change_panel_v2)




###switch get_cookie "move_to_content_block"
	when "true"
		alert "true"
		add_scrolling_to_content_on_load()
		write_cookie "move_to_content_block", "false"
	else
		null
		alert "not true"
###
