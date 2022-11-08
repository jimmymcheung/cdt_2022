#! /bin/bash

if [ ! -d "./iid" ]
then
        mkdir ./iid
fi

# export iid
for n in *.gt
do
        echo "Reading $n"
        m="./iid/${n%.gt}_iid.gt"
        cat "$n" | grep '^i[0-9]+*' > "$m"
        echo "Finish with $n, written in $m"
done
