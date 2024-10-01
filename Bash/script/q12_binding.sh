#!/bin/bash

#set -o emacs   # Enable readline support for command line editing

bind -x '"\e[23;5~":"bash ./q10_google"'
echo "Script bound to ctrl+F11 key successfully."

bind -x '"\e[24;5~":"bash ./q11_translate"'
echo "Script bound to ctrl+F12 key successfully."
