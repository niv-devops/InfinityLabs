#!/bin/bash

students=( "Alm" "Arin" "Matan" "Eitan" "Yarin" "Sharon" "Niv" "Amit" "Or" "Yakir" "Liraz" )
students=( $(shuf -e "${students[@]}") )

length=${#students[*]}

if [ $length%2 == 0 ]
then
   for ((i=0; i<length-1; i+=2))
   do
      echo "Pair: ${students[i]} & ${students[i+1]}"
   done
   
else
   echo "Trio: ${students[0]} & ${students[1]} & ${students[2]}"
   for ((i=3; i<length-1; i+=2))
   do
      echo "Pair: ${students[i]} & ${students[i+1]}"
   done
fi
