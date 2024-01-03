#!/usr/bin/node
// Import the 'request' module
const httpRequest = require('request');

// Define the URL
const url = process.argv[2];

// Define the callback function
function logStatusCode(response) {
  console.log(`Status code: ${response.statusCode}`);
}

// Send a GET request to the URL and log the status code
httpRequest.get(url).on('response', logStatusCode);
