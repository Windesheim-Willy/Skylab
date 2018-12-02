<!DOCTYPE html>
<?php
// make SSH connection
print("Making SSH connection <br>");
// use correct host when in production
$connection = ssh2_connect('10.10.1.34',22);

include("secret_info.php");
$user = SSH_USERNAME;
$pass = SSH_PASSWORD;

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
// real locations when connection is made, un-remark next line for production
// $remote_questions_file = "/opt/willy/components/social_interaction/src/interactions/assets/survey.csv";
$local_questions_file = "/home/willy/survey/survey.csv";

// test locations, ** remove next line for production **
$remote_questions_file = "/home/willy/survey/survey.csv";

print("Copying file " . $local_questions_file . " to " . $remote_questions_file . "<br>");

if (ssh2_scp_send($connection, $local_questions_file, $remote_questions_file, 0644)) {
    print("File copy successful!<br><br>");
} else {
    print("<br>File copy failed...<br><br>");
}

ssh2_exec($connection,'exit');

?>

<a href="survey.html">Terug naar enquete pagina</a>
