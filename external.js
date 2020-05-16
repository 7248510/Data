//Thought: Combine this program and the headers program
const http = require('http')
const cheerio = require('cheerio')
const fs = require('fs')
//
const req = http.request('http://api.ipify.org/', response => {
//Returning the status code
    response.on('data', body => {
    const $ = cheerio.load(body)
    externalIP = $('body').text()
    console.log("Your external IP address is:",externalIP) //Outputting your external IP
    })
})
//Error handling
req.on('error', error =>
{   
    console.error(error);
})
//Ending the request
req.end();
