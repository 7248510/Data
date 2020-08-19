//https://nodejs.dev/making-http-requests-with-nodejs
//https://cheerio.js.org/
const http = require('http')
const cheerio = require('cheerio')
const fs = require('fs')
//
//I'm in the process of learning Node.JS, It's a really fun language! 
const req = http.request('INPUT_URL', response => {
//Returning the status code
//console.log(`statuscode: ${req.statusCode}`)  
    response.on('data', body => {
    //console.log(body) //This only outputs the buffer's(Depending on how big the request is, multiple buffers may show)
    //process.stdout.write(body); //Outputs the html
    fs.writeFileSync("./body.html", body) //Writing FileSync removes the call back error? This writes an html file from the request data.
    const $ = cheerio.load(body)
    testing = $('a').text()
    console.log(testing) //Lists the a elements from the document.
    
    //return body;
    })
    //console.log(body); body becomes unreachable
})
//Error handling
req.on('error', error =>
{   
    console.error(error);
})
req.end();
