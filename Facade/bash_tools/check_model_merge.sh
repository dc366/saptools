#!/bin/bash

#run script to create csv files
find . -name "*.txt" -exec "/d/WPy64-3850/notebooks/Facade/bash_tools/import_to_csv.sh" "{}" \;

#check csv files for misses

#set to allow **/*
shopt -s globstar

#set counter
count=0

for i in **/*misses_compiled.csv
do	
	#save first file
	if [ $count == 0 ] 
	then 
		firstfile="$i" 
	fi

	#print current file name
	echo "$i"

	#compare this file against the first file for unexpected conflicts
	echo "    unexpected conflicts:"
	awk -F, 'FNR==NR {a[$1]=$0; next}; {if($1 in a == 0) {print $0}}' "$firstfile" "$i"

	#print every conflict with a non-zero import count
	echo "    partial imports:"
	awk -F, 'BEGIN { FS = "," } ; { if ($2 > 0) print $0}' "$i"

	#end loop
	((count++))
done

#unset globstar
shopt -u globstar
