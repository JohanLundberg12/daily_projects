#!/bin/bash

# cat file | yank (enter interactive mode where you can yank stuff to clipboard)
# docker ps | yank (maybe yank image id and then docker stop <image_id>)

#ncdu (disk usage, human readable, interactive)

# find the package your working with to debug:
# -i for case insensitive
pip freeze | grep -i 'num\|sci'

#pip list: get packages first in a two column format
# --format json: get packages in json format
# jq: json query command line tool using domain specific language (DSL)
pip list --format json | jq

printf "\n\n\n\n"

# unpack it (removing [])
# and print each on separate lines(jsonlines): -c
pip list --format json | jq -c ".[]"
pip list --format json | jq -c ".[]" | grep num