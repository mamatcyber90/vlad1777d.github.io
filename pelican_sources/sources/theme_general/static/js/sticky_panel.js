$(window).scroll(function() {
    if ($(this).scrollTop() > 1){  
        $('#top_panel').addClass("sticky");
    }
    else{
        $('#top_panel').removeClass("sticky");
    }
});
