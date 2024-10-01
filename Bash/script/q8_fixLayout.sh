#!/bin/bash

# Convert English--><--Hebrew according to keyboard layout
declare -A english=(["a"]="ש" ["b"]="נ" ["c"]="ב" ["d"]="ג" ["e"]="ק" ["f"]="כ" ["g"]="ע" ["h"]="י" ["i"]="ן" ["j"]="ח" ["k"]="ל" ["l"]="ך" ["m"]="צ" ["n"]="מ" ["o"]="ם" ["p"]="פ" ["q"]="/" ["r"]="ר" ["s"]="ד" ["t"]="א" ["u"]="ו" ["v"]="ה" ["w"]="'" ["x"]="ס" ["y"]="ט" ["z"]="ז")
declare -A hebrew=(["ש"]="a" ["נ"]="b" ["ב"]="c" ["ג"]="d" ["ק"]="e" ["כ"]="f" ["ע"]="g" ["י"]="h" ["ן"]="i" ["ח"]="j" ["ל"]="k" ["ך"]="l" ["צ"]="m" ["מ"]="n" ["ם"]="o" ["פ"]="p" ["/"]="q" ["ר"]="r" ["ד"]="s" ["א"]="t" ["ו"]="u" ["ה"]="v" ["'"]="w" ["ס"]="x" ["ט"]="y" ["ז"]="z")

string="$1"  #Get string as first argument

PS3='Correct this string to: '

select lang in English Hebrew
do
   # Correct to English
   if [ "$lang" == 'English' ]
   then
     length=${#string}
     new_string=""
     for ((i = 0; i < length; i++)); do
       char="${string:i:1}"
       new_string+="${hebrew[$char]}"
     done
     echo "Converted string: $new_string"
     setxkbmap us   #change keyboard layout to English
     echo "Keyboard layout changed to English"
     break
     
   # Correct to Hebrew 
   elif [ "$lang" == 'Hebrew' ]
   then
     length=${#string}
     new_string=""
     for ((i = 0; i < length; i++)); do
       char="${string:i:1}"
       new_string+="${english[$char]}"
     done
     echo "Converted string: $new_string"
     setxkbmap il   #change keyboard layout to Hebrew
     echo "Keyboard layout changed to Hebrew"
     break
     
   # Wrong input
   else
     echo "Not valid option"
     break
   fi
done
