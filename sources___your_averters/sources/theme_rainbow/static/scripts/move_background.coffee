window.move_background = {}
#window.move_background.blue_background___element = {}




turn_on_scrolling = () ->
	prepare_variables()
	header___element = window.move_background.header___element
	header___element.addEventListener 'mousemove', on_mouse_move
	header___element.addEventListener 'touchmove', on_touch_move


turn_off_scrolling = () ->
	header___element = window.move_background.header___element
	header___element.removeEventListener 'mousemove', on_mouse_move
	header___element.removeEventListener 'touchmove', on_touch_move


prepare_variables = () ->
	calculate_variables___browser()
	calculate_variables___for_dark_background()
	calculate_variables___for_blue_background()


calculate_variables___browser = () ->
	width_of_screen = window.innerWidth
	height_of_screen = window.innerHeight

	header___element = document.getElementById("header")

	screen_center_x = width_of_screen / 2
	screen_center_y = height_of_screen / 2  # because height of screen causes errors

	window.move_background.width_of_screen = width_of_screen
	window.move_background.height_of_screen = height_of_screen

	window.move_background.header___element = header___element

	window.move_background.screen_center_x = screen_center_x
	window.move_background.screen_center_y = screen_center_y


calculate_variables___for_dark_background = () ->
	width_of_screen = window.move_background.width_of_screen
	height_of_screen = window.move_background.height_of_screen
	dark_background___element = document.getElementsByClassName("header___background_black")[0]

	width_of_background = dark_background___element.offsetWidth
	height_of_background = dark_background___element.offsetHeight

	if width_of_background > width_of_screen
		dark_background___amount_of_moving_x = width_of_background - width_of_screen
	else
		dark_background___amount_of_moving_x = width_of_screen - width_of_background
	if height_of_background > height_of_screen
		dark_background___amount_of_moving_y = height_of_background - height_of_screen
	else
		dark_background___amount_of_moving_y = height_of_screen - height_of_background

	window.move_background.dark_background___element = dark_background___element
	window.move_background.dark_background___amount_of_moving_x = dark_background___amount_of_moving_x
	window.move_background.dark_background___amount_of_moving_y = dark_background___amount_of_moving_y


calculate_variables___for_blue_background = () ->
	width_of_screen = window.move_background.width_of_screen
	height_of_screen = window.move_background.height_of_screen
	blue_background___element = document.getElementsByClassName("header___background_sky")[0]

	width_of_background = blue_background___element.offsetWidth
	height_of_background = blue_background___element.offsetHeight

	if width_of_background > width_of_screen
		blue_background___amount_of_moving_x = width_of_background - width_of_screen
	else
		blue_background___amount_of_moving_x = width_of_screen - width_of_background
	if height_of_background > height_of_screen
		blue_background___amount_of_moving_y = height_of_background - height_of_screen
	else
		blue_background___amount_of_moving_y = height_of_screen - height_of_background

	moving_from_one_mousemoving___x = blue_background___amount_of_moving_x / width_of_screen
	moving_from_one_mousemoving___y = blue_background___amount_of_moving_y / height_of_screen

	window.move_background.blue_background___element = blue_background___element
	window.move_background.blue_background___amount_of_moving_x = blue_background___amount_of_moving_x
	window.move_background.blue_background___amount_of_moving_y = blue_background___amount_of_moving_y

	window.move_background.moving_from_one_mousemoving___x = moving_from_one_mousemoving___x
	window.move_background.moving_from_one_mousemoving___y = moving_from_one_mousemoving___y


on_mouse_move = (event) ->
	moved_x = event.clientX
	moved_y = event.clientY

	move_backgrounds moved_x, moved_y


on_touch_move = (event) ->
	moved_x = event.touches[0].clientX
	moved_y = event.touches[0].clientY
	move_backgrounds moved_x, moved_y


move_backgrounds = (moved_x, moved_y) ->
		window.move_background.moved_x = moved_x
		window.move_background.moved_y = moved_y

		move_dark_background()
		move_blue_background()


move_dark_background = () ->
	width_of_screen = window.move_background.width_of_screen
	height_of_screen = window.move_background.height_of_screen

	screen_center_x = window.move_background.screen_center_x
	screen_center_y = window.move_background.screen_center_y

	moved_x = window.move_background.moved_x
	moved_y = window.move_background.moved_y

	dark_background___element = window.move_background.dark_background___element
	dark_background___amount_of_moving_x = window.move_background.dark_background___amount_of_moving_x
	dark_background___amount_of_moving_y = window.move_background.dark_background___amount_of_moving_y

	moving_from_one_mousemoving___x = dark_background___amount_of_moving_x / width_of_screen
	moving_from_one_mousemoving___y = dark_background___amount_of_moving_y / height_of_screen

	amount_moved_x = moved_x - screen_center_x
	amount_of_transform_x = amount_moved_x * moving_from_one_mousemoving___x
	amount_moved_y = moved_y - screen_center_y
	amount_of_transform_y = amount_moved_y * moving_from_one_mousemoving___y

	dark_background___element.style.transform = 'translateX(' + amount_of_transform_x + "px)"
	dark_background___element.style.transform += ' translateY(' + amount_of_transform_y + "px)"


move_blue_background = () ->
	width_of_screen = window.move_background.width_of_screen
	height_of_screen = window.move_background.height_of_screen

	screen_center_x = window.move_background.screen_center_x
	screen_center_y = window.move_background.screen_center_y

	cursor_moved_x = window.move_background.moved_x
	cursor_moved_y = window.move_background.moved_y

	blue_background___element = window.move_background.blue_background___element
	max_moving_x = window.move_background.blue_background___amount_of_moving_x
	max_moving_y = window.move_background.blue_background___amount_of_moving_y

	moving_from_one_mousemoving___x = max_moving_x / width_of_screen
	moving_from_one_mousemoving___y = max_moving_y / height_of_screen

	target_moving_x = cursor_moved_x * moving_from_one_mousemoving___x
	target_moving_y = cursor_moved_y * moving_from_one_mousemoving___y

	blue_background___element.style.left = -target_moving_x + "px"
	blue_background___element.style.top = -target_moving_y + "px"




switch document.readyState
	when "loading", "interactive"
		window.addEventListener "load", turn_on_scrolling
	when "complete"
		turn_on_scrolling()

window.addEventListener "resize", turn_on_scrolling
