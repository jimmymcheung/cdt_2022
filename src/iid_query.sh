#! /bin/bash

usage() { echo -e "\nUsage: $0 [-s /path/to/source] [-D /path/to/distination]\n\nArguments: \n	-s	Source Directory. If not supplied, current working directory will be used. In case directory name contain space, it should be escaped with double quote (\"\") or (\\ ).\n	-D	Destination directory. If not supplied, directory 'iid' under the source directory will be used or will be created (in case not exist). Space in the name should be escaped, see '-s' argument for more info." 1>&2; exit 1; }

# Get options
while getopts ":s:D:" flag
do
	case "${flag}" in
		s) sc_dir=${OPTARG};;
                D) des_dir=${OPTARG};;
		*) usage;;
        esac
done
shift $((OPTIND-1))
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
if [[ "${des_dir}" =~ .*\/$ ]]
then
	des_dir="${des_dir%/}"
fi

###### Main Programme ######
if [ -d "sc_dir" ]
then
	cd "$sc_dir" && echo "Landed at $(pwd)"
else
	echo "Error: No such directory"; exit 128
fi
if [ ! -d "$des_dir" ]
then
        mkdir "$des_dir"
fi

# export iid
for n in *.gt
do
        echo "Reading $n"
        m="${des_dir}/${n%.gt}_iid.gt"
        cat "$n" | grep -v '\(\(^rs[0-9]\+.*\)\|\(^#.*\)\)' > "$m"
        echo "Finished with $n, written in $m"
done