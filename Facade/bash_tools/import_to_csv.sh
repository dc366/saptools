#!/bin/bash
FULL_NAME=$1;
NAME_STEM=${FULL_NAME%.txt};
awk '{ if ($2" "$3" "$4" "$5 == "DATABASE IMPORT DETAILED LOG") exit ; print $0 }' $FULL_NAME > temp
grep 'records successfully read' temp | awk 'BEGIN { FS = ":" } ; { print $1 }' > names
grep 'records successfully read' temp | awk '{sub(/.+: /,""); print $1","$3 }' > counts
paste -d , names counts > "${NAME_STEM}_full_compiled.csv"
awk 'BEGIN { FS = "," } ; { if ($2 < $3) print $0 }' "${NAME_STEM}_full_compiled.csv" > "${NAME_STEM}_misses_compiled.csv"
rm temp
rm names
rm counts
