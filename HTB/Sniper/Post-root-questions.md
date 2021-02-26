# Post-root questions

Why doesn't the PHP filter php:// work for LFI?

Here's the PHP code of the page vulnerable to LFI

```php
PS C:\inetpub\wwwroot\blog> Get-Content index.php
Get-Content index.php
<html>
<body>
<?php include 'header.html'; ?>
<?php
stream_wrapper_unregister("php");
stream_wrapper_unregister("data");
$lang = "blog-en.php";
if(!ISSET($_GET['lang'])) {
        include $lang;
}
else {
        $lang = $_GET['lang'];

        if(stripos($lang, "..") === false && stripos($lang, "C:") === false) { // Hardened 8)
                if(!(include $lang)) {
                        include "error.html";
                }
        }
        else {
                include "error.html";
                die();
        }


}

?>
</body>
</html>
```

The `stream_wrapper_unregister("php")` is [what disables](https://security.stackexchange.com/questions/193247/disable-php-filter-globally-or-per-php-file) it. There are [other PHP wrappers](https://www.php.net/manual/en/wrappers.php) and more importantly the standard [file://](https://www.php.net/manual/en/wrappers.file.php) wrapper which is invoked when we try to do LFI without specifying a wrapper type is not disabled.