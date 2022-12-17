$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(info) {
    for (let PEPE1 = 0; PEPE1 < info.results.length; PEPE1++) {
        console.log(info.results[PEPE1].title)
        $('UL#list_movies').append(`<li>${info.results[PEPE1].title}</li>`)
    }
});