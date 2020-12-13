# Enumerating FTP

First try the NSE scripts

```shell
root@kali:~/CTF/HTB/Remote# nmap -Pn -n -sV -p21 --script=ftp* 10.10.10.180 -e tun0
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-04 00:32 +08
NSE: [ftp-bounce] PORT response: 501 Server cannot accept argument.
Nmap scan report for 10.10.10.180
Host is up (0.013s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-brute:
|   Accounts: No valid accounts found
|_  Statistics: Performed 50009 guesses in 100 seconds, average tps: 572.3
| ftp-syst:
|_  SYST: Windows_NT
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.51 seconds
```

Nothing. Try anonymous login since it's allowed.

```shell
root@kali:~/CTF/HTB/Remote# ftp -p 10.10.10.180
Connected to 10.10.10.180.
220 Microsoft FTP Service
Name (10.10.10.180:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
227 Entering Passive Mode (10,10,10,180,194,25).
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> pwd
257 "/" is current directory.
ftp> cd ../../
250 CWD command successful.
ftp> ls
227 Entering Passive Mode (10,10,10,180,194,26).
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> pwd
257 "/" is current directory.
```

So we can't list anything or do directory traversal. Nothing here.