$('#toggle_header').click(function() {
    if ($('header').attr('class') === 'green') {
        $('header').attr('class', 'red');
    } else if ($('header').attr('class') === 'red') {
        $('header').attr('class', 'green');
    }
})