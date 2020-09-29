# TCP 631 CUPS

I saw these from linpeas which was CUPS listening on localhost, running as root user.
```
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -               
root      1496  0.0  0.6  14196  6892 ?        Ss   13:16   0:00 /usr/sbin/cupsd -l
root      1498  0.0  0.8  37564  8788 ?        Ssl  13:16   0:00 /usr/sbin/cups-browsed
```
We forward this back to Kali since we don't have roosa's SSH password (though I learned later it was possible to [do that](https://stackoverflow.com/questions/47804851/remote-port-forwarding-with-ssh-keys)) Local port forward 22 to 2222 on Kali
```shell
root@Kali:~/HTB/DevOops/feed# ssh -f -N -L 0.0.0.0:2222:localhost:22 root@localhost
root@localhost's password: 
```

Remote port forward to Kali:
```shell
roosa@gitter:/var$ ssh -f -N -R 631:127.0.0.1:631 root@10.10.14.78 -p 2222
The authenticity of host '[10.10.14.78]:2222 ([10.10.14.78]:2222)' can't be established.
ECDSA key fingerprint is SHA256:HRvXIeB7FuR8syEm3D1KDRx6s3O7n4jJQmXw4ald9PA.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[10.10.14.78]:2222' (ECDSA) to the list of known hosts.
root@10.10.14.78's password: 
```

Now let's run an `nmap` scan
```shell
root@Kali:~/HTB/DevOops/feed# nmap -Pn -n -sV -p631 --script=vuln,discovery localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-26 02:20 +08
too short
Pre-scan script results:
| broadcast-igmp-discovery: 
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 224.0.0.251
|     Description: mDNS (rfc6762)
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 224.0.0.252
|     Description: Link-local Multicast Name Resolution (rfc4795)
|_  Use the newtargets script-arg to add the results as targets
| ipv6-multicast-mld-list: 
|   fe80::b041:cdc8:aed5:1dee: 
|     device: eth0
|     mac: 00:50:56:c0:00:08
|     multicast_ips: 
|       ff02::1:ffd5:1dee         (NDP Solicited-node)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:ff26:b582         (Solicited-Node Address)
|       ff02::c                   (SSDP)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::fb                  (mDNSv6)
|_      ff02::1:3                 (Link-local Multicast Name Resolution)
| targets-asn: 
|_  targets-asn.asn is a mandatory parameter
| targets-ipv6-multicast-mld: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
| 
|_  Use --script-args=newtargets to add the results as targets
| targets-ipv6-multicast-slaac: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|   IP: fe80::1037:fd18:3926:b582  MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(33, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:11518 > 127.0.0.1:631 S ttl=128 id=0 iplen=0  seq=626517041 win=3072 <mss 1460>
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000044s latency).
Other addresses for localhost (not scanned): ::1

PORT    STATE SERVICE VERSION
631/tcp open  ipp     CUPS 2.1
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
|_cups-info: ERROR: Script execution failed (use -d to debug)
|_cups-queue-info: ERROR: Script execution failed (use -d to debug)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
| http-backup-finder: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=localhost
|   http://localhost:631/help/man-cupsd.conf.bak
|   http://localhost:631/help/man-cupsd.conf.html~
|   http://localhost:631/help/man-cupsd.conf copy.html
|   http://localhost:631/help/Copy of man-cupsd.conf.html
|   http://localhost:631/help/Copy (2) of man-cupsd.conf.html
|   http://localhost:631/help/man-cupsd.conf.html.1
|_  http://localhost:631/help/man-cupsd.conf.html.~1~
|_http-chrono: Request times for /; avg: 1178.42ms; min: 157.25ms; max: 5068.99ms
|_http-date: Fri, 25 Sep 2020 18:21:30 GMT; -6s from local time.
| http-headers: 
|   Connection: close
|   Content-Language: en_US
|   Content-Length: 2361
|   Content-Type: text/html; charset=utf-8
|   Date: Fri, 25 Sep 2020 18:21:30 GMT
|   Last-Modified: Mon, 19 Feb 2018 17:51:16 GMT
|   Accept-Encoding: gzip, deflate, identity
|   Server: CUPS/2.1 IPP/2.1
|   X-Frame-Options: DENY
|   Content-Security-Policy: frame-ancestors 'none'
|   
|_  (Request type: GET)
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: CUPS/2.1 IPP/2.1
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-title: Home - CUPS 2.1.3
| http-vhosts: 
| 103 names had status 400
|_24 names had status ERROR
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
| http-waf-detect: IDS/IPS/WAF detected:
|_localhost:631/?p4yl04d3=<script>alert(document.cookie)</script>
| vulners: 
|   cpe:/a:apple:cups:2.1: 
|     	CVE-2009-0032	6.9	https://vulners.com/cve/CVE-2009-0032
|     	CVE-2012-6094	6.8	https://vulners.com/cve/CVE-2012-6094
|     	CVE-2010-3702	6.8	https://vulners.com/cve/CVE-2010-3702
|     	CVE-2017-18190	5.0	https://vulners.com/cve/CVE-2017-18190
|     	CVE-2018-4300	4.3	https://vulners.com/cve/CVE-2018-4300
|     	CVE-2017-18248	3.5	https://vulners.com/cve/CVE-2017-18248
|_    	CVE-2008-1033	2.1	https://vulners.com/cve/CVE-2008-1033

Host script results:
|_dns-brute: Can't guess domain of "localhost"; use dns-brute.domain script argument.
|_fcrdns: PASS (localhost)
| hostmap-crtsh: 
|_  subdomains: Error: found no hostnames but not the marker for "name_value" (pattern error?)
|_ipidseq: ERROR: Script execution failed (use -d to debug)
|_path-mtu: 65535 <= PMTU < 65536
| resolveall: 
|   Host 'localhost' also resolves to:
|   Use the 'newtargets' script-arg to add the results as targets
|_  Use the --resolve-all option to scan all resolved addresses without using this script.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 73.76 seconds
```
Then checking `searchsploit`. Unfortunately version 2.1 doesn't have any known public exploits.
```shell
root@Kali:~/HTB/DevOops/feed# searchsploit CUPS
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                      |  Path
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
APC UPS 3.7.2 - 'apcupsd' Local Denial of Service                                                                   | linux/dos/251.c
CUPS - 'kerberos' Cross-Site Scripting                                                                              | multiple/remote/10001.txt
CUPS 1.1.x - '.HPGL' File Processor Buffer Overflow                                                                 | linux/remote/24977.txt
CUPS 1.1.x - Cupsd Request Method Denial of Service                                                                 | linux/dos/22619.txt
CUPS 1.1.x - Negative Length HTTP Header                                                                            | linux/remote/22106.txt
CUPS 1.1.x - UDP Packet Remote Denial of Service                                                                    | linux/dos/24599.txt
CUPS 1.3.7 - 'HP-GL/2' Filter Remote Code Execution                                                                 | linux/remote/32470.rb
CUPS 1.3.7 - Cross-Site Request Forgery (Add RSS Subscription) Remote Crash                                         | linux/dos/7150.html
CUPS 1.3.9 - 'cups/ipp.c' Null Pointer Dereference Denial of Service                                                | linux/dos/33020.py
CUPS 1.4.2 - Web Interface Information Disclosure                                                                   | linux/remote/34152.txt
CUPS < 1.3.8-4 - Local Privilege Escalation                                                                         | multiple/local/7550.c
CUPS < 2.0.3 - Multiple Vulnerabilities                                                                             | multiple/remote/37336.txt
CUPS < 2.0.3 - Remote Command Execution                                                                             | linux/remote/41233.py
Cups Easy 1.0 - Cross Site Request Forgery (Password Reset)                                                         | php/webapps/47973.txt
CUPS Filter - Bash Environment Variable Code Injection (Metasploit)                                                 | linux/remote/35115.rb
CUPS Server 1.1 - GET Denial of Service                                                                             | linux/dos/1196.c

-------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```