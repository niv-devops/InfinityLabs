#!/bin/bash

#Translate string from clipboard using google translate
clipboard="$(xclip -o)"   #Get string from clipboard
echo "the string from clipboard is: $clipboard"

PS3='Select string language: '

select lang in English Hebrew
do
   # --------- English to Hebrew ---------
   if [ "$lang" == 'English' ]
   then
   #Use curl Client for URL data transfer protocol to send a GET request to the Google Translate API endpoint to translate text
   translation=$(curl -sG --data-urlencode "sl=en" --data-urlencode "tl=he" --data-urlencode "q=$clipboard" "https://translate.googleapis.com/translate_a/single?client=gtx&dt=t")

   translated_word=$(echo "$translation" | jq -r '.[0][0][0]')   #Parse translation from JSON response
   echo "$clipboard in Hebrew is: $translated_word"
   break
     
   # --------- Hebrew to English ---------
   elif [ "$lang" == 'Hebrew' ]
   then
    translation=$(curl -sG --data-urlencode "sl=he" --data-urlencode "tl=en" --data-urlencode "q=$clipboard" "https://translate.googleapis.com/translate_a/single?client=gtx&dt=t")
    translated_word=$(echo "$translation" | jq -r '.[0][0][0]')
   echo "$clipboard in English is: $translated_word"
   break
     
   # --------- Wrong input ---------
   else
     echo "Not valid option"
     break
   fi
done
