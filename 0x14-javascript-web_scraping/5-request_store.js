#!/usr/bin/node
// Import the 'fs' and 'request' modules
const fileSystem = require('fs');
const httpRequest = require('request');

// Define the URL and output file path
const url = process.argv[2];
const outputPath = process.argv[3];

// Send a GET request to the URL and pipe the response to the output file
httpRequest(url).pipe(fileSystem.createWriteStream(outputPath));
