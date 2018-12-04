#!/bin/bash

RESULT=0
declare -A FOUND  # associative array reqires bash
FOUND[0]=true

mapfile -t OPERATIONS < input.txt

while true
do
	for op in "${OPERATIONS[@]}"
	do
		RESULT=$(expr $RESULT ${op:0:1} ${op:1})
		if [[ "${FOUND[$RESULT]}" ]]
		then
			echo "ANSWER: $RESULT"
			exit
		fi
		FOUND+=([$RESULT]=true)
	done
done
