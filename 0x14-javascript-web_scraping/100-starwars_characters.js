#!/usr/bin/node
// Import the 'request' module
const httpRequest = require('request');

// Define the URL
const filmApiUrl = 'https://swapi.co/api/films/' + process.argv[2];

// Define the callback function for character names
function displayCharacterName(error, response, responseBody) {
  if (!error) {
    console.log(JSON.parse(responseBody).name);
  }
}

// Define the callback function for film characters
function fetchCharacterNames(error, response, responseBody) {
  if (!error) {
    const characterUrls = JSON.parse(responseBody).characters;
    characterUrls.forEach((characterUrl) => {
      httpRequest(characterUrl, displayCharacterName);
    });
  }
}

// Send a GET request to the URL and fetch the character names
httpRequest(filmApiUrl, fetchCharacterNames);
