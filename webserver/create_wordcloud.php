<?php

print("Making wordcloud, please wait....<BR>");
# shell_exec("python3 -V 2>&1");
exec("python3 /var/www/html/create_wordcloud.py  2>&1", $output, $return );

// Return will return non-zero upon an error
if (!$return) {
    print("Wordcloud created successfully <BR>");
} else {
    print("Wordcloud not created <BR>");
    print("Output : ");
    print_r($output);
    print("<BR>");
    print("Errorcode: ");
    print($return + "<BR>");
}

?>
<img src="willywordcloud.png">
<br>

<a href="willy_wiki.html">Terug naar Willy Wiki</a>

