<!DOCTYPE html>
<?php
include("config.php");
$host = SI_SURVEY_NODE_IP_ADDRESS;
// make SSH connection
print("Making SSH connection <br>");
// use correct host when in production
$connection = ssh2_connect($host,22);

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
// real locations when connection is made, ** un-remark next line for production **
// $remote_answers_file = "/opt/willy/components/social_interaction/src/interactions/assets/survey_answers.csv";
// $local_answers_file  = "/var/www/html/survey/survey_answers.csv";
$local_answers_file  = "/home/willy/survey/survey_answers.csv";

// test locations, ** remove next line for production **
$remote_answers_file = "/opt/willy/components/social_interaction/src/interactions/assets/survey_answers.csv";

print("Copying file " . $remote_answers_file . " to " . $local_answers_file . "<br>");

if (ssh2_scp_recv($connection, $remote_answers_file, $local_answers_file)) {
    print("File copy successful!<br><br>");
} else {
    print("<br>File copy failed...<br><br>");
}

ssh2_exec($connection,'exit');
?>

<a href="survey.html">Terug naar enquete pagina</a>
