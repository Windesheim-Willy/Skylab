<?php
// $input = "survey.csv";

$row = 1;
if (($handle = fopen("/home/willy/survey/survey.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if ($row == 1){
            $row++;
        }
        else{

        $num = count($data);
        print("<br>Vraag:" . ($row - 1));
        $row++;
        for ($c = 0; $c < $num; $c++) {
            if ($c != 0) {
                if ($c == 1) {
                    print(" " . $data[$c] . "<br>");
                } else {
                    print("() " . $data[$c] . "<br>");
                }
            }
        }
        }
    }
    fclose($handle);
}

?>
<br>
<br>
<a href="survey.html">Terug naar enquete pagina</a>
