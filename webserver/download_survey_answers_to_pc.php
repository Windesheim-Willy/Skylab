<?php
$survey_filename="/home/willy/survey/survey_answers.csv";
$dl_name = "survey_answers.csv";
header("Content-disposition: attachment;name=$dl_name; filename=$survey_filename");
readfile($survey_filename);
?>
