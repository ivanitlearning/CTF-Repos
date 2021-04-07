# nikto

nikto scan

```text
root@kali:~/CTF/HTB/Node# nikto -h http://10.10.10.58:3000
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.58
+ Target Hostname:    10.10.10.58
+ Target Port:        3000
+ Start Time:         2021-04-02 00:31:12 (GMT8)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ Retrieved x-powered-by header: Express
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /backup.jks: Potentially interesting archive/cert file found.
+ /backup.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.war: Potentially interesting archive/cert file found.
+ /101010.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.alz: Potentially interesting archive/cert file found.
+ /10.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.egg: Potentially interesting archive/cert file found.
+ /10.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.cer: Potentially interesting archive/cert file found.
+ /site.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.egg: Potentially interesting archive/cert file found.
+ /1010.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.jks: Potentially interesting archive/cert file found.
+ /1010.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.alz: Potentially interesting archive/cert file found.
+ /101010.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.egg: Potentially interesting archive/cert file found.
+ /backup.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.tar.lzma: Potentially interesting archive/cert file found.
+ /10.10.10.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.tgz: Potentially interesting archive/cert file found.
+ /10.10.10.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.tar: Potentially interesting archive/cert file found.
+ /10.10.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.tar.lzma: Potentially interesting archive/cert file found.
+ /101010.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.war: Potentially interesting archive/cert file found.
+ /10101058.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.alz: Potentially interesting archive/cert file found.
+ /site.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.egg: Potentially interesting archive/cert file found.
+ /10.10.10.58.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.alz: Potentially interesting archive/cert file found.
+ /58.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.egg: Potentially interesting archive/cert file found.
+ /58.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.pem: Potentially interesting archive/cert file found.
+ /site.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.cer: Potentially interesting archive/cert file found.
+ /10_10_10_58.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.tar.bz2: Potentially interesting archive/cert file found.
+ /10.10.10.58.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.pem: Potentially interesting archive/cert file found.
+ /10.10.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.war: Potentially interesting archive/cert file found.
+ /1010.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.war: Potentially interesting archive/cert file found.
+ /10.10.10.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.jks: Potentially interesting archive/cert file found.
+ /10.10.10.58.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.tar.lzma: Potentially interesting archive/cert file found.
+ /10101058.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.tgz: Potentially interesting archive/cert file found.
+ /10101058.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.tar: Potentially interesting archive/cert file found.
+ /backup.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.war: Potentially interesting archive/cert file found.
+ /10.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.tar: Potentially interesting archive/cert file found.
+ /1010.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.tgz: Potentially interesting archive/cert file found.
+ /backup.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.cer: Potentially interesting archive/cert file found.
+ /10.10.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.pem: Potentially interesting archive/cert file found.
+ /backup.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.jks: Potentially interesting archive/cert file found.
+ /10_10_10_58.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.tar: Potentially interesting archive/cert file found.
+ /58.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.tar.lzma: Potentially interesting archive/cert file found.
+ /site.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.tar.bz2: Potentially interesting archive/cert file found.
+ /site.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.tgz: Potentially interesting archive/cert file found.
+ /1010.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.cer: Potentially interesting archive/cert file found.
+ /10.10.10.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.tar.bz2: Potentially interesting archive/cert file found.
+ /10_10_10_58.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.cer: Potentially interesting archive/cert file found.
+ /10.10.10.58.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.tar.bz2: Potentially interesting archive/cert file found.
+ /backup.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.egg: Potentially interesting archive/cert file found.
+ /10_10_10_58.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.tgz: Potentially interesting archive/cert file found.
+ /10.10.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.war: Potentially interesting archive/cert file found.
+ /58.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.cer: Potentially interesting archive/cert file found.
+ /10101058.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.tar: Potentially interesting archive/cert file found.
+ /10.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.cer: Potentially interesting archive/cert file found.
+ /backup.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.tgz: Potentially interesting archive/cert file found.
+ /58.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.jks: Potentially interesting archive/cert file found.
+ /10.10.10.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.war: Potentially interesting archive/cert file found.
+ /site.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.egg: Potentially interesting archive/cert file found.
+ /10.10.10.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.tar.bz2: Potentially interesting archive/cert file found.
+ /101010.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.pem: Potentially interesting archive/cert file found.
+ /10101058.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.pem: Potentially interesting archive/cert file found.
+ /1010.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.tar.lzma: Potentially interesting archive/cert file found.
+ /10_10_10_58.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.tar.lzma: Potentially interesting archive/cert file found.
+ /58.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.alz: Potentially interesting archive/cert file found.
+ /10101058.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.cer: Potentially interesting archive/cert file found.
+ /101010.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.tar.lzma: Potentially interesting archive/cert file found.
+ /10.10.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.war: Potentially interesting archive/cert file found.
+ /10.10.10.58.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.pem: Potentially interesting archive/cert file found.
+ /10.10.10.58.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.pem: Potentially interesting archive/cert file found.
+ /101010.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.tar.lzma: Potentially interesting archive/cert file found.
+ /10.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.pem: Potentially interesting archive/cert file found.
+ /10.10.10.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.jks: Potentially interesting archive/cert file found.
+ /site.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.egg: Potentially interesting archive/cert file found.
+ /10101058.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.cer: Potentially interesting archive/cert file found.
+ /1010.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.egg: Potentially interesting archive/cert file found.
+ /site.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.jks: Potentially interesting archive/cert file found.
+ /10101058.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.tgz: Potentially interesting archive/cert file found.
+ /101010.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.tar: Potentially interesting archive/cert file found.
+ /10.10.10.58.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.tgz: Potentially interesting archive/cert file found.
+ /10.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.tgz: Potentially interesting archive/cert file found.
+ /10_10_10_58.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.war: Potentially interesting archive/cert file found.
+ /10.10.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.alz: Potentially interesting archive/cert file found.
+ /1010.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.alz: Potentially interesting archive/cert file found.
+ /10.10.10.58.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.alz: Potentially interesting archive/cert file found.
+ /10.10.10.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.tar.bz2: Potentially interesting archive/cert file found.
+ /10.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.alz: Potentially interesting archive/cert file found.
+ /10_10_10_58.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.cer: Potentially interesting archive/cert file found.
+ /10.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.tgz: Potentially interesting archive/cert file found.
+ /10.10.10.58.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.egg: Potentially interesting archive/cert file found.
+ /10.10.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.jks: Potentially interesting archive/cert file found.
+ /58.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.tar.bz2: Potentially interesting archive/cert file found.
+ /10101058.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.alz: Potentially interesting archive/cert file found.
+ /10.10.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.pem: Potentially interesting archive/cert file found.
+ /58.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.tar: Potentially interesting archive/cert file found.
+ /101010.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10101058.tar: Potentially interesting archive/cert file found.
+ /10101058.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.tar.bz2: Potentially interesting archive/cert file found.
+ /10.10.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.tar: Potentially interesting archive/cert file found.
+ /10_10_10_58.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.jks: Potentially interesting archive/cert file found.
+ /10.10.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.pem: Potentially interesting archive/cert file found.
+ /10.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.tar.bz2: Potentially interesting archive/cert file found.
+ /10.10.10.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.jks: Potentially interesting archive/cert file found.
+ /101010.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.war: Potentially interesting archive/cert file found.
+ /backup.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.jks: Potentially interesting archive/cert file found.
+ /10.jks: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.cer: Potentially interesting archive/cert file found.
+ /58.cer: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.pem: Potentially interesting archive/cert file found.
+ /10_10_10_58.pem: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10_10_10_58.war: Potentially interesting archive/cert file found.
+ /10_10_10_58.war: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.tar: Potentially interesting archive/cert file found.
+ /site.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /58.tar.bz2: Potentially interesting archive/cert file found.
+ /58.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.tar.lzma: Potentially interesting archive/cert file found.
+ /backup.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.tar.bz2: Potentially interesting archive/cert file found.
+ /1010.tar.bz2: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.58.tar.lzma: Potentially interesting archive/cert file found.
+ /10.10.10.58.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /101010.egg: Potentially interesting archive/cert file found.
+ /101010.egg: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /1010.tar.lzma: Potentially interesting archive/cert file found.
+ /1010.tar.lzma: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /10.10.10.tar: Potentially interesting archive/cert file found.
+ /10.10.10.tar: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /backup.alz: Potentially interesting archive/cert file found.
+ /backup.alz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ /site.tgz: Potentially interesting archive/cert file found.
+ /site.tgz: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ ERROR: Error limit (20) reached for host, giving up. Last error: error reading HTTP response
+ Scan terminated:  20 error(s) and 224 item(s) reported on remote host
+ End Time:           2021-04-02 00:31:41 (GMT8) (29 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

