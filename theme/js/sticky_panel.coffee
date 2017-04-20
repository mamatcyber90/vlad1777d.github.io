#top_panel_current_position = $('#top_panel').offset().top  # относительно начала страницы к версии скрипта с jQuery

top_panel = document.getElementById('top_panel')
top_panel_current_position = top_panel.getBoundingClientRect().top + window.pageYOffset
# относительно начала страницы


###change_panel = () ->  # версия с jQuery
	if $(this).scrollTop() > (top_panel_current_position - 20)
		$('#top_panel').addClass 'top_panel_sticky'
	else
		$('#top_panel').removeClass 'top_panel_sticky'
	return
###


change_panel_v2 = () ->
	if window.pageYOffset > (top_panel_current_position - 20)  # or window.srollY
		top_panel.classList.add ( 'top_panel_sticky' )
	else
		top_panel.classList.remove ( 'top_panel_sticky' )


window.document.addEventListener("scroll", change_panel_v2)
window.addEventListener("load", change_panel_v2)
