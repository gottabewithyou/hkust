#!/bin/bash

while true; do
  nc chal.firebird.sh 33004 << EOF
a\n
EOF
  read -r -d '' response <<< "$(cat)"  # Use a here string to capture the entire output
  echo "$response"
done