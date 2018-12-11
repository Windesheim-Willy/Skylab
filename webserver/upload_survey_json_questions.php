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

print("<br>");

print("Logging in <br>");

// login to remote server
if (ssh2_auth_password($connection, $user, $pass)) {
    print("Authentication Successful<br>");
} else {
    print("Authentication Failed...<br>");
}
print("<br>");

// make SFTP connection
print("Making SFTP connection <br>");
$sftp = ssh2_sftp($connection);
print("SFTP connection successful <br>");
print("<br>");

// copy file
// real locations when connection is made, un-remark next line for production
// $remote_questions_file = "/opt/willy/components/social_interaction/src/interactions/assets/survey.csv";
$local_questions_file1 = "/home/willy/survey/survey.json";
$local_questions_file2 = "/home/willy/survey/survey.csv";

// test locations, ** remove next line for production **
$remote_questions_file1 = "/opt/willy/components/social_interaction/src/interactions/assets/survey.json";
$remote_questions_file2 = "/opt/willy/components/social_interaction/src/interactions/assets/survey.csv";

print("<br>");

print("Copying file " . $local_questions_file1 . " to " . $remote_questions_file1 . "<br>");

if (ssh2_scp_send($connection, $local_questions_file1, $remote_questions_file1, 0644)) {
    print("JSON file copy successful!<br><br>");
} else {
    print("<br>JSON File copy failed...<br><br>");
}

print("<br>");

print("Copying file " . $local_questions_file2 . " to " . $remote_questions_file2 . "<br>");

if (ssh2_scp_send($connection, $local_questions_file2, $remote_questions_file2, 0644)) {
    print("CSV file copy successful!<br><br>");
} else {
    print("<br>CSV file copy failed...<br><br>");
}

ssh2_exec($connection,'exit');

?>

<a href="survey.html">Terug naar enquete pagina</a>
