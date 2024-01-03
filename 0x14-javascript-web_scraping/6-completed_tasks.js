#!/usr/bin/node
// Import the 'request' module
const httpRequest = require('request');

// Define the URL
const apiUrl = process.argv[2];

// Define the callback function
function countCompletedTasks(error, response, responseBody) {
  if (!error) {
    const tasks = JSON.parse(responseBody);
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed && completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 1;
      } else if (task.completed) {
        completedTasks[task.userId] += 1;
      }
    });
    console.log(completedTasks);
  }
}

// Send a GET request to the URL and count the completed tasks
httpRequest(apiUrl, countCompletedTasks);
