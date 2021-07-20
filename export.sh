#!/bin/bash
# crontab -e
# */5 * * * * sudo sh /place/path/here/export.sh

file="/file/to/export"
auth="/place/path/here/auth.json"
exportpy="/place/path/here/export.py"

modify=$(expr $(expr $(date +%s) - $(stat "$file" -c %Y)))
# run if file changed during the last 300 sec
if [[ "$modify" < 300 ]]; then
  nice -n 3 ionice -c3 python3 "$exportpy" -i "$file" --spreadsheet SPREADSHEET_ID --auth "$auth" --page SPREADSHEETS_PAGE_NAME
fi

# https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit