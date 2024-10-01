#!/bin/bash

# Return the type of each file in path
read -p "Enter directory path: " dirPath

if [ -d "$dirPath" ]
then
    for file in "$dirPath"/*
    do
      fileType=$(file -b "$file" | cut -d " " -f1)
      case "$fileType" in
         directory)
            fileType="Directory"
            ;;
         block)
            fileType="Block device"
            ;;
         character)
            fileType="Character device"
            ;;
         fifo)
            fileType="Named pipe (FIFO)"
            ;;
         socket)
            fileType="Socket"
            ;;
         symbolic)
            fileType="Symbolic link"
            ;;
         *)
            fileType="Regular file"
            ;;
      esac       
      echo  -e "File name: $(basename "$file") \t\t File type: $fileType"
    done
else
    echo "Directory not found"
fi
