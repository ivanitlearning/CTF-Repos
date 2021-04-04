# nikto and gobuster
First nikto

```text
root@kali:~/CTF/HTB/TartarSauce# nikto -h http://10.10.10.88
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.88
+ Target Hostname:    10.10.10.88
+ Target Port:        80
+ Start Time:         2021-03-23 21:47:04 (GMT8)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Cookie PHPSESSID created without the httponly flag
+ Entry '/webservices/monstra-3.0.4/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ "robots.txt" contains 5 entries which should be manually viewed.
+ Server may leak inodes via ETags, header found with file /, inode: 2a0e, size: 565becf5ff08d, mtime: gzip
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7881 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2021-03-23 21:48:47 (GMT8) (103 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Then I ran gobuster on those paths in robots.txt which returned 404 to see if there was anything else hidden.

```text
root@kali:~/CTF/HTB/TartarSauce# gobuster dir -u http://tartarsauce.htb/tar/tar/sauce -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://tartarsauce.htb/tar/tar/sauce
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,txt,bak,pl,cgi,html,htm,conf,sh
[+] Timeout:        50s
===============================================================
2021/03/23 22:34:05 Starting gobuster
===============================================================
===============================================================
2021/03/23 22:39:02 Finished
===============================================================
	
root@kali:~/CTF/HTB/TartarSauce# gobuster dir -u http://tartarsauce.htb/webservices/easy-file-uploader/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://tartarsauce.htb/webservices/easy-file-uploader/
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     txt,bak,pl,cgi,php,html,htm,conf,sh
[+] Timeout:        50s
===============================================================
2021/03/23 23:01:08 Starting gobuster
===============================================================
===============================================================
2021/03/23 23:06:34 Finished
===============================================================

root@kali:~/CTF/HTB/TartarSauce# gobuster dir -u http://tartarsauce.htb/webservices/developmental/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.txt,.html,.htm,.conf,.bak,.sh,.pl,.cgi --timeout 50s -t 170
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://tartarsauce.htb/webservices/developmental/
[+] Threads:        170
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     sh,html,htm,bak,pl,cgi,php,txt,conf
[+] Timeout:        50s
===============================================================
2021/03/23 23:11:11 Starting gobuster
===============================================================
===============================================================
2021/03/23 23:16:37 Finished
===============================================================
```

Nothing, unfortunately.