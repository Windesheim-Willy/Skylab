<!DOCTYPE html>
<?php
// Begin define variables about the table ----------------------------------------------------
$table_name = "survey_answers";
// End define variables about the table ----------------------------------------------------
include("secret_info.php");
include("config.php");
$db = "Willy";
$user = DB_USERNAME;
$pass = DB_PASSWORD;
$db = "pgsql:host=10.10.1.35;dbname=$db;user=$user;password=$pass; port=5432";
// create a PostgreSQL database connection
try {
    $pdo = new PDO($db);
    // display a message if connected to the PostgreSQL successfully
    if ($pdo) {
        // Remove remark on next line to see result on screen for succesfull connection
        // echo "Connected to the <strong>$db</strong> database successfully!";
    }
} catch (PDOException $e) {
    // report error message
    echo $e->getMessage();
}


$row = 1;
if (($handle = fopen("/home/willy/survey/survey_answers.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if ($row == 1) {
            $row++;
        } else {

            $num = count($data);
//            print("<br>Vraag:" . ($row - 1). "<br>");
            // create needed SQL statement
            $to_do = "INSERT INTO " . $table_name . " (survey, timestamp, question, answer_raw,answer) VALUES ('" . $data[0] . "','" . $data[1] . "','" . $data[2] . "','" . $data[3] . "','" . $data[4] . "')";
//            print($to_do) . "<br>";
            $pdo = new PDO($db);
            $stmt = $pdo->prepare($to_do);
            $stmt->execute();
            $row++;
        }
    }
    fclose($handle);
}
print("Data in Postgres geimporteerd. <br>");
?>
<br>
<br>
<a href="survey.html">Terug naar enquete pagina</a>


