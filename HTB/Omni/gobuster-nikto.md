# gobuster and nikto

Tried gobustering

```text
root@kali:~/CTF/HTB/Omni# gobuster dir -u http://10.10.10.204:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi.asp,aspx --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.204:8080
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     txt,htm,bak,aspx,php,html,conf,sh,pl,cgi.asp
[+] Timeout:        50s
===============================================================
2021/03/03 22:32:47 Starting gobuster
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://10.10.10.204:8080/ab2e01cd-8105-4f50-8392-e9e5e9555fb6 => 401. To force processing of Wildcard responses, specify the '--wildcard' switch
```

We need to exclude 401 responses.

```text
root@kali:~/CTF/HTB/Omni# gobuster dir -u http://10.10.10.204:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi.asp,aspx --timeout 50s -t 170 -s 200,204,301,302,307,403
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.204:8080
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,txt,bak,sh,pl,cgi.asp,html,htm,conf,aspx
[+] Timeout:        50s
===============================================================
2021/03/03 22:33:41 Starting gobuster
===============================================================
===============================================================
2021/03/03 22:47:22 Finished
===============================================================
```

But we find nothing. I also tried nikto but nothing too.

```text
root@kali:~/CTF/HTB/Omni# nikto -h http://10.10.10.204:8080
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.204
+ Target Hostname:    10.10.10.204
+ Target Port:        8080
+ Start Time:         2021-03-03 22:50:26 (GMT8)
---------------------------------------------------------------------------
+ Server: Microsoft-HTTPAPI/2.0
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Cookie CSRF-Token created without the httponly flag
+ / - Requires Authentication for realm 'Windows Device Portal'
+ Default account found for 'Windows Device Portal' at / (ID '', PW '_Cisco'). Cisco device.
+ Root page / redirects to: /authorizationrequired.htm
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 7867 requests: 1 error(s) and 5 item(s) reported on remote host
+ End Time:           2021-03-03 22:51:58 (GMT8) (92 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

