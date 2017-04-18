/* Объявим функцию для получения значения куки */ 
function get_cookie ( cookie_name )
	{
	var results = document.cookie.match ( '(^|;) ?' + cookie_name + '=([^;]*)(;|$)' );

	if ( results )
		return ( unescape ( results[2] ) );
	else
		return null;
	}




/* Объявим функции для записи в куки значения стиля (выбор пал на функцию, чтобы не сразу шла запись, а по вызову этой функции пользователем). */
function write_cookie ( cookie_name, text ) 
	{ 
	experation_data = new Date();	experation_data.setFullYear(experation_data.getFullYear() + 1);
	document.cookie = cookie_name + '=' + text + ';' + 'expires=' + experation_data + 'path=/;' ;
	}




write_cookie( "first_start", 1 ) ;
var first_start = get_cookie ( "first_start" );
alert("Cookie first_start: " + first_start);




/* Вытащим из куки значение нашего стиля с помощью ранее объявленной функции и назначим переменной title */
function check_language_load_page ()
	{
	var first_start = get_cookie ( "first_start" );


	if ((first_start == null) || (first_start == '1'))
		{
		var lang = (navigator.language || navigator.systemLanguage || navigator.userLanguage).substr(0, 2).toLowerCase();
		
		if ((lang == 'ru') || (lang == 'ru-ru'))
			{
			alert("russian language");
			var reg_expr = new RegExp(/en\/\w+\.html/, "i");
			var reg_expr_value = document.location.href.match(reg_expr);
			if (reg_expr_value != null)
				{
				var reg_expr_value = document.location.href.match(reg_expr)[0];
				alert("matched: " + reg_expr_value);
				var new_reg_expr = new RegExp(/\w+\.html/, "i");
				var new_reg_expr_value = reg_expr_value.match(new_reg_expr)[0];
				
				var new_location = document.location.href.replace(reg_expr_value, new_reg_expr_value);
				alert("New location: " + new_location);
				document.location.replace (new_location);
				}			
			}
		else if (lang == 'en' || 'en-us')
			{
			var reg_expr_en = new RegExp(/en\/\w+\.html/, "i");
			var reg_expr_en_value = document.location.href.match(reg_expr_en);
			if (reg_expr_en_value == null)
				{
				var reg_expr = new RegExp(/\w+\.html/, "i");
				var reg_expr_value = document.location.href.match(reg_expr);
				alert("matched: " + reg_expr_value[0]);
				var new_location = document.location.href.replace(reg_expr_value, "en/" + reg_expr_value);
				alert("New location: " + new_location);
				document.location.replace (new_location);
				}
			}
		else
			{
			/*alert("unknown language");*/
			}
		}
	
	
	else
		{write_cookie("first_start", '1' );}
	}



check_language_load_page ();
