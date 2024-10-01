#!/bin/bash

# Delete all files in path larger than X bytes
DIR="$1"  # Dir is the first argument
X="$2"  # Bytes size is the second argument

if [ -d "$DIR" ]
then
   for file in *   #Loop files in current dir
   do
      if [ $(stat -c%s "$file") -gt "$X" ]    #Check if file size larger than X
      then
          echo "File found: '$file'"
          read -p "Confirm to delete file (yes): " confirm
          if [ "$confirm" == "yes" ]
          then
              rm -f "$file"
              echo "Successfully deleted: '$file'"
          fi
      fi
   done
else
   echo "Directory not found"
fi
