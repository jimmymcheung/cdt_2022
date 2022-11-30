#!/bin/sh
#
# auto-install script, check INSTALL
# Copyright © 2022 CDT project
# Author: Jiaming Zhang

self="$(echo "$0" | sed -e 's,.*/,,')"
self_dir="$(echo "$0" | sed -e "s,/$self$,,")"
usage() {
  printf "\033[7mUsage:\033[0m\n   \033[1m%s\033[0m\
 [\033[1m-h|-?|--help\033[0m] [\033[1m--skip-check\
\033[0m] [\033[1m--ignore\033[0m \033[4mshell command\
\033[0m]\n" "$self"
}
die() {
  printf '\033[1m%s\033[0m\n' "$1" >&2
  exit 1
}

env_skip=0
sh_ignore=''

# get options
while :; do
	case $1 in
	  -h|-\?|--help)
	    usage
	    exit
	    ;;
	  --skip-check)
	    env_skip=1
	    ;;
	  --ignore)
	    if [ "$2" ]; then
	      sh_ignore=$2
	      shift
	    else
	      die 'ERROR: "--ignore" requires a file path for the python check modules script.'
	    fi
	    ;;
	  --ignore=?*)
	    sh_ignore=${1#*=};;
	  --ignore=)
	    die 'ERROR: "--ignore" requires a file path for the python check modules script.';;
	  --)
	    shift
	    break;;
	  -?*)
	    printf '\033[5m\033[1mWARN: Unknown option (ignored): %s\033[0m\n%s\n' "$1" "$(usage)" >&2
	    exit 128;;
	  *)
	    break
	esac

  shift
done
if test $# != 0; then
  printf "\033[5m\033[1m$self: too many arguments\033[0m\n%s\n" "$(usage)" >&2
  exit 1
fi

# env_check
if [ $env_skip = 0 ] && [ "$sh_ignore" = '' ]; then
  if ! "$self_dir"/src/env_check
  then
    printf "\033[1mERROR: You do not met the basic requirement \
or \033[4menv_check\033[0m\033[1m exit with an error. Check above for details.\033[0m\n"
    exit 1
  fi
elif [ $env_skip = 0 ] && [ "$sh_ignore" != '' ]; then
  if ! "$self_dir"/src/env_check --ignore "$sh_ignore";
  then
    printf "\033[1mERROR: You do not met the basic requirement \
or \033[4menv_check\033[0m\033[1m exit with an error. Check above for details.\033[0m\n"
    exit 1
  fi
elif [ $env_skip = 1 ]; then
  printf "\033[1mWARN: env_check skipped. You may encounter error during install.\033[0m\n"
else
  printf "\033[1mERROR: This script is modified.\nExiting\033[0m\n" >&2
  exit 1
fi
