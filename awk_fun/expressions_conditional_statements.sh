#!/bin/bash


df | awk '$1 != "none" {print $0}'

df | awk '{
	if ($1 != "none") {
		print $0
	}
}'

#sunday=$(cal | awk 'NR==2 {printf "%s", $1}')
#monday=$(cal | awk 'NR==2 {printf "%s", $2}')
#tuesday=$(cal | awk 'NR==2 {printf "%s", $3}')
#wednesday=$(cal | awk 'NR==2 {printf "%s", $4}')
#thursday=$(cal | awk 'NR==2 {printf "%s", $5}')
#friday=$(cal | awk 'NR==2 {printf "%s", $6}')
#saturday=$(cal | awk 'NR==2 {printf "%s", $7}')

days=$(cal | awk 'NR==2 {print $1, $2, $3, $4, $5, $6, $7}')

read -r sunday monday tuesday wednesday thursday friday saturday <<< $days


cal | awk -v sunday="$sunday" -v monday="$monday" -v tuesday="$tuesday" -v wednesday="$wednesday" -v thursday="$thursday" -v friday="$friday" -v saturday="$saturday" 'NR<=2 {print $0} NR>2 {printf "%2s %2s %2s %2s %2s %2s %2s\n", sunday, monday, tuesday, wednesday, thursday, friday, saturday; print $0}' | awk 'NR==1 || NR > 2 {print $0}'

