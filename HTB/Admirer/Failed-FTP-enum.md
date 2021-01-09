# FTP enumeration

searchsploit returned no results for vsftpd 3.0.3

```text
root@kali:~/CTF/HTB/Admirer# searchsploit vsftpd
------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                    |  Path
------------------------------------------------------------------------------------------------------------------ ---------------------------------
vsftpd 2.0.5 - 'CWD' (Authenticated) Remote Memory Consumption                                                    | linux/dos/5814.pl
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (1)                                                    | windows/dos/31818.sh
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (2)                                                    | windows/dos/31819.pl
vsftpd 2.3.2 - Denial of Service                                                                                  | linux/dos/16270.c
vsftpd 2.3.4 - Backdoor Command Execution (Metasploit)                                                            | unix/remote/17491.rb
------------------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results
```

nmap scripts found nothing with the FTP service

```text
root@kali:~/CTF/HTB/Admirer# nmap -Pn -n -sV -p21 --script=ftp* 10.10.10.187 -e tun0
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-27 19:37 +08
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] passwords: Time limit 10m00s exceeded.
Nmap scan report for 10.10.10.187
Host is up (0.0061s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-brute:
|   Accounts: No valid accounts found
|_  Statistics: Performed 10127 guesses in 601 seconds, average tps: 16.7
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 601.06 seconds
```

Anonymous FTP logins don't work

```text
root@kali:~/CTF/HTB/Admirer# ftp -p 10.10.10.187
Connected to 10.10.10.187.
220 (vsFTPd 3.0.3)
Name (10.10.10.187:root): anonymous
530 Permission denied.
Login failed.
ftp> quit
221 Goodbye.
root@kali:~/CTF/HTB/Admirer# ftp -p 10.10.10.187
Connected to 10.10.10.187.
220 (vsFTPd 3.0.3)
Name (10.10.10.187:root): waldo
530 Permission denied.
Login failed.
ftp> quit
221 Goodbye.
```

