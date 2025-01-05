#!/bin/bash

read -p 'Enter numbers separated by spaces: ' nums
nums=${nums//-/}
echo "Sum of nums: $(( ${nums// /+} ))"
