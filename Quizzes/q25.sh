#!/bin/bash
find / -type f -exec grep -l -i "word" {} \;
