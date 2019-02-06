CS 62700 Project 2: Python SSH Brute Force
Kyle Healy
2/6/2019

NAME
	sshbrute.py - program to brute force an ssh terminal with a given user and host

USAGE
	./sshbrute.py <-f filename | -g> <host> <username>

DESCRIPTION
	sshbrute.py is a python program that attempts to gain access to a remote host over ssh. The program takes in multiple command line arguments as a set up. Given -f FILENAME the program will attempt to gain access using all the passwords in the given file (1 per line). Given the -g argument, the program will generate all combinations of 3 lower case character strings and use those to attempt to login over ssh. 

OPTIONS
	-f [FILENAME] 	Input file containing a common password on each line.
	-g		Flag to generate every combination of 3 lower case characters.

INPUT FILE FORMAT
	Input file should contain a single password per line, with as many lines as there are passwords to be tested.

KNOWN BUGS AND LIMITATIONS

ADDITIONAL NOTES

Account	Password	Method Discovered
usera	abc123		File
userb	baseball	File
userc	adf		Generated
userd	letmein		File
usere	cxv		Generated
