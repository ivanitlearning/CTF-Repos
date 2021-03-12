# Web server 8080 enumeration

I ran gobuster on both hostnames on port 8080, but found nothing.

```text
root@kali:~/CTF/HTB/SneakyMailer# gobuster dir -u http://sneakycorp.htb:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://sneakycorp.htb:8080
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     html,htm,conf,pl,php,txt,cgi,bak,sh
[+] Timeout:        50s
===============================================================
2021/02/20 02:54:58 Starting gobuster
===============================================================
/index.html (Status: 200)
===============================================================
2021/02/20 02:59:11 Finished
===============================================================

root@kali:~/CTF/HTB/SneakyMailer# gobuster dir -u http://sneakymailer.htb:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://sneakymailer.htb:8080
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,html,conf,bak,sh,cgi,txt,htm,pl
[+] Timeout:        50s
===============================================================
2021/02/20 03:02:57 Starting gobuster
===============================================================
/index.html (Status: 200)
===============================================================
2021/02/20 03:07:09 Finished
===============================================================
```

