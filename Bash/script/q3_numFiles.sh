#!/bin/bash

# Return number of files in path
dirPath="$1"  # Dir is the first argument

if [ -d "$dirPath" ]
then
    fileCount=$(find "$dirPath" -type f | wc -l)
    echo "Number of files in $dirPath: $fileCount"
else
    echo "Directory not found"
fi
