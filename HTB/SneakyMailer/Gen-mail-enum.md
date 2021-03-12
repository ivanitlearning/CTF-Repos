# General mail service enumeration

## SMTP enumeration

First I tried a searchsploit for the port 25 banner **Postfix smtpd** which found nothing

```text
root@kali:~/CTF/HTB/SneakyMailer# searchsploit postfix
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                        |  Path
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
gld 1.4 - Postfix Greylisting Daemon Remote Format String                                                             | linux/remote/934.c
Postfix 1.1.x - Denial of Service (1)                                                                                 | linux/dos/22981.c
Postfix 1.1.x - Denial of Service (2)                                                                                 | linux/dos/22982.pl
Postfix 2.6-20080814 - 'symlink' Local Privilege Escalation                                                           | linux/local/6337.sh
Postfix < 2.4.9/2.5.5/2.6-20080902 - '.forward' Local Denial of Service                                               | multiple/dos/6472.c
Postfix SMTP 4.2.x < 4.2.48 - 'Shellshock' Remote Command Injection                                                   | linux/remote/34896.py
Salim Gasmi GLD (Greylisting Daemon) - Postfix Buffer Overflow (Metasploit)                                           | linux/remote/16841.rb
Salim Gasmi GLD (Greylisting Daemon) 1.0 < 1.4 - Postfix Greylisting Buffer Overflow (Metasploit)                     | linux/remote/10023.rb
Salim Gasmi GLD (Greylisting Daemon) 1.x - Postfix Greylisting Daemon Buffer Overflow                                 | linux/remote/25392.c
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

Then I tried a VRFY enumeration to see which emails were valid but despite using either an email list or just the usernames I found nothing.

```text
root@kali:~/CTF/HTB/SneakyMailer# smtp-user-enum -U users.txt -t 10.10.10.197
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... users.txt
Target count ............. 1
Username count ........... 57
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............

######## Scan started at Sat Feb 27 01:36:08 2021 #########
######## Scan completed at Sat Feb 27 01:37:08 2021 #########
0 results.

57 queries in 60 seconds (0.9 queries / sec)

root@kali:~/CTF/HTB/SneakyMailer# smtp-user-enum -U emails.txt -t 10.10.10.197
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... emails.txt
Target count ............. 1
Username count ........... 57
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............

######## Scan started at Sat Feb 27 01:53:44 2021 #########
######## Scan completed at Sat Feb 27 01:54:44 2021 #########
0 results.

