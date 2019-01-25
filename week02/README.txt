CS 62700 Project 1: Bash Port Scanner
Kyle Healy
1/24/2019

NAME
	portscanner.sh - scans specified ports on a given host name

USAGE

DESCRIPTION
	portscanner.sh is a bash program that reads in a hostname and a starting and stopping port. The program attempts to access the hostname, verifying it is up and operational. If the hostname is up, it scans the ports in between the starting and stopping port. 

OPTIONS
	-t 	Change the duration of the wait time before cancelling the ping request.

INPUT FILE FORMAT
	Input files should contain multiples of 3 lines. The format should follow the format below.
	Line 1: Hostname - Either a string with the name (www.lewisu.com) or a 32 bit number (192:168:1:1)
	Line 2: Starting Port - The number to start the port scanning at.
	Line 3: Stopping Port - The number to stop the port scanning at.
	

KNOWN BUGS AND LIMITATIONS
	

ADDITIONAL NOTES
