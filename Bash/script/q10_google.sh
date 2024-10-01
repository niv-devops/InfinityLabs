#!/bin/bash

#Search google for string given by user
#read -p "Serach Google for: " google

#Search google for string in clipboard
google="$(xclip -o)"   #Get string from clipboard
echo "the string from clipboard is: $google"

echo "Searching for : $google"

for string in $google ; do
    echo "$string"
    search="$search%20$string"
done
    open "http://www.google.com/search?q=$search"
