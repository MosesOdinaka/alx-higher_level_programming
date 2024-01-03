#!/usr/bin/node
// Import the 'fs' module
const fileSystem = require('fs');

// Define the file path and content
const filePath = process.argv[2];
const fileContent = process.argv[3];

// Define the callback function
function handleError(error) {
  if (error) console.log(error);
}

// Write to the file
fileSystem.writeFile(filePath, fileContent, handleError);
