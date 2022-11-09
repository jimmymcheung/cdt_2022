#! /bin/bash

usage() { echo -e "\nUsage: $0 [-hr] [-s path/to/source] [-D path/to/destination]\n\nArguments: \n\t-D\tDestination directory. If not supplied, directory 'iid' under the source directory will be used or will be created (in case not exist). Space in the name should be escaped, see '-s' argument for more info.\n\t-h\tDisplay usage.\n\t-r\tReverse mode. The script will export rsid records instead of private id records.\n\t-s\tSource Directory. If not supplied, current working directory will be used. In case directory name contain space, it should be escaped with double quote (\"\") or (\\ )." 1>&2; exit 1; }

# Variables warehouse
reverse=false

# Get options
while getopts ":s:D:r" flag
do
	case "${flag}" in
		s) sc_dir=${OPTARG};;
                D) des_dir=${OPTARG};;
		r) reverse=true;;
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
	if [ "$reverse" = flase ]
	then
		des_dir="${sc_dir}/iid"
	elif [ "$reverse" = true ]
	then
		des_dir="${sc_dir}/rsid"
	fi
fi
if [[ "${des_dir}" =~ .*\/$ ]]
then
	des_dir="${des_dir%/}"
fi

###### Main Programme ######
if [ -d "$sc_dir" ]
then
	cd "$sc_dir" && echo "Landed at $(pwd)"
else
	echo "Error: No such source directory";
	exit 128
fi
if [ ! -d "$des_dir" ]
then
        mkdir -p "$des_dir"
fi

if [ "$reverse" = true ]
then
	echo "Running in reverse mode."
	# export rsid
	for n in *.gt
	do
		echo "Reading $n"
        	m="${des_dir}/${n%.gt}_rsid.gt"
		cat "$n" | grep '\(\(^rs[0-9]\+.*\)\)' > "$m"
		echo "Finished with $n, output written in $m"
	done
elif [ "$reverse" = false ]
then
	# export iid
	for n in *.gt
	do
        	echo "Reading $n"
        	m="${des_dir}/${n%.gt}_iid.gt"
        	cat "$n" | grep -v '\(\(^rs[0-9]\+.*\)\|\(^#.*\)\)' > "$m"
        	echo "Finished with $n, output written in $m"
	done
fi
