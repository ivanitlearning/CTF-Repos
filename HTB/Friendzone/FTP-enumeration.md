# FTP enumeration

Let's try the nmap FTP scripts

```plaintext
root@Kali:~/HTB/Friendzone# nmap -Pn -n -sV -p21 --script=ftp* 10.10.10.123 -e tun0
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-12 00:06 +08
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] passwords: Time limit 10m00s exceeded.
Nmap scan report for 10.10.10.123
Host is up (0.0055s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-brute: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 3611 guesses in 602 seconds, average tps: 6.0
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 602.57 seconds
```

Nothing. There's no indication that anonymous logins are allowed which I tried anyway

```plaintext
root@Kali:~/HTB/Friendzone# ftp -p 10.10.10.123
Connected to 10.10.10.123.
220 (vsFTPd 3.0.3)
Name (10.10.10.123:root): anonymous
331 Please specify the password.
Password:
530 Login incorrect.
Login failed.
ftp> quit
221 Goodbye.
```

The FTP version 3.0.3 also appears to not be vulnerable

```plaintext
root@Kali:~/HTB/Friendzone# searchsploit vsftpd
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                      |  Path
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
vsftpd 2.0.5 - 'CWD' (Authenticated) Remote Memory Consumption                                                      | linux/dos/5814.pl
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (1)                                                      | windows/dos/31818.sh
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (2)                                                      | windows/dos/31819.pl
vsftpd 2.3.2 - Denial of Service                                                                                    | linux/dos/16270.c
vsftpd 2.3.4 - Backdoor Command Execution (Metasploit)                                                              | unix/remote/17491.rb
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

