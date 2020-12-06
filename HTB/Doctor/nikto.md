# nikto scans

This scan was run right at the start on the Web server.

```shell
root@Kali:~/HTB/Doctor# nikto -h http://10.10.10.209
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.209
+ Target Hostname:    10.10.10.209
+ Target Port:        80
+ Start Time:         2020-11-24 21:42:52 (GMT8)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server may leak inodes via ETags, header found with file /, inode: 4d88, size: 5afad8bea6589, mtime: gzip
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST
+ OSVDB-3268: /css/: Directory indexing found.
+ OSVDB-3092: /css/: This might be interesting...
+ OSVDB-3268: /images/: Directory indexing found.
+ 7863 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2020-11-24 21:44:38 (GMT8) (106 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


      *********************************************************************
      Portions of the server's headers (Apache/2.4.41) are not in
      the Nikto 2.1.6 database or are newer than the known string. Would you like
      to submit this information (*no server specific data*) to CIRT.net
      for a Nikto update (or you may email to sullo@cirt.net) (y/n)? y

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ The site uses SSL and Expect-CT header is not present.
- Sent updated info to cirt.net -- Thank you!
```

Later when I discovered the domain name I re-did the scan again on the vhost.

```shell
root@kali:~/CTF/HTB/Doctor# nikto -h http://doctors.htb
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.209
+ Target Hostname:    doctors.htb
+ Target Port:        80
+ Start Time:         2020-12-06 13:51:43 (GMT8)
---------------------------------------------------------------------------
+ Server: Werkzeug/1.0.1 Python/3.8.2
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Root page / redirects to: http://doctors.htb/login?next=%2F
+ Server banner has changed from 'Werkzeug/1.0.1 Python/3.8.2' to 'Apache/2.4.41 (Ubuntu)' which may suggest a WAF, load balancer or proxy is in place
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET
+ 7785 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2020-12-06 13:53:52 (GMT8) (129 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


      *********************************************************************
      Portions of the server's headers (Python/3.8.2) are not in
      the Nikto 2.1.6 database or are newer than the known string. Would you like
      to submit this information (*no server specific data*) to CIRT.net
      for a Nikto update (or you may email to sullo@cirt.net) (y/n)? y

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ The site uses SSL and Expect-CT header is not present.
- Sent updated info to cirt.net -- Thank you!
```

