<?php
// configuration
$url = 'edit_cloudset.php';
$file = '/var/www/html/cloudset.txt';

// check if form has been submitted
if (isset($_POST['text'])) {
    // save the text contents
    file_put_contents($file, $_POST['text']);

    header('Location: http://10.10.1.45/willy_wiki.html', true, 301);
    exit();
} else {

// read the textfile
    $text = file_get_contents($file);
    ?>
    <!-- HTML form -->
    <form action="" method="post">
        <textarea name="text" rows="35" cols="100"><?php echo htmlspecialchars($text) ?></textarea>
        <input type="submit" value="Opslaan"/>
    </form>

    <?php
}
?>