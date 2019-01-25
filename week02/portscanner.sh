#!/bin/bash

# Basic bash port scanner

# display a usage message if incorrect number of arguments
function usage
{
	echo "Usage: ./portscanner.sh [-t timeout] [<host> <startport> <stopport>]"
	exit
}

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
		if timeout $timeoutVal bash -c "echo > /dev/tcp/$host/$counter"
		then
			echo "Port $counter open"
		else
			echo "Port $counter closed"
		fi
#		(echo >/dev/tcp/$host/$counter) > /dev/null 2>%1 && echo "$counter open"
	done
}


function interactiveMode
{
	while [[ 1 == 1 ]]
	do
		echo "Enter hostname:"
		read host
		if [ -z "$host" ]
		then #empty string host. Exit
			exit
		fi
		echo "Enter starting port:"
		read startport
		echo "Enter stopping port:"
		read stopport
		pingcheck
		portcheck
	done
}

# populate our variables from the arguments.
# Check if optional -t exists
totalArgs=$#
if [[ $totalArgs == 5 ]] && [[ "$1" == "-t" ]]
then
	timeoutVal=$2
	host=$3
	startport=$4
	stopport=$5
	pingcheck
	portcheck
elif [[ $totalArgs == 3 ]]
then
	timeoutVal=2
	host=$1
	startport=$2
	stopport=$3
	pingcheck
	portcheck
elif [[ $totalArgs == 2 ]] && [[ "$1" == "-t" ]]
then
	timeoutVal=$2
	#Interactive/Batch Mode
	interactiveMode
elif [[ $totalArgs == 0 ]]
then
	timeoutVal=2
	#Interactive/Batch Mode
	interactiveMode
else
	usage
fi


