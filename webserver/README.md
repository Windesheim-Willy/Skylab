# Webserver files

These files are used in the webserver from Willy. They all make reports of the stored topics by the Fetcher.

The php script **make_web_page.php** is the central script.

For the username and password to connect to the PostgreSQL database the file **secret_info.php** is used. The content of this file is:
```php
<?php
define('PASSWORD', 'the password of the user');
define('USERNAME', 'the name of the user');
?>
```
