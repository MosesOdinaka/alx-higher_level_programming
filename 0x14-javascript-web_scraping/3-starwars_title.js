#!/usr/bin/node
// Import the 'request' module
const httpRequest = require('request');

// Define the URL
const filmUrl = 'http://swapi.co/api/films/' + process.argv[2];

// Define the callback function
function displayFilmTitle (error, httpResponse, responseBody) {
  console.log(JSON.parse(responseBody).title || error);
}

// Send a GET request to the URL and display the film title
httpRequest(filmUrl, displayFilmTitle);
