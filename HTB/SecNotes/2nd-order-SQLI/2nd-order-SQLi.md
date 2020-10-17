# SecNotes' 2nd order SQL injection

0xdf explains how it [works here](https://0xdf.gitlab.io/2019/01/19/htb-secnotes.html) and IppSec covers it at the end of [his video](https://www.youtube.com/watch?v=PJXb2pK8K84). Here's my understanding of how it works. These PHP files are all found in **C:\inetpub\wwwroot**

Once you login to the Web app, these lines in **home.php** is run to retrieve the notes.

```php
$sql = "SELECT id, title, note, created_at FROM posts WHERE username = '" . $username . "'";
$res = mysqli_query($link, $sql);
```

Note for $username there is no checking whether $username contains SQL commands which will try to alter the statement. If you inject $username as `' or 1=1;` which you can [try here](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_where_number), everything gets retrieved with the query

```sql
SELECT * FROM Customers WHERE CustomerName = '' OR 1=1;
```

This is in contrast to login.php where we see lines like

```php
$sql = "SELECT username, password FROM users WHERE username = ?";
        
if($stmt = mysqli_prepare($link, $sql)){
```

where the username variable is being prepared undergoes **mysqli_prepare()**. What is **mysqli_prepare()**? This [answer](https://stackoverflow.com/questions/46159964/what-does-mysqli-prepare-really-do-why-should-it-be-called-by-user-and-not-hax) helps to explain it but the gist is

> The point of prepared statements is that the values/arguments/variables for the SQL query are send separated from the actual SQL query to the MySQL server. This way the values/arguments/variables cannot change the SQL query you are trying to send. This prevents SQL injections where the inputs contain values like `"='' OR 1 = 1 --"`.

Remember in SQL injection we are trying to modify the Web app's SQL statements so that it retrieves information it shouldn't be. But if the inputs are strictly treated as variables we can have a username like **' or 1=1;-- -** without it being mistaken as part of an SQL query. For more examples see the procedural-style ones [here](https://www.tutorialspoint.com/php/php_function_mysqli_stmt_execute.htm) and [here](https://www.php.net/manual/en/mysqli-stmt.execute.php).

Ok now let's see where the **$username** in home.php comes from and how it is handled for SQL injection checking. In login.php we see

```php
    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = 'Please enter username.';
    } else{
        $username = trim($_POST["username"]);
    }
```

where [trim() without arguments](https://www.w3schools.com/php/func_string_trim.asp) removes all the newlines and whitespaces and these HTML elements where $username is entered by POST requests

```html
            <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
                <label>Username</label>
                <input type="text" name="username"class="form-control" value="<?php echo $username; ?>">
                <span class="help-block"><?php echo $username_err; ?></span>
            </div>    
```

In login.php once the password is verified, and the input clears the **mysqli_prepare()** statement above, it then sets the SESSION variable for **username**

```php
if(password_verify($password, $hashed_password)){
	/* Password is correct, so start a new session and
	save the username to the session */
	session_start();
	$_SESSION['username'] = $username;      
	header("location: home.php");
}
```

So the upshot is that any input for username like `'or 1=1;-- -` is treated as a username instead of modifying the SQL statements in login.php but since home.php doesn't use mysqli_prepare() it becomes possible to modify the SQL query there to retrieve everything.