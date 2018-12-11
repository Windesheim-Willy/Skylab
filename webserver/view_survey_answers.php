<?php
// $input = "survey.csv";

$row = 1;
if (($handle = fopen("/home/willy/survey/survey_answers.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if ($row == 1){
            $row++;
        }
        else{

            $num = count($data);
            print("<br>Vraag: " . ($row - 1) . "<br>");
            $row++;
            for ($c = 0; $c < $num; $c++) {
                if ($c != 0) {
                    if ($c == 1) {
                        print("() " . substr($data[$c],0,10) . " om " . substr($data[$c],11, 5) . "<br>");
                    } else {
                        print("() " . $data[$c] . "<br>");
                    }
                }
            }
        }
    }
    fclose($handle);
}
else {
    print("File not found ......");
}

?>
<br>
<br>
<a href="survey.html">Terug naar enquete pagina</a>
