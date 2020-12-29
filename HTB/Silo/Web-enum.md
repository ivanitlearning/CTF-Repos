# Web enumeration

nikto found nothing

```text
root@kali:~/CTF/HTB/Silo# nikto -h http://10.10.10.82
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.82
+ Target Hostname:    10.10.10.82
+ Target Port:        80
+ Start Time:         2020-12-20 20:07:05 (GMT8)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/8.5
+ Retrieved x-powered-by header: ASP.NET
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-aspnet-version header: 4.0.30319
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST
+ Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST
+ 7863 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2020-12-20 20:08:14 (GMT8) (69 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Neither did gobuster

```text
root@kali:~/CTF/HTB/Silo# gobuster dir -u http://10.10.10.82 -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi,.asp,.aspx --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.82
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     sh,asp,aspx,php,html,htm,conf,bak,txt,pl,cgi
[+] Timeout:        50s
===============================================================
2020/12/20 20:08:58 Starting gobuster
===============================================================
[ERROR] 2020/12/20 20:17:43 [!] read tcp 10.10.14.78:45864->10.10.10.82:80: read: connection reset by peer
[ERROR] 2020/12/20 20:17:43 [!] read tcp 10.10.14.78:46160->10.10.10.82:80: read: connection reset by peer
[ERROR] 2020/12/20 20:17:43 [!] read tcp 10.10.14.78:45966->10.10.10.82:80: read: connection reset by peer
===============================================================
2020/12/20 20:25:59 Finished
===============================================================
```

