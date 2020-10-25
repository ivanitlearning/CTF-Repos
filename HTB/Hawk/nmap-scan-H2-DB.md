# nmap scan on H2 database
This scan was run after I remote port-forwarded back to Kali
```shell
root@Kali:~/HTB/Hawk# nmap -Pn -n -sV -p8082,9092 --script=vuln,discovery localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-23 23:03 +08
too short
Pre-scan script results:
| broadcast-igmp-discovery: 
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 224.0.0.252
|     Description: Link-local Multicast Name Resolution (rfc4795)
|   192.168.92.1
|     Interface: eth0
|     Version: 2
|     Group: 239.255.255.250
|     Description: Organization-Local Scope (rfc2365)
|_  Use the newtargets script-arg to add the results as targets
| ipv6-multicast-mld-list: 
|   fe80::b041:cdc8:aed5:1dee: 
|     device: eth0
|     mac: 00:50:56:c0:00:08
|     multicast_ips: 
|       ff02::1:ffd5:1dee         (NDP Solicited-node)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:ffac:ffe9         (Solicited-Node Address)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:ffac:ffe9         (Solicited-Node Address)
|       ff02::fb                  (mDNSv6)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::c                   (SSDP)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|_      ff02::1:3                 (Link-local Multicast Name Resolution)
| targets-asn: 
|_  targets-asn.asn is a mandatory parameter
| targets-ipv6-multicast-mld: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
| 
|_  Use --script-args=newtargets to add the results as targets
| targets-ipv6-multicast-slaac: 
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|   IP: fe80::e918:296:b2ac:ffe9   MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(27, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:58360 > 127.0.0.1:8082 S ttl=128 id=0 iplen=0  seq=72367593 win=3072 <mss 1460>
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000039s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE SERVICE       VERSION
8082/tcp open  http          H2 database http console
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-chrono: Request times for /; avg: 22164.57ms; min: 22150.29ms; max: 22181.06ms
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=localhost
|     
|     Path: http://localhost:8082/
|     Line number: 2
|     Comment: 
|         <!--
|         Copyright 2004-2014 H2 Group. Multiple-Licensed under the MPL 2.0,
|         and the EPL 1.0 (http://h2database.com/html/license.html).
|         Initial Developer: H2 Group
|         -->
|     
|     Path: http://localhost:8082/stylesheet.css
|     Line number: 1
|     Comment: 
|         /*
|          * Copyright 2004-2014 H2 Group. Multiple-Licensed under the MPL 2.0,
|          * and the EPL 1.0 (http://h2database.com/html/license.html).
|          * * Initial Developer: H2 Group
|_         */
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-errors: Couldn't find any error pages.
|_http-feed: Couldn't find any feeds.
| http-headers: 
|   Content-Type: text/html
|   Cache-Control: no-cache
|   Content-Length: 937
|   
|_  (Request type: GET)
|_http-mobileversion-checker: No mobile version detected.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; css: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1; css: 1
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-title: H2 Console
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
| http-vhosts: 
|_127 names had status ERROR
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-xssed: No previously reported XSS vuln.
9092/tcp open  XmlIpcRegSvc?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9092-TCP:V=7.80%I=7%D=10/23%Time=5F92F0E4%P=x86_64-pc-linux-gnu%r(i
SF:nformix,36A,"\0\0\0\0\0\0\0\x05\x009\x000\x000\x004\x007\0\0\0B\0V\0e\0
SF:r\0s\0i\0o\0n\0\x20\0m\0i\0s\0m\0a\0t\0c\0h\0,\0\x20\0d\0r\0i\0v\0e\0r\
SF:0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x20\0\"\x000\0\"\0\x20\0b\0u\0
SF:t\0\x20\0s\0e\0r\0v\0e\0r\0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x20\
SF:0\"\x001\x006\0\"\xff\xff\xff\xff\0\x01_\xbf\0\0\x01b\0o\0r\0g\0\.\0h\x
SF:002\0\.\0j\0d\0b\0c\0\.\0J\0d\0b\0c\0S\0Q\0L\0E\0x\0c\0e\0p\0t\0i\0o\0n
SF:\0:\0\x20\0V\0e\0r\0s\0i\0o\0n\0\x20\0m\0i\0s\0m\0a\0t\0c\0h\0,\0\x20\0
SF:d\0r\0i\0v\0e\0r\0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x20\0\"\x000\
SF:0\"\0\x20\0b\0u\0t\0\x20\0s\0e\0r\0v\0e\0r\0\x20\0v\0e\0r\0s\0i\0o\0n\0
SF:\x20\0i\0s\0\x20\0\"\x001\x006\0\"\0\x20\0\[\x009\x000\x000\x004\x007\0
SF:-\x001\x009\x006\0\]\0\n\0\t\0a\0t\0\x20\0o\0r\0g\0\.\0h\x002\0\.\0m\0e
SF:\0s\0s\0a\0g\0e\0\.\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0g\0e\0t\0J\0d
SF:\0b\0c\0S\0Q\0L\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\(\0D\0b\0E\0x\0c\0e\0p\0t\
SF:0i\0o\0n\0\.\0j\0a\0v\0a\0:\x003\x004\x005\0\)\0\n\0\t\0a\0t\0\x20\0o\0
SF:r\0g\0\.\0h\x002\0\.\0m\0e\0s\0s\0a\0g\0e\0\.\0D\0b\0E\0x\0c\0e\0p\0t\0
SF:i\0o\0n\0\.\0g\0e\0t\0\(\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0j\0a\0v\
SF:0a\0:\x001\x007\x009\0\)\0\n\0\t\0a\0t\0\x20\0o\0r\0g\0\.\0h\x002\0\.\0
SF:s\0e\0r\0v\0e\0r\0\.\0T\0c\0p\0S\0e\0r\0v\0e\0r\0T\0h\0r\0e\0a\0d\0\.\0
SF:r\0u\0n\0\(\0T\0c\0p\0S\0e\0r\0v\0e\0r\0T\0h\0r\0e\0a\0d\0\.\0j\0a\0v\0
SF:a\0:\x008\x009\0\)\0\n\0\t\0a\0t\0\x20\0j\0a\0v\0a\0\.\0b\0a\0s\0e\0/\0
SF:j\0a\0v\0a\0\.\0l\0a\0n\0g\0\.\0T\0h\0r\0e\0a\0d\0\.\0r\0u\0n\0\(\0T\0h
SF:\0r\0e\0a\0d\0\.\0j\0a\0v\0a\0:\x008\x004\x004\0\)\0\n")%r(drda,36A,"\0
SF:\0\0\0\0\0\0\x05\x009\x000\x000\x004\x007\0\0\0B\0V\0e\0r\0s\0i\0o\0n\0
SF:\x20\0m\0i\0s\0m\0a\0t\0c\0h\0,\0\x20\0d\0r\0i\0v\0e\0r\0\x20\0v\0e\0r\
SF:0s\0i\0o\0n\0\x20\0i\0s\0\x20\0\"\x000\0\"\0\x20\0b\0u\0t\0\x20\0s\0e\0
SF:r\0v\0e\0r\0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x20\0\"\x001\x006\0
SF:\"\xff\xff\xff\xff\0\x01_\xbf\0\0\x01b\0o\0r\0g\0\.\0h\x002\0\.\0j\0d\0
SF:b\0c\0\.\0J\0d\0b\0c\0S\0Q\0L\0E\0x\0c\0e\0p\0t\0i\0o\0n\0:\0\x20\0V\0e
SF:\0r\0s\0i\0o\0n\0\x20\0m\0i\0s\0m\0a\0t\0c\0h\0,\0\x20\0d\0r\0i\0v\0e\0
SF:r\0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x20\0\"\x000\0\"\0\x20\0b\0u
SF:\0t\0\x20\0s\0e\0r\0v\0e\0r\0\x20\0v\0e\0r\0s\0i\0o\0n\0\x20\0i\0s\0\x2
SF:0\0\"\x001\x006\0\"\0\x20\0\[\x009\x000\x000\x004\x007\0-\x001\x009\x00
SF:6\0\]\0\n\0\t\0a\0t\0\x20\0o\0r\0g\0\.\0h\x002\0\.\0m\0e\0s\0s\0a\0g\0e
SF:\0\.\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0g\0e\0t\0J\0d\0b\0c\0S\0Q\0L
SF:\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\(\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0j
SF:\0a\0v\0a\0:\x003\x004\x005\0\)\0\n\0\t\0a\0t\0\x20\0o\0r\0g\0\.\0h\x00
SF:2\0\.\0m\0e\0s\0s\0a\0g\0e\0\.\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0g\
SF:0e\0t\0\(\0D\0b\0E\0x\0c\0e\0p\0t\0i\0o\0n\0\.\0j\0a\0v\0a\0:\x001\x007
SF:\x009\0\)\0\n\0\t\0a\0t\0\x20\0o\0r\0g\0\.\0h\x002\0\.\0s\0e\0r\0v\0e\0
SF:r\0\.\0T\0c\0p\0S\0e\0r\0v\0e\0r\0T\0h\0r\0e\0a\0d\0\.\0r\0u\0n\0\(\0T\
SF:0c\0p\0S\0e\0r\0v\0e\0r\0T\0h\0r\0e\0a\0d\0\.\0j\0a\0v\0a\0:\x008\x009\
SF:0\)\0\n\0\t\0a\0t\0\x20\0j\0a\0v\0a\0\.\0b\0a\0s\0e\0/\0j\0a\0v\0a\0\.\
SF:0l\0a\0n\0g\0\.\0T\0h\0r\0e\0a\0d\0\.\0r\0u\0n\0\(\0T\0h\0r\0e\0a\0d\0\
SF:.\0j\0a\0v\0a\0:\x008\x004\x004\0\)\0\n");

Host script results:
|_dns-brute: Can't guess domain of "localhost"; use dns-brute.domain script argument.
|_fcrdns: PASS (localhost)
| hostmap-crtsh: 
|_  subdomains: Error: could not GET http://crt.sh/?q=%.localhost&output=json
|_ipidseq: ERROR: Script execution failed (use -d to debug)
|_path-mtu: 65535 <= PMTU < 65536
|_qscan: ERROR: Script execution failed (use -d to debug)
| resolveall: 
|   Host 'localhost' also resolves to:
|   Use the 'newtargets' script-arg to add the results as targets
|_  Use the --resolve-all option to scan all resolved addresses without using this script.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 541.20 seconds
```