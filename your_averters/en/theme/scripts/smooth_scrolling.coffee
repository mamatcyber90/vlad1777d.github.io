### Main function must be launched from link with anchor.
It wll scroll there, where this anchor points.

Not neede. Use in CSS:
body {
	scroll-behavior: smooth;
}
###




window.smoothly_scroll_to_anchor = (anchor) ->
	### Must be runned from onclick event of anchor link.
	###

	current_offset = window.pageYOffset
	target_element = document.getElementById anchor
	scroll_to = target_element.offsetTop
	where_to_scroll = scroll_to - current_offset
	window.scrollBy {top: where_to_scroll, left: 0, behavior: 'smooth'}
