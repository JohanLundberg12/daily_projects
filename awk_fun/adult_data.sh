#!/bin/bash

CURL='/usr/bin/curl'
URL="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
OUT_FLAG="--out"
OUT="adult.data"

"$($CURL $URL $OUT_FLAG $OUT)"

cat $OUT | awk '{print $4}' | sort | uniq -c | sort -rn | head

cat $OUT | awk '{print $1, $4}' | awk '{ a[$2] += $1; count[$2]++;} END { for (i in a) {average=a[i] / count[i]; printf "%-15s\t%s\n", i, average;}}'

