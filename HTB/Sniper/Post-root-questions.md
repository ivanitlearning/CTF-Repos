# Post-root questions

### Why doesn't the PHP filter php:// work for LFI?

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

The `stream_wrapper_unregister("php")` is [what disables](https://security.stackexchange.com/questions/193247/disable-php-filter-globally-or-per-php-file) it. There are [other PHP wrappers](https://www.php.net/manual/en/wrappers.php) and more importantly the standard [file://](https://www.php.net/manual/en/wrappers.file.php) wrapper which is invoked when we try to do LFI without specifying a wrapper type is not disabled. We also see from the code above, that if either "C:" or ".." is included, error.html is loaded and the PHP session dies. This explains why relative path file inclusion fails but absolute paths work.

### Why didn't HTTP RFI work but SMB RFI did?

In **C:\Program Files (x86)\PHP\v7.3\php.ini** we see:

```ini
;;;;;;;;;;;;;;;;;;
; Fopen wrappers ;
;;;;;;;;;;;;;;;;;;

; Whether to allow the treatment of URLs (like http:// or ftp://) as files.
; http://php.net/allow-url-fopen
allow_url_fopen = On

; Whether to allow include/require to open URLs (like http:// or ftp://) as files.
; http://php.net/allow-url-include
allow_url_include = Off
```

This means URLs can't be included. Additionally SMB file inclusion is [enabled by default](https://stackoverflow.com/questions/5070545/php-read-file-contents-of-network-share-file/5070774#5070774). One such example is stated [in the documentation](https://www.php.net/manual/en/wrappers.file.php).

### How exactly does the PHP session file LFI work?

First understand how a PHP [session works](https://stackoverflow.com/questions/1535697/how-do-php-sessions-work-not-how-are-they-used/1535712#1535712). The general idea behind it is that Web servers use cookies to distinguish between different users and each cookie represents a PHP session ID. What kind of data is stored in the PHP session file? In this case, the code for login.php shows

```php
PS C:\inetpub\wwwroot\user> type login.php
type login.php
<!DOCTYPE html>
<html>
<meta charset="utf-8">
<title>Login</title>
</head>
<body>
<?php
require('db.php');
session_start();
// If form submitted, insert values into the database.
if (isset($_POST['username'])){
        // removes backslashes
        $username = stripslashes($_REQUEST['username']);
        //escapes special characters in a string
        $username = mysqli_real_escape_string($con,$username);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con,$password);
        //Checking is user existing in the database or not
        $query = "SELECT * FROM `users` WHERE username='$username'
and password='".md5($password)."'";
        $result = mysqli_query($con,$query) or die(mysql_error());
        $rows = mysqli_num_rows($result);
        if($rows==1){
            $_SESSION['username'] = $username;
            // Redirect user to index.php
            header("Location: index.php");
         }else{
        echo "<div class='form'>
<h3>Username/password is incorrect.</h3>
<br/>Click here to <a href='login.php'>Login</a></div>";
```

Pay attention to the line `$_SESSION['username'] = $username;`. The stackoverflow answer is that data in session file is serialized but it doesn't appear to be so here. With a SYSTEM shell, I created an account with user/pass as the username/password and examined the contents of file

```text
PS C:\Windows\Temp> get-Content sess_2ui1a55ljgtcfdj1t9d8cj7m2f
get-Content sess_2ui1a55ljgtcfdj1t9d8cj7m2f
username|s:4:"user";
```

It's stored in plaintext instead of serialised data, allowing for code upload and execution via LFI. Since we don't know in advance what the session file would contain we should check to see if it allows code injection there. For a real-life example of how this was used to get RCE, [read this](https://www.rcesecurity.com/2017/08/from-lfi-to-rce-via-php-sessions/). Here's [a list](https://nets.ec/File_Inclusion) of possible PHP session file locations.

### How does registration.php filter out the bad characters for usernames?

```php
PS C:\inetpub\wwwroot\user> type registration.php
type registration.php
<!DOCTYPE html>
<html>
<meta charset="utf-8">

</head>
<body>
<?php
require('db.php');
// If form submitted, insert values into the database.
if (isset($_REQUEST['username'])){
        // removes backslashes
        $username = stripslashes($_REQUEST['username']);
        $username = str_replace('-', '', $username);
        $username = str_replace('$', '', $username);
        $username = str_replace('[', '', $username);
        $username = str_replace('(', '', $username);
        $username = str_replace('_', '', $username);
        $username = str_replace('.', '', $username);
        $username = str_replace(';', '', $username);
        $username = str_replace('&', '', $username);
        $username = str_replace('"', '', $username);
        //escapes special characters in a string
        $username = mysqli_real_escape_string($con,$username);
        $email = stripslashes($_REQUEST['email']);
        $email = mysqli_real_escape_string($con,$email);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con,$password);
        $trn_date = date("Y-m-d H:i:s");
        $query = "INSERT into `users` (username, password, email, trn_date)
VALUES ('$username', '".md5($password)."', '$email', '$trn_date')";
        $result = mysqli_query($con,$query);
        if($result){

sleep(1);
header("Location: login.php");
   }
    }else{
?>
```

The code pretty much explains it.