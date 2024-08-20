#!/bin/bash

while true; do
  nc chal.firebird.sh 33004 << EOF
a
EOF
  read -r -d '' response <&1
  if [[ "$response" =~ "Unfortunate. Try again" ]]; then
    echo "Trying again..."
  else
    echo "Success!"
    break
  fi
done