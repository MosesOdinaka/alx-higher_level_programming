#!/usr/bin/node
// Import the 'request' module
const httpRequest = require('request');

// Define the URL
const apiUrl = process.argv[2];

// Define the callback function
function countCharacters(error, response, responseBody) {
  if (error) console.log(error);
  let characterList = [];
  for (const movie of JSON.parse(responseBody).results) {
    characterList = characterList.concat(movie.characters);
  }
  const filteredCharacters = characterList.filter(character => character.includes('18'));
  console.log(filteredCharacters.length);
}

// Send a GET request to the URL and count the characters
httpRequest(apiUrl, countCharacters);
