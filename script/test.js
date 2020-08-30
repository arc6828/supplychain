const Nightmare = require('nightmare')
const nightmare = Nightmare({ show: true })

nightmare
    //FETCH URL
    .goto('https://duckduckgo.com')
    //TYPE SPECIFIED INPUT
    .type('#search_form_input_homepage', 'github nightmare')
    //CLICK SPECIFIED BUTTON
    .click('#search_button_homepage')
    //WAIT UNTIL ELEMENT IS PRESENT
    .wait('a.result__a')

    .evaluate(() => {
        let elements = document.querySelectorAll('a.result__a');
        let urls = Array.from(elements).map(el => el.href);
        return JSON.stringify(urls);

    })
    .end()
    .then((text) => {
        text = JSON.parse(text);
        text.forEach((t)=>console.log(t))
        /*
        elements.forEach(function(el) {
            console.log(el.href);
        });*/

    })
    .catch(error => {
        console.error('Search failed:', error)
    })