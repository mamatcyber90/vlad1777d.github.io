

top_panel_current_position = $('#top_panel').offset().top  # относительно начала страницы


change_panel = () ->
	alert "scrolled"
	if $(this).scrollTop() > top_panel_current_position
		$('#top_panel').addClass 'sticky'
	else
		$('#top_panel').removeClass 'sticky'
	return


#$(window).scroll (change_panel)
window.addEventListener ("scroll", change_panel)
#window.onscroll = change_panel

