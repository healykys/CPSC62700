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
	This is a set of three programs. 
	The first, botinstall.py, reads in a file (compromised_hosts.txt from the same directory) with with hosts, users, and passwords to create a BotNet and uploads a netshell script to those Zombie computers. botinstall.py assumes that the passwords, users and hosts are accurate to get into an account on a zombie computer. It does contain error handling within the program. Botinstall.py will attempt to access each host in the compromised_hosts.txt file and SFTP the netshell.py file to the host. Next, it will log in over ssh and starts up the netshell.py program in the background to continue to run even when the ssh connection is broken. That open connnection will create the backdoor to the zombie computer
	The second, netshell.py, is the script that runs on the zombie computer to act as a server and control the computer remotely. The script will accept connections over 8081 and execute them on the zombie computer, returning the result back over the same connection.
	The third, candc.py, is the command and control computer to oversee the botnet. The command and control computer connects to the zombie computers over port 8081. After connecting, it sends the same commands to the entire botnet at once. Each zombie computer on the botnet executes that command and returns the result back to the command and control computer. The restuls are printed out to the screen for the botnet conductor to see.

OPTIONS
	N/A

INPUT FILE FORMAT
	The input file should be the host, username, and password separated by a space each. The file can have as many of these rows as it likes, but the format should remain <host> <username> <password> than immediately starting a new line.

ORDER TO RUN FILES
	./botinstall.py
	./candc.py

KNOWN BUGS AND LIMITATIONS
	The response from the zombie computers is a max size of 1024. The program does not loop around if bigger responses are provided.
	The port is not configurable between the botnet and the command and control. Both are hard coded right now.
	Only basic commands can be sent to the botnet right now. Anything interactive (ex. vi) will cause the program to hang.

ADDITIONAL NOTES


