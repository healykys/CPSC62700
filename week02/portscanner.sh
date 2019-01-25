#!/bin/bash

# Basic bash port scanner

# display a usage message if incorrect number of arguments
function usage
{
	echo "Args = $#"
	if [[ "$#" -ne 0 ]] && [[ "$#" -ne 2 ]] && [[ "$#" -ne 3 ]] && [[ "$#" -ne 5 ]]
	then
		echo "Usage: ./portscanner.sh [-t timeout] [<host> <startport> <stopport>]"
		exit
	fi
}
usage

# populate our variables from the arguments.
host=$1
startport=$2
stopport=$3

# function pingcheck
# ping a device to see if it is up
function pingcheck
{
	pingresult=$(ping -c 1 $host | grep bytes | wc -l)
	if [ "$pingresult" -gt 1 ]
	then
		echo "$host is up"
	else
		echo "$host is down, quitting"
		exit
	fi
}

# function portcheck
# test a port to see if it is open
function portcheck
{
	for ((counter=$startport; counter <= $stopport; counter++))
	do
		if timeout 2 bash -c "echo > /dev/tcp/$host/$counter"
		then
			echo "Port $counter open"
		else
			echo "Port $counter closed"
		fi
#		(echo >/dev/tcp/$host/$counter) > /dev/null 2>%1 && echo "$counter open"
	done
}

# run our functions
pingcheck
portcheck
