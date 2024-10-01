#!/bin/bash

set -o emacs   # Enable readline support for command line editing

bind -x '"\e[21;5~":"bash ./q7_converClipboard"'

echo "Script bound to ctrl+F10 key successfully."
