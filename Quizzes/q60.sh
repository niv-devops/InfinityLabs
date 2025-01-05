#!/bin/bash

if [ -z "$1" ]; then
  echo "File not provided: $0 <path_to_text_file>"
  exit 1
elif [ ! -f "$1" ]; then
  echo "File not found: $1"
  exit 1
fi

while IFS= read -r line; do
  if echo "$line" | grep -q -E '\b([a-zA-Z0-9]+)\s+\1\b'; then
    echo "$line"
  fi
done < "$1"
