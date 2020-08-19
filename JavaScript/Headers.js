const http = require('http');
console.log('Waiting for a request')
//Run this locally to test headers. Additionally you could ssh/rdp on a server and view the output of your headers!
const server = http.createServer((request, response) => {
const url = request.url;
const method = request.method; //Make sure the request isnt set to response! That was a fun logical error.
  if (url === '/') {
    response.write('<html>');
    response.write('<head><title>Testing Headers</title></head>');
    response.write('<body><h1>Blank page.</h1></body>');
    response.write('</html>');
    console.log('The method is', request.method);
    console.log('Your current headers are', request.headers);
    console.log('Waiting for another request');
    return response.end(); 
  }  
});
//This program runs indefinitely on port 3000, you can change it to anything you'd like.
server.listen(3000);
