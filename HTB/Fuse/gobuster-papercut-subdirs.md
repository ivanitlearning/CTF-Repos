# gobuster papercut subdirs

The URL of the landing page is **fuse.fabricorp.local/papercut/logs/html/index.htm** so I thought of gobustering **/papercut**, **/logs**, **/html**

```text
root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,txt,html,htm,pl,conf,bak,sh,cgi,asp,aspx
[+] Timeout:        50s
===============================================================
2021/01/16 21:49:35 Starting gobuster
===============================================================
/resources (Status: 301)
/Resources (Status: 301)
/logs (Status: 301)
===============================================================
2021/01/16 22:04:34 Finished
===============================================================
```

Trying /papercut/resources

```text
root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut/resources -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut/resources
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     bak,pl,cgi,aspx,php,html,conf,asp,txt,htm,sh
[+] Timeout:        50s
===============================================================
2021/01/16 23:04:50 Starting gobuster
===============================================================
/icons (Status: 301)
/about.htm (Status: 200)
/layout (Status: 301)
===============================================================
2021/01/16 23:19:10 Finished
===============================================================
```

Trying /papercut/logs

```text
root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut/logs -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut/logs
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     htm,bak,sh,pl,asp,html,txt,conf,cgi,aspx,php
[+] Timeout:        50s
===============================================================
2021/01/16 23:20:14 Starting gobuster
===============================================================
/html (Status: 301)
/csv (Status: 301)
===============================================================
2021/01/16 23:34:43 Finished
===============================================================
```

There was nothing in /papercut/logs/csv/daily

```text
root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut/logs/csv -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut/logs/csv
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     sh,asp,htm,conf,bak,pl,cgi,aspx,php,txt,html
[+] Timeout:        50s
===============================================================
2021/01/16 23:45:39 Starting gobuster
===============================================================
/daily (Status: 301)
/monthly (Status: 301)
===============================================================
2021/01/16 23:59:13 Finished
===============================================================

root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut/logs/csv/daily -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut/logs/csv/daily
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     asp,php,txt,html,conf,sh,cgi,htm,bak,pl,aspx
[+] Timeout:        50s
===============================================================
2021/01/17 00:03:15 Starting gobuster
===============================================================
===============================================================
2021/01/17 00:22:50 Finished
===============================================================
```

Lastly trying **/papercut/resources/layout**

```text
root@kali:~/CTF/HTB/Fuse# gobuster dir -u http://fuse.fabricorp.local/papercut/resources/layout -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 100
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://fuse.fabricorp.local/papercut/resources/layout
[+] Threads:        100
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     aspx,php,txt,htm,sh,pl,cgi,asp,html,conf,bak
[+] Timeout:        50s
===============================================================
2021/01/18 23:01:53 Starting gobuster
===============================================================
===============================================================
2021/01/18 23:16:49 Finished
===============================================================
```

All nothing