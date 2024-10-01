#!/bin/bash

#Questions
echo "------------------Questions------------------"
#Q4
arr=(text1 333 text3 ok)

#Q5
echo "all elements: ${artcell[*]}"
echo "Third element: ${arr[-1]}"

#Q6
for elem in ${arr[@]}
    do
        echo $elem
done 

#Q7
my_array1=(3 4 5 6)
my_array2=(3,4,5,6)
echo "all elements: ${#my_array1[*]}"
echo "all elements: ${#my_array1[@]}"
echo "all elements: ${#my_array2[*]}"
echo "all elements: ${#my_array2[@]}"

#Exercises
echo "------------------Exercises------------------"
#Ex1
echo "Number of lines: $(wc -l < /home/niv/Worksheets/bash_script/example.txt)"

#Ex2
ls_output='ls/usr | wc -l'

#Ex3
declare -A mentors_emails=([Naftali]="naf@ilrd.co.il" [Tal]="tal@ilrd.co.il" [Ilya]="ilya@ilrd.co.il")

PS3='Please enter your choice: '

select name in Naftali Tal Ilya Exit
do
    if [ "$name" == 'Exit' ] 
    then
        break
    fi
    echo "Email of $name: ${mentors_emails[$name]}"
done
echo "Bye"
