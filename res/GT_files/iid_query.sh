#! /bin/bash

for n in *.gt
do
        echo "Reading $n"
        cat "$n" | grep '^i[0-9]+*' > "${n%.gt}.txt"
        echo "Finish with $n"
done
