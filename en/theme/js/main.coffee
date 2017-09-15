


window.go_after_timeout = (element, event, link) ->
	### pass word "this" to "element" when launching, for example, from onclick.
	###
	setTimeout () ->
		if link isnt undefined
			document.location.href = link
	, 200
