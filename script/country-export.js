const Nightmare = require('nightmare')
const nightmare = Nightmare({ show: true })

nightmare
//TRADE MAP
    //FETCH URL
    .goto('https://www.trademap.org')
    //CLICK LOGIN
    .click('#ctl00_MenuControl_marmenu_login')
//LOGIN
    //WAIT UNTIL ELEMENT IS PRESENT
    .wait('#Username')
    //TYPE SPECIFIED INPUT
    .type('#Username', 'chavalit.kow@gmail.com')
    .type('#Password', 'kakkak1')
    //CLICK LOGIN
    .click('button[name="button"]')
//TRADEMAP AGAIN
    //WAIT
    .wait('#ctl00_PageContent_RadComboBox_Product_Input')
    //TYPE RICE
    .type('#ctl00_PageContent_RadComboBox_Product_Input', ' rice')
    //CLICK TITLE 1006
    .wait('div[title="1006 - Rice"]')
    .click('div[title="1006 - Rice"]')
    //CLICK MONTHLY TIME SERIES
    .click('#ctl00_PageContent_Button_TimeSeries_M')
//TARTGET PAGE
    //WAIT
    .wait('#ctl00_PageContent_MyGridView1')
    //CHOOSE IMPORT
    .click('#ctl00_PageContent_GridViewPanelControl_ImageButton_ExportExcel')
    //.type('#ctl00_PageContent_RadComboBox_Product_Input', ' rice')
    .type('body', '\u000d')

    
    //CHOOSE MODE COUNTRY
    //SELECT DROP DOWN COUNTRIES



    // //TYPE SPECIFIED INPUT
    // .type('#search_form_input_homepage', 'github nightmare')
    // //CLICK SPECIFIED BUTTON
    // .click('#search_button_homepage')
    // //WAIT UNTIL ELEMENT IS PRESENT
    // .wait('a.result__a')

    // .evaluate(() => {
    //     let elements = document.querySelectorAll('a.result__a');
    //     let urls = Array.from(elements).map(el => el.href);
    //     return JSON.stringify(urls);

    // })
    //.end()
    // .then((text) => {
    //     text = JSON.parse(text);
    //     text.forEach((t)=>console.log(t))
    //     /*
    //     elements.forEach(function(el) {
    //         console.log(el.href);
    //     });*/

    // })
    .catch(error => {
        console.error('Search failed:', error)
    })