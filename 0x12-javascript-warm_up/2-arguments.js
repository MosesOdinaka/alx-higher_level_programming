#!/usr/bin/node
if (Process.argv.length === 2) {
    console.log("No argument");
}
if (Process.argv.length === 3) {
    console.log("Argument found");
}
if (Process.argv.length > 3) {
    console.log("Argument found");
}
