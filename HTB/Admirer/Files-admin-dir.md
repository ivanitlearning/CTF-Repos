# Files in /admin-dir

**contacts.txt** showed this (shown in Burp)

```text
HTTP/1.1 200 OK
Date: Sun, 27 Dec 2020 12:06:15 GMT
Server: Apache/2.4.25 (Debian)
Last-Modified: Wed, 29 Apr 2020 09:18:35 GMT
ETag: "15e-5a46a6ec54540-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 350
Connection: close
Content-Type: text/plain

##########
# admins #
##########
# Penny
Email: p.wise@admirer.htb


##############
# developers #
##############
# Rajesh
Email: r.nayyar@admirer.htb

# Amy
Email: a.bialik@admirer.htb

# Leonard
Email: l.galecki@admirer.htb



#############
# designers #
#############
# Howard
Email: h.helberg@admirer.htb

# Bernadette
Email: b.rauch@admirer.htb
```

**credentials.txt**

```text
HTTP/1.1 200 OK
Date: Sun, 27 Dec 2020 12:12:25 GMT
Server: Apache/2.4.25 (Debian)
Last-Modified: Wed, 29 Apr 2020 09:11:31 GMT
ETag: "88-5a46a5583b1c0-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 136
Connection: close
Content-Type: text/plain

[Internal mail account]
w.cooper@admirer.htb
fgJr6q#S\W:$P

[FTP account]
ftpuser
%n?4Wz}R$tTF7

[Wordpress account]
admin
w0rdpr3ss01!
```



