#!/usr/bin/node
// Import the 'fs' module
const fileSystem = require('fs');

// Define the file path and encoding
const filePath = process.argv[2];
const encodingType = 'utf-8';

// Define the callback function
function displayFileContent (err, fileContent) {
  console.log(err || fileContent);
}

// Read the file
fileSystem.readFile(filePath, encodingType, displayFileContent);
