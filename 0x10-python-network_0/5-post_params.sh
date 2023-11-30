#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -sX POST -d "email=test@gmail.com.com&subject=I will always be here for PLD" "$1"
