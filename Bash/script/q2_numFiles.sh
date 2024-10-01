#!/bin/bash

# Return number of files in path
read -p "Enter directory path: " dirPath

if [ -d "$dirPath" ]
then
    fileCount=$(find "$dirPath" -type f | wc -l)
    echo "Number of files in $dirPath: $fileCount"
else
    echo "Directory not found"
fi
