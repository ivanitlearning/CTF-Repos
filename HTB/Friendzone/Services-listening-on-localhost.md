# Services listening on localhost

### TCP 953

First forward it back to Kali since we don't have the SSH passwords or keys of our user.

```text
www-data@FriendZone /etc/apache2/sites-available $ netstat -ntlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 10.10.10.123:53         0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -
tcp6       0      0 :::21                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 ::1:25                  :::*                    LISTEN      -
tcp6       0      0 :::443                  :::*                    LISTEN      -
tcp6       0      0 :::445                  :::*                    LISTEN      -
tcp6       0      0 :::139                  :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -

www-data@FriendZone /var/www $ ssh -f -N -R 953:127.0.0.1:953 root@10.10.14.78 -p 22022
Could not create directory '/var/www/.ssh'.
The authenticity of host '[10.10.14.78]:22022 ([10.10.14.78]:22022)' can't be established.
ECDSA key fingerprint is SHA256:HRvXIeB7FuR8syEm3D1KDRx6s3O7n4jJQmXw4ald9PA.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/var/www/.ssh/known_hosts).
root@10.10.14.78's password:
```

Unfortunately nmap tells us nothing about what service is this

```text
root@Kali:~/HTB/Friendzone# nmap -Pn -n -sV -p953 --script=vuln,discovery localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-14 01:26 +08
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
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:ffdb:bed3         (Solicited-Node Address)
|       ff02::1:ffdb:bed3         (Solicited-Node Address)
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
|   IP: fe80::ed99:8ff6:7cdb:bed3  MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(11, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:24232 > 127.0.0.1:953 S ttl=128 id=0 iplen=0  seq=977726649 win=3072 <mss 1460>
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000049s latency).
Other addresses for localhost (not scanned): ::1

PORT    STATE SERVICE VERSION
953/tcp open  rndc?

Host script results:
|_dns-brute: Can't guess domain of "localhost"; use dns-brute.domain script argument.
|_fcrdns: PASS (localhost)
| hostmap-crtsh:
|   subdomains:
|     localhost
|     localhost\nwww.localhost
|     Localhost
|     LOCALHOST
|     naeu2.naeuinc.localhost
|     root@localhost
|     SERVER02.counterintel.localhost
|     fndlync01.5ninesdata.localhost
|     mail.localhost
|     autodiscover.localhost
|     mse-ca-mail.corp.mse.localhost
|     webmail.otto-wulff.local,localhost,owsvex01,owsvex01.otto-wulff.
|     autodiscover.localhost\nlocalhost
|     localhost\nlocalhost.spp.co.nz\nlocalhost.spp.local
|     172.30.2.80 10.1.1.1 gkh-xchng localhost
|     localhost\nlocalhost.polimaster.local
|     server02.counterintel.localhost
|     *.localhost\nlocalhost
|     autodiscover.regency.localhost\nmail02.regency.localhost\nmail03.regency.localhost\nmail.regency.localhost\nowa.regency.localhost
|     sbs.allsaintsschool.localhost
|     server2.hunter.localhost
|     tools.sonoma.edu.localhost
|     ExchVM.nwcnet.localhost
|_    LocalHost
|_ipidseq: ERROR: Script execution failed (use -d to debug)
|_path-mtu: 65535 <= PMTU < 65536
| resolveall:
|   Host 'localhost' also resolves to:
|   Use the 'newtargets' script-arg to add the results as targets
|_  Use the --resolve-all option to scan all resolved addresses without using this script.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.35 seconds
```

