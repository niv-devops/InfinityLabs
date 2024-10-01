#!/bin/bash

#Rename all files in dir to 'YYYY-MM-DD-filename"
current_date=$(date +%Y-%m-%d)

for file in *   #Loop files in current dir
do
    if [ -f "$file" ]    #Check if regular file
    then
        new_file="${current_date}-${file}"
        mv "$file" "$new_file"
        echo "Successfully renamed '$file' to '$new_file'"
    fi
done
