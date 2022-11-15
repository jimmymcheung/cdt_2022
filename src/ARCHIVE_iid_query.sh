#!/bin/bash

version=1.2
# Version 1.0
# shipped with ability to query and export private SNP ID entry.

# Version 1.1
# shipped with abiilty to query and export RSID marked SNP entry (with -r option)

# Version 1.2
# shipped with ability to query and export individual file.

usage() { local error_msg="$1" ; printf "\n\033[1m\033[7mUsage:\033[0m\n$0 [\033[1m-hrv\033[0m] [\033[1m-s\033[0m \033[4mpath/to/source\033[0m] [\033[1m-D\033[0m \033[4mpath/to/destination\033[0m] [\033[1m-f\033[0m \033[4mpath/to/file\033[0m]\n\n\033[1m\033[7mArguments:\033[0m \n\t\033[1m-D\033[0m\tDestination directory. If not supplied, directory 'iid' under the source directory will be used or will be created (in case not exist). Space in the name should be escaped, see \033[1m-s\033[0m argument for more info.\n\t\033[1m-f\033[0m\tSingle file mode. File with extension other than '.gt' is also accepted, however, it is important to include a file extension to prevent error. Input only a signle file insead of a directory.\n\t\033[1m-h\033[0m\tDisplay usage.\n\t\033[1m-r\033[0m\tReverse mode. The script will export rsid records instead of private id records. Can be combined with single file mode.\n\t\033[1m-s\033[0m\tSource Directory. If not supplied, current working directory will be used. In case directory name contain space, it should be escaped with double quote (\"\") or (\\ ).\n\t\033[1m-v\033[0m\tPrint script version.\n" >&2; exit 1; }

checksource() { if [ -n $(ls | grep *.gt) ]; then printf "\033[1mWarning: Source directory is empty\033[0m\n"; exit 1; fi }

# Variables warehouse
reverse=false
file=false

# Get options
while getopts ":s:D:f:rv" flag
do
	case "${flag}" in
		s) sc_dir=${OPTARG};;
                D) des_dir=${OPTARG};;
		f) file=${OPTARG:?Error: file cannot be empty} ;;
		r) reverse=true;;
		v) printf "Version: ${version}\n" ; exit 0;;
		*) usage;;
        esac
done
shift $((OPTIND-1))
# Validate variables
if [ "${file}" != false ] && [ -f "${file}" ]
then
	sc_dir="${file%/*}"
elif [ "${file}" != false ] && [ ! -f "${file}" ]
then
	printf "\033[1mError: File not exists\033[0m\n"
	exit 128;
fi
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
if [ "$file" = false ]
then
	if [ -d "$sc_dir" ]
	then
		cd "$sc_dir" && printf "Landed at $(pwd)\n"
	else
		printf "\033[1mError: No such source directory\033[0m\n";
		exit 128
	fi
	checksource
	if [ ! -d "$des_dir" ]
	then
	        mkdir -p "$des_dir"
	fi

	if [ "$reverse" = flase ]
	then
		# export iid
		for n in *.gt
		do
       		 	printf "Reading $n\n"
       		 	m="${des_dir}/${n%.gt}_iid.gt"
	        	cat "$n" | grep -v '\(\(^rs[0-9]\+.*\)\|\(^#.*\)\)' > "$m"
       		 	printf "Finished with $n, output written in $m\n"
		done
	elif [ "$reverse" = true ]
	then
		printf "Running in reverse mode.\n"
		# export rsid
		for n in *.gt
		do
			printf "Reading $n\n"
       		 	m="${des_dir}/${n%.gt}_rsid.gt"
			cat "$n" | grep '\(\(^rs[0-9]\+.*\)\)' > "$m"
			printf "Finished with $n, output written in $m\n"
		done
	fi
else
	f="${file##*/}"
	if [ ! -d "$des_dir" ]
	then
	        mkdir -p "$des_dir"
	fi
	if [ "$reverse" = true ]
	then
		printf "Running in reverse mode.\n"
		# export rsid
			printf "Reading ${file}\n"
       		 	m="${des_dir}/${f%.*}_rsid.gt"
			cat "$file" | grep '\(\(^rs[0-9]\+.*\)\)' > "$m"
			printf "Finished with $f, output written in $m\n"
	elif [ "$reverse" = false ]
	then
		# export iid
       		 	printf "Reading $file\n"
       		 	m="${des_dir}/${f%.*}_iid.gt"
	        	cat "$file" | grep -v '\(\(^rs[0-9]\+.*\)\|\(^#.*\)\)' > "$m"
       		 	printf "Finished with $f, output written in $m\n"
	fi
fi
