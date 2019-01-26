#!/bin/bash

#Kyle Healy
#CPSC 62700 - Penetration Testing
#1/26/2019

# Basic bash port scanner program

# Display a usage message and exit if incorrect number of arguments
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
	done
}

# function portOrder
# Checks that startport is less than stopport. If it's not, wrap search around total number of ports (wraps 255 to 0)
function portOrder
{
	if [ "$startport" -le "$stopport" ]
	then
		portcheck
	else
		tmpstopport=$stopport
		stopport=255
		portcheck
		startport=0
		stopport=$(($tmpstopport))
		portcheck
	fi	
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
		portOrder
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
	portOrder
elif [[ $totalArgs == 3 ]]
then
	timeoutVal=2
	host=$1
	startport=$2
	stopport=$3
	pingcheck
	portOrder
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


