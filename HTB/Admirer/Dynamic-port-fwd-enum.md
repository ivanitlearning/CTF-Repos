# Enumerating via SSH dynamic port forwarding

We can login via SSH but it closes immediately without giving a shell.

```text
root@kali:~/CTF/HTB/Admirer# ssh ftpuser@10.10.10.187
ftpuser@10.10.10.187's password:
Linux admirer 4.9.0-12-amd64 x86_64 GNU/Linux

The programs included with the Devuan GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Devuan GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Connection to 10.10.10.187 closed.
```

This is true even when we try the standard trick to allocate pseudo-TTY, run Bash upon login.

```text
root@kali:~/CTF/HTB/Admirer# ssh ftpuser@10.10.10.187 -t "bash --noprofile --norc"
ftpuser@10.10.10.187's password:
Connection to 10.10.10.187 closed.

root@kali:~/CTF/HTB/Admirer# ssh ftpuser@10.10.10.187 -t "sh --noprofile --norc"
ftpuser@10.10.10.187's password:
Connection to 10.10.10.187 closed.

root@kali:~/CTF/HTB/Admirer# ssh -T ftpuser@10.10.10.187
ftpuser@10.10.10.187's password:
Linux admirer 4.9.0-12-amd64 x86_64 GNU/Linux

The programs included with the Devuan GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Devuan GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
```

But we can still use this to establish an SSH tunnel with which to enumerate ports the box is listening on localhost. First we set up the Proxychains proxy server on localhost:22222

```text
root@kali:~/CTF/HTB/Admirer# tail /etc/proxychains.conf
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4         127.0.0.1 9050
#http   127.0.0.1 8080
socks5  127.0.0.1 22222
```

Then configure SSH dynamic port forwarding

```text
root@kali:~/CTF/HTB/Admirer# ssh -D 22222 -f -N ftpuser@10.10.10.187
ftpuser@10.10.10.187's password:

root@kali:~/CTF/HTB/Admirer# netstat -ant | grep 22222
tcp        0      0 127.0.0.1:22222         0.0.0.0:*               LISTEN
tcp6       0      0 ::1:22222               :::*                    LISTEN
```

Now we can do an nmap scan to check for open ports, remember to specify -sT because the default half-TCP scans don't work over proxychains.

```text
root@kali:~/CTF/HTB/Admirer# proxychains nmap -Pn -n -sT -p- 127.0.0.1
ProxyChains-3.1 (http://proxychains.sf.net)
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-28 00:34 +08
Nmap scan report for 127.0.0.1
Host is up (0.0067s latency).
Not shown: 65529 closed ports
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
80/tcp    open  http
3306/tcp  open  mysql
36064/tcp open  unknown
43196/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 406.68 seconds
```

Note that on the terminal you did the dynamic port forwarding you'll see a lot of this error message. It's fine this error is simply telling us the scanned port isn't open.

```text
channel 2: open failed: connect failed: Connection refused
```

When done we do a service scan to identify running services.

```text
root@kali:~/CTF/HTB/Admirer# proxychains nmap -Pn -n -sTV -p21,22,80,3306,36064,43196 127.0.0.1
ProxyChains-3.1 (http://proxychains.sf.net)
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-28 00:46 +08
Nmap scan report for 127.0.0.1
Host is up (0.017s latency).

PORT      STATE  SERVICE VERSION
21/tcp    open   ftp     vsftpd 3.0.3
22/tcp    open   ssh     OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)
80/tcp    open   http    Apache httpd 2.4.25 ((Debian))
3306/tcp  open   mysql   MySQL 5.5.5-10.1.44-MariaDB-0+deb9u1
36064/tcp closed unknown
43196/tcp closed unknown
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.25 seconds
```

Note the higher level ports aren't actually open. Sometimes you'll get false positives with nmap.

## Enumerating remote MySQL

Now we can try to enumerate the MySQL service. searchsploit returned these

```text
root@kali:~/CTF/HTB/Admirer# searchsploit mysql 5.5.5
----------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                   |  Path
----------------------------------------------------------------------------------------------------------------- ---------------------------------
MySQL / MariaDB / PerconaDB 5.5.51/5.6.32/5.7.14 - Code Execution / Privilege Escalation                         | linux/local/40360.txt
MySQL < 5.6.35 / < 5.7.17 - Integer Overflow                                                                     | multiple/dos/41954.py
----------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

I checked out [the exploit](https://www.exploit-db.com/exploits/40360), which seems to require creds, as per [this reddit thread](https://www.reddit.com/r/netsec/comments/52dgxh/mysql_remote_root_code_execution_privilege/)

> Doesn't this exploit require you have valid credentials in order to connect to the database itself?
>
> > The PoC exploit does - the vulnerability doesn't per se (SQL injection, phpmyadmin, etc)

Other implementations of this exploit (going by CVE) on Github such as [this](https://github.com/boompig/cve-2016-6662/blob/master/0ldSQL_MySQL_RCE_exploit.py) and [this](https://github.com/Ashrafdev/MySQL-Remote-Root-Code-Execution/blob/master/rce_mysql.py) also require that creds be specified. The alternative is that we find a Web application that has access to the SQL server and exploit it via SQLi. But we don't have that here.