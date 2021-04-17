# Enumerating MySQL

Checking out the webroot dir, we see a file db.php which contains MySQL creds.

```text
reader@book:/var/www/html$ ls
admin      collections.php  db.php  download.php  home.php  index.php   profile.php  settings.php
books.php  contact.php      docs    feedback.php  images    logout.php  search.php
reader@book:/var/www/html$ cat db.php
<?php
$conn = mysqli_connect("localhost","book_admin","I_Hate_Book_Reading","book");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
?>
```

We use it to login to the DB.

```text
reader@book:/var/www/html$ mysql -u book_admin -pI_Hate_Book_Reading
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 225
Server version: 5.7.29-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| book               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use book;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_book |
+----------------+
| collections    |
| feedback       |
| messages       |
| users          |
+----------------+
4 rows in set (0.00 sec)

mysql> select * from users;
+----------+-------------------+-------------------+
| name     | email             | password          |
+----------+-------------------+-------------------+
| admin    | admin@book.htb    | Sup3r_S3cur3_P455 |
| peter    | hi@hello.com      | password          |
| attacker | attacker@kali.com | Password1         |
+----------+-------------------+-------------------+
3 rows in set (0.00 sec)
mysql> select * from messages;
+---------+---------+
| email   | message |
+---------+---------+
| a@b.com |         |
+---------+---------+
1 row in set (0.00 sec)

mysql> select * from feedback;
+----------------------+-------+----------+
| email                | title | feedback |
+----------------------+-------+----------+
| admin@book.htb       | Waldo | Waldo    |
+----------------------+-------+----------+
1 row in set (0.00 sec)

mysql> select * from collections;
+--------------------+--------+------+---------------------------------+
| name               | author | link | email                           |
+--------------------+--------+------+---------------------------------+
| Corpse Flower      | -      | 1    | egotisticalSW_was_here@book.htb |
| Queen of the Night | -      | 2    | egotisticalSW_was_here@book.htb |
| Chocolate cosmos   | -      | 3    | egotisticalSW_was_here@book.htb |
| Lady's-Slipper     | -      | 4    | egotisticalSW_was_here@book.htb |
+--------------------+--------+------+---------------------------------+
4 rows in set (0.00 sec)
```

which gives us a password **Sup3r_S3cur3_P455** (the other entries are by me except for the emails). But the password doesn't work anywhere and there are no other users with a shell.