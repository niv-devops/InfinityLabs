#!/bin/bash

echo "$1" | awk '{
    for (i=1; i<=length; i++)
    {
        char = substr($0, i, 1);
        count[char]++;
        if (!(char in occur))
        {
            occur[char] = 1;
            order = order char;
        }
    }
    for (i=1; i<=length(order); i++) 
    {
        char = substr(order, i, 1);
        printf (count[char] > 1 ? count[char] : "") char;
    }
    print "";
}'

# Another solution
echo "$1" | tr -d '\n' | sed "s/./&\n/g" | uniq -c | awk '{rle = ($1 > 1 ? $1 : "") $2; printf "%s", rle} END {print ""}'
