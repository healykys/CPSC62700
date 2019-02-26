CPSC 62700 Project 4: Powershell
Kyle Healy
2/20/2019

NAME
    powerpwn.ps1 - Powershell program to create a back door and execute programs on start up and a specified time.

USAGE
    .\powerpwn.ps1

DESCRIPTION:
    This is a script to be run remotely after taking over a Windows-based machine. Assumption is that one already has access to Administrator, so this script can perform the next steps automatically. First, it will create a backdoor account by adding a new user "poweruser" under the "Admins" group and add that Admins to Administrators, giving poweruser full Administrator access. Next, it will download two programs and save them to a C:\temp folder with non-suspicious names. Third, it'll add one of the programs to start up automatically by changing the Host Key Local Machine registry. This tasks simulates adding a key-logger to a machine and logging every users keys. Finally, it'll schedule a task to run a different program, nightly at 2am. This last task simulates exfiltrae key logs from every user to the hacker. 

OPTIONS
    N/A

INPUTS
    N/A

KNOWN BUGS AND LIMITATIONS
    Assumption that the poweruser, and Admins group do not exist. Will throw an error if they already exist.

ADDITIONAL NOTES
    Execution Policy on target machine should be set to "RemoteSigned" instead of "Restricted"
    Had a good amount of trouble getting any internet sites to show up on the Windows Server from 2008. Everything was locked down. Files had to be copy and pasted over through a website. They all worked on the Windows Server machine, but were copied over after.