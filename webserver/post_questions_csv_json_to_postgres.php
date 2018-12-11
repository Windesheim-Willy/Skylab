<!DOCTYPE html>
<?php
// Begin define variables about the table ----------------------------------------------------
$json_file = "/home/willy/survey/survey.json";
$jason_table_name = "survey_jason";
$table_name = "survey";
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
// read json file in to an array
$lines = file($json_file);
$t_name = substr($lines[1], 11);
$t_description= substr($lines[2], 18);
$t_author = substr($lines[3], 13);

$name = substr($t_name, 0, strlen($t_name) - 4);
$description = substr($t_description, 0 ,strlen($t_description) - 4);
$author = substr($t_author, 0, strlen($t_author) - 3);

$to_do = "INSERT INTO " . $jason_table_name . " (name,description,author) VALUES ('" . $name . "','" . $description . "','" . $author . "')";
// print($to_do) . "<br>";
$pdo = new PDO($db);
$stmt = $pdo->prepare($to_do);
$stmt->execute();

$row = 1;
if (($handle = fopen("/home/willy/survey/survey.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        if ($row == 1) {
            $row++;
        } else {

            $num = count($data);
//            print("<br>Vraag:" . ($row - 1). "<br>");
            // create needed SQL statement
            $to_do = "INSERT INTO " . $table_name . " (id,question,answer_1,answer_2,answer_3,answer_4,name) VALUES ('" . $data[0] . "','" . $data[1] . "','" . $data[2] . "','" . $data[3] . "','" . $data[4] . "','" . $data[5] . "','" . $name .  "')";
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


