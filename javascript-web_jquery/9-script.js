$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (info) {
    console.log(info.hello)
    $('DIV#hello').append(info.hello)
})