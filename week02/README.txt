CS 62700 Project 1: Bash Port Scanner
Kyle Healy
1/26/2019

NAME
	portscanner.sh - scans specified ports on a given host name

USAGE
	./portscanner.sh [-t timeout] [hostname startport stopport]

DESCRIPTION
	portscanner.sh is a bash program that reads in a hostname and a starting and stopping port. The program attempts to access the hostname, verifying it is up and operational. If the hostname is up, it scans the ports in between the starting and stopping port. If the starting port is greater than the stopping port, the scan loops around. Ex. all ports between [startport 255] and [0 stopport] will be scanned.

OPTIONS
	-t 	Change the duration of the wait time before cancelling the ping request.

INPUT FILE FORMAT
	Input files should contain multiples of 3 lines. The format should follow the format below.
	Line 1: Hostname - Either a string with the name (www.lewisu.com) or a 32 bit number (192:168:1:127)
	Line 2: Starting Port - The number to start the port scanning at.
	Line 3: Stopping Port - The number to stop the port scanning at.
	

KNOWN BUGS AND LIMITATIONS
	If a non integer is passed in as the stopport, an error is thrown, but the scanner will continue on to scan from startport through port 255 and port 0.
	If a non integer is passed as the start port, an error is thrown, but the scanner will continue to scan from 0 to 255. 

ADDITIONAL NOTES
	Looping aroung the ports was an addition to the program. The initial program would have broken if start was higher than the stop (Ex. Start 255 and stop 2). 
