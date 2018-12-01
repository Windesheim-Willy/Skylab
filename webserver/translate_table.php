<?php
?>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link href="stijl.css" rel="stylesheet">
    <?php
    print("<title>" . $page_title . "</title>");
    print($page_title);
    // Variables about the connection to the database, username and password defined in secret_info.php
    include("secret_info.php");
    $db = "Willy";
    $user = USERNAME;
    $pass = PASSWORD;
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
    // do select to decide column names
    $pdo = new PDO($db);
    $to_do = "select column_name from information_schema.columns where table_name = '" . $table_name . "'";
    print("<br>" . $to_do . "<br>");
    $stmt = $pdo->prepare($to_do);
    $stmt->execute();
    $i = 0;
    while ($row = $stmt->fetch()) {
        $i = $i + 1;
        ${'c' . $i . '_name'} = $row["column_name"];
    }
    $number_of_columns = $i;
    // do select to decide max number of records and number of pages
    $pdo = new PDO($db);
    $stmt = $pdo->prepare("SELECT * FROM " . $table_name);
    $stmt->execute();
    $number_of_records = $stmt->rowCount();
    $number_of_pages = ceil($number_of_records / @$number_of_records_per_page);
    // start at first page and if $_GET['page'] is defined, use that as the current_page
    $current_page = 1;
    if (isset($_GET['page'])) {
        $current_page = $_GET['page'];
    }
    // print the link to access each page
    $self = $_SERVER['PHP_SELF'];
    $nav = '';
    for ($page = 1; $page <= $maxPage; $page++) {
        if ($page == $current_page) {
            $nav .= " $page "; // no need to create a link to current page
        } else {
            $nav .= " <a href=\"$self?page=$page\">$page</a> ";
        }
    }
    // calculate offset
    $start_record = (($current_page - 1) * $number_of_records_per_page);
    $end_record = $number_of_records_per_page;
    // create needed SQL statement
    $to_do = "SELECT * FROM " . $table_name . " LIMIT " . $end_record . " OFFSET " . $start_record;
    // do select on PostgreSQL for neede page
    $pdo = new PDO($db);
    $stmt = $pdo->prepare($to_do);
    $stmt->execute();
    // print table
    print("<table>");
    // overflow gives horizental scroll when needed
    print("<table style = \"overflow-x:auto;\">");
    // create header of table with column names
    print("<tr>");
    for ($i = 1; $i <= $number_of_columns; $i++) {
        print("<td>" . ${'c' . $i . '_name'} . "</td>");
    }

    // fetch needed records
    while ($row = $stmt->fetch()) {
        print("<tr>");
        for ($i = 1; $i <= $number_of_columns; $i++) {
            ${'c' . $i} = $row[${'c' . $i . '_name'}];
            print("<td>" . ${'c' . $i} . "</td>");
        }
        print("</tr>");
    }
    print("</table>");
    // print the link to access each page
    $self = $_SERVER['PHP_SELF'];
    // create navigation links Vorige and Eerste pagina except for first page
    if ($current_page > 1) {
        $page = $current_page - 1;
        $prev = " <a href=\"$self?page=$page\">[Vorige]</a> ";

        $first = " <a href=\"$self?page=1\">[Eerste pagina]</a> ";
    } else {
        $prev = '&nbsp;'; // we're on page one, don't print previous link
        $first = '&nbsp;'; // nor the first page link
    }
    // create navigation links Volgende and Laatste pagina except for last page
    if ($current_page < $number_of_pages) {
        $page = $current_page + 1;
        $next = " <a href=\"$self?page=$page\">[Volgende]</a> ";

        $last = " <a href=\"$self?page=$number_of_pages\">[Laatste pagina]</a> ";
    } else {
        $next = '&nbsp;'; // we're on the last page, don't print next link
        $last = '&nbsp;'; // nor the last page link
    }

    // print the navigation links and information bar
    print($first . $prev . "Totaal aantal records: " . $number_of_records . " Pagina: " . $current_page . " van " . $number_of_pages . " Zichtbare records zijn: " . $start_record . " tot " . (($start_record + $end_record) - 1) . $next . $last . "<br>");
    // close database
    $pdo = NULL;
    ?>

    <a href="index.html">Terug naar hoofdpagina</a>
    </body>
</html>

