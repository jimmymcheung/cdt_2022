#! /bin/bash

# Get options
while getopts s:D:h: flag
do
	case "${flag}" in
		s) sc_dir=${OPTARG};;
                D) des_dir=${OPTARG};;
		h) echo -e "Usage: \nArguments: \n	-D	Destination directory. If directory name contain space, it should be escaped with double quote (\"\") or (\\ ).";;
		*) echo -e "Error: invalid argument found. Usage: \nArguments: \n	-s	Source Directory. If not supplied, current working directory will be used. In case directory name contain space, it should be escaped with double quote (\"\") or (\\ ).\n	-D	Destination directory. If not supplied, directory 'iid' under the source directory will be used or will be created (in case not exist)."
        esac
done
# Validate variables
if [ -z "${sc_dir}" ]
then
	sc_dir="."
fi
if [[ "${sc_dir}" =~ .*\/$ ]]
then
	sc_dir="${sc_dir%/}"
fi
if [ -z "${des_dir}" ]
then
	des_dir="${sc_dir}/iid"
fi

###### Main Programme ######
( cd "$sc_dir" && echo "Landed at $(pwd)" ) || ( echo "No such directory" && exit )
if [ ! -d "$des_dir" ]
then
        mkdir "$des_dir"
fi

# export iid
for n in *.gt
do
        echo "Reading $n"
        m="${des_dir}/${n%.gt}_iid.gt"
        cat "$n" | grep '^i[0-9]+*' > "$m"
        echo "Finished with $n, written in $m"
done
