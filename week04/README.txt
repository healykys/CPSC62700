CS 62700 Project 3: Python BotNet
Kyle Healy
2/13/2019

NAME
	botinstall.py - program to install a backdoor on a zombie computer and add that computer to a BotNet.
    	netshell.py - A python server that runs in the backgroun on a zombie computer. The program runs as a server, accepts connections and runs commands locally and returns the output.
    	candc.py - comand and control python program that opens up client sockets to connect to the Zombie computers and run commands over those sockets and return the outputs back to the Command and Control PC.

USAGE
	All three python files and the compromised_hosts.txt should be in the same folder where the commands will be run from.
	./botinstall.py
    	./candc.py

DESCRIPTION
	This is a set of three programs that read in a file (compromised_hosts.txt) with with hosts, users, and passwords to create a BotNet and uploads a netshell script to those Zombie computers. 

OPTIONS
	N/A

INPUT FILE FORMAT
	The input file should be the host, username, and password separated by a space each. The file can have as many of these rows as it likes, but the format should remain <host> <username> <password> than immediately starting a new line.

ORDER TO RUN FILES
	./botinstall.py
	.candc.py

KNOWN BUGS AND LIMITATIONS

ADDITIONAL NOTES


