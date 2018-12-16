<!DOCTYPE html>
<?php
include("config.php");
$host = P_NODE_IP_ADDRESS;
// make SSH connection
print("Making SSH connection <br>");
// use correct host when in production
$connection = ssh2_connect($host,22);

include("secret_info.php");
$user = SSH_P_USERNAME;
$pass = SSH_P_PASSWORD;

print("Logging in <br>");

// login to remote server
if (ssh2_auth_password($connection, $user, $pass)) {
    print("Authentication Successful!<br>");
} else {
    print("Authentication Failed...<br>");
}

// make SFTP connection
print("Making SFTP connection <br>");
$sftp = ssh2_sftp($connection);
print("SFTP connection successful! <br>");

// copy file
// real locations when connection is made, ** un-remark next line for production **
// $remote_answers_file = "/opt/willy/components/social_interaction/src/interactions/assets/survey_answers.csv";
// $local_answers_file  = "/var/www/html/survey/survey_answers.csv";
$local_picture_file1  = "/var/www/html/navigation_joystick.png";
$local_picture_file2  = "/var/www/html/navigation_geometry.png";
#$local_picture_file1  = "/home/willy/navigation_joystick.png";
#$local_picture_file2  = "/home/willy/navigation_geometry.png";

// test locations, ** remove next line for production **
$remote_picture_file1  = "/home/willy/Willy/navigation_joystick.png";
$remote_picture_file2  = "/home/willy/Willy/navigation_geometry.png";

print("Copying file " . $remote_picture_file1 . " to " . $local_picture_file1 . "<br>");

if (ssh2_scp_recv($connection, $remote_picture_file1, $local_picture_file1)) {
    print("File copy successful!<br><br>");
} else {
    print("<br>File copy failed...<br><br>");
}

print("Copying file " . $remote_picture_file2 . " to " . $local_picture_file2 . "<br>");

if (ssh2_scp_recv($connection, $remote_picture_file2, $local_picture_file2)) {
    print("File copy successful!<br><br>");
} else {
    print("<br>File copy failed...<br><br>");
}

ssh2_exec($connection,'exit');
?>
<img src="navigation_joystick.png">
<br>
<img src="navigation_geometry.png">
<br>
<a href="topics.html">Terug naar topics pagina</a>
