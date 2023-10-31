#!/bin/bash

grep "CLUE" ./crimescene

echo -e "\nWe get 3 clues telling us: 1. That the suspect is a male 2. That a wallet suspected of belonging to the killer has been found, which has membership cards for AAA, Delter_SkyMiles and Museum_of_Bash_History 3. A witness with the name of Annabel may have seen something\n"

grep "Annabel" ./people

echo -e "\nThere are two Annabels we need to track down. However, the one on Buckigham Place 38 (line 179) is the right one.\n"

head -n 179 ./streets/Buckingham_Place | tail -n 1

echo -e "\nThe above tells us to check the interview they did at her address.\n"

cat ./interviews/interview-699607

echo -e "\nShe informs us that she did not see the killer but she saw a Blue Honda driving away. She saw a license plate starting with L337 and ending with 9.\n"

grep -A 5 "L337" ./vehicles | grep -A 5 -B 1 "Honda" | grep -A 5 -B 2 "Blue" | awk '/Owner/ {print $0}'

echo -e "\nThere are several owners of a blue honda with the license plate described.\n"

cat ./memberships/AAA ./memberships/Delta_SkyMiles ./memberships/Museum_of_Bash_History | grep "Jeremy Bowers"

echo -e "\nJeremy Bowers happens to be a member of each of the three clumbs mentioned in one of the CLUE's\n"

cd ..

echo -e "Jeremy Bowers" | $(command -v md5 || command -v md5sum) | grep -qif /dev/stdin encoded && echo CORRECT\! GREAT WORK, GUMSHOE. || echo SORRY, TRY AGAIN.

echo -e "\nIt was him. Done! L337!"

