# General FTP enumeration



searchsploit on the FTP server did not find any public exploits.

```text
root@kali:~/CTF/HTB/SneakyMailer# searchsploit vsftpd
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                        |  Path
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
vsftpd 2.0.5 - 'CWD' (Authenticated) Remote Memory Consumption                                                        | linux/dos/5814.pl
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (1)                                                        | windows/dos/31818.sh
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (2)                                                        | windows/dos/31819.pl
vsftpd 2.3.2 - Denial of Service                                                                                      | linux/dos/16270.c
vsftpd 2.3.4 - Backdoor Command Execution (Metasploit)                                                                | unix/remote/17491.rb
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

Also tried an unsuccessful anonymous login

```text
root@kali:~/CTF/HTB/SneakyMailer# ftp -p 10.10.10.197
Connected to 10.10.10.197.
220 (vsFTPd 3.0.3)
Name (10.10.10.197:root): anonymous
530 Permission denied.
Login failed.
ftp> quit
221 Goodbye.
```

Lastly I ran all the available nmap FTP scripts against it but found nothing

```text
root@kali:~/CTF/HTB/SneakyMailer# nmap -Pn -n -sV -p21 --script=ftp* 10.10.10.197 -e tun0
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-20 02:15 +08
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] passwords: Time limit 10m00s exceeded.
Nmap scan report for 10.10.10.197
Host is up (0.014s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-brute:
|   Accounts: No valid accounts found
|_  Statistics: Performed 10679 guesses in 600 seconds, average tps: 17.9
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 600.90 seconds
```

