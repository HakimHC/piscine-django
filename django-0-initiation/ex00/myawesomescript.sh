#! /bin/bash

regex='^(https://bit.ly|bit.ly)/.*$'
match_regex() {
  grep -E "$regex" <(echo "$1") >/dev/null 2>&1
}

if [[ "$#" != "1" || "$1" == "--help" || "$1" == "-h" ]]; then
  echo "usage: $0 <URL>"
  exit 1
fi

arg="$1"
if ! match_regex "$arg"; then
  echo "fatal: URL must be a bit.ly link"
  exit 1
fi

res=$(curl -I "$arg" -s | grep -i location | cut -c 11- )

if [ -z "$res" ]; then
  echo "fatal: not found"
else
  echo ${res%?}
fi