57 queries in 60 seconds (0.9 queries / sec)
```

I also tried hydra but it returned similar results (none).

```text
root@kali:~/CTF/HTB/SneakyMailer# hydra smtp-enum://10.10.10.197/vrfy -L users.txt -p 10.10.10.197
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-02-27 01:38:30
[DATA] max 16 tasks per 1 server, overall 16 tasks, 57 login tries (l:57/p:1), ~4 tries per task
[DATA] attacking smtp-enum://10.10.10.197:25/vrfy
1 of 1 target completed, 0 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-02-27 01:38:41
root@kali:~/CTF/HTB/SneakyMailer# hydra smtp-enum://10.10.10.197/vrfy -L emails.txt -p 10.10.10.197
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-02-27 01:39:26
[DATA] max 16 tasks per 1 server, overall 16 tasks, 57 login tries (l:57/p:1), ~4 tries per task
[DATA] attacking smtp-enum://10.10.10.197:25/vrfy
1 of 1 target completed, 0 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-02-27 01:39:38
```

### General IMAP enumeration

searchsploit found nothing for the IMAP banner **Courier Imapd (released 2018)**

```text
root@kali:~/CTF/HTB/SneakyMailer# searchsploit imapd
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                        |  Path
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
Alt-N MDaemon 9.6.4 - IMAPD FETCH Buffer Overflow (Metasploit)                                                        | windows/remote/16482.rb
Cyrus IMAPD - pop3d popsubfolders USER Buffer Overflow (Metasploit)                                                   | linux/remote/16836.rb
Cyrus IMAPD 1.4/1.5.19/2.0.12/2.0.16/2.1.9/2.1.10 - Pre-Login Heap Corruption                                         | linux/dos/22061.txt
Cyrus imapd 2.2.4 < 2.2.8 - 'imapmagicplus' Remote Overflow                                                           | linux/remote/903.c
Cyrus IMAPD 2.3.2 - 'pop3d' Remote Buffer Overflow (1)                                                                | linux/remote/1813.c
Cyrus IMAPD 2.3.2 - 'pop3d' Remote Buffer Overflow (2)                                                                | multiple/remote/2053.rb
Cyrus IMAPD 2.3.2 - 'pop3d' Remote Buffer Overflow (3)                                                                | linux/remote/2185.pl
Eudora Qualcomm WorldMail 3.0 - 'IMAPd' Remote Overflow                                                               | windows/remote/1380.py
Eudora Qualcomm WorldMail 3.0 - IMAPd 'LIST' Remote Buffer Overflow (Metasploit)                                      | windows/remote/16474.rb
Eudora Qualcomm WorldMail 9.0.333.0 - IMAPd Service UID Buffer Overflow                                               | windows/remote/31694.py
FTGate4 Groupware Mail Server 4.1 - imapd Remote Buffer Overflow (PoC)                                                | windows/dos/1327.pl
Ipswitch IMail 5.0 - Imapd Buffer Overflow (Denial of Service) (PoC)                                                  | multiple/dos/19377.txt
IPSwitch IMail Server 8.15 - IMAPD Remote Code Execution                                                              | linux/remote/1124.pl
IPSwitch IMail Server 8.20 - IMAPD Remote Buffer Overflow                                                             | windows/remote/3627.c
Linux imapd - Remote Overflow / File Retrieve                                                                         | linux/remote/340.c
MailEnable - IMAPD W3C Logging Buffer Overflow (Metasploit)                                                           | windows/remote/16480.rb
MailEnable 1.54 Pro - Universal IMAPD W3C Logging Buffer Overflow (Metasploit)                                        | windows/remote/1332.pm
MailEnable Enterprise 1.x - IMAPd Remote Overflow                                                                     | linux/remote/915.c
MailEnable IMAPD 1.54 - STATUS Request Buffer Overflow (Metasploit)                                                   | windows/remote/16485.rb
MailEnable IMAPD Enterprise 2.32 < 2.34 - Remote Buffer Overflow                                                      | windows/remote/3319.pl
MailEnable IMAPD Professional (2.35) - Login Request Buffer Overflow (Metasploit)                                     | windows/remote/16475.rb
MailEnable IMAPD Professional 2.35 - Remote Buffer Overflow                                                           | windows/remote/3320.pl
MDaemon 8.0.3 - IMAPD CRAM-MD5 Authentication Overflow (Metasploit)                                                   | windows/remote/1151.pm
Mercur IMAPD 5.00.14 (Windows x86) - Remote Denial of Service                                                         | windows_x86/dos/3527.pl
Mercury/32 4.52 IMAPD - 'SEARCH' (Authenticated) Overflow                                                             | windows/remote/4429.pl
Netscape Messaging Server 3.55 & University of Washington imapd 10.234 - Remote Buffer Overflow                       | linux/remote/19107.c
Perdition 1.17 - IMAPD __STR_VWRITE Remote Format String                                                              | linux/dos/30724.txt
UoW IMAPd Serve 10.234/12.264 - COPY Buffer Overflow (Metasploit)                                                     | unix/remote/19849.pm
UoW IMAPd Server - LSUB Buffer Overflow (Metasploit)                                                                  | linux/remote/16846.rb
UoW IMAPd Server 10.234/12.264 - LSUB Buffer Overflow (Metasploit)                                                    | unix/remote/19848.pm
UoW IMAPd Server 10.234/12.264 - Remote Buffer Overflow                                                               | unix/remote/19847.c
WorldMail IMAPd 3.0 - Remote Overflow (SEH) (Egghunter)                                                               | windows/remote/18354.py
WU-IMAPd 2000/2001 - Partial Mailbox Attribute Remote Buffer Overflow (1)                                             | linux/remote/21442.c
WU-IMAPd 2000/2001 - Partial Mailbox Attribute Remote Buffer Overflow (2)                                             | linux/remote/21443.c
---------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

