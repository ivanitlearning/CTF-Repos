# Investigating listening ports on localhost

linpeas tells us 8888 and 9000 are listening on localhost

```text
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:9000          0.0.0.0:*               LISTEN      -
tcp        0    372 10.10.10.87:8888        10.10.14.78:60796       ESTABLISHED -
tcp        0      0 :::80                   :::*                    LISTEN      -
tcp        0      0 :::22                   :::*                    LISTEN      -
tcp        0      0 :::8888                 :::*                    LISTEN      -
udp        0      0 10.10.10.87:34823       10.10.10.2:53           ESTABLISHED -
```

So I forwarded back to Kali and ran an nmap scan on them

```shell
waldo:~$ ssh -f -N -R 8888:127.0.0.1:8888 root@10.10.14.78 -p 22022
root@10.10.14.78's password:
waldo:~$ ssh -f -N -R 9000:127.0.0.1:9000 root@10.10.14.78 -p 22022
root@10.10.14.78's password:


root@Kali:~/HTB/Waldo# nmap -Pn -n -sV -p8888,9000 --script=vuln,discovery localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-22 01:59 +08
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
|       ff02::1:ff57:1a59         (Solicited-Node Address)
|       ff02::1:ff57:1a59         (Solicited-Node Address)
|       ff02::fb                  (mDNSv6)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::1:3                 (Link-local Multicast Name Resolution)
|       ff02::c                   (SSDP)
|_      ff02::1:3                 (Link-local Multicast Name Resolution)
| targets-asn:
|_  targets-asn.asn is a mandatory parameter
| targets-ipv6-multicast-mld:
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|
|_  Use --script-args=newtargets to add the results as targets
| targets-ipv6-multicast-slaac:
|   IP: fe80::b041:cdc8:aed5:1dee  MAC: 00:50:56:c0:00:08  IFACE: eth0
|   IP: fe80::786e:5c42:557:1a59   MAC: 00:50:56:c0:00:08  IFACE: eth0
|_  Use --script-args=newtargets to add the results as targets
sendto in send_ip_packet_sd: sendto(15, packet, 65536, 0, 127.0.0.1, 16) => Message too long
Offending packet: TCP 127.0.0.1:19236 > 127.0.0.1:8888 S ttl=128 id=0 iplen=0  seq=527652093 win=3072 <mss 1460>
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000046s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE SERVICE         VERSION
8888/tcp open  sun-answerbook?
9000/tcp open  cslistener?

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
|_qscan: ERROR: Script execution failed (use -d to debug)
| resolveall:
|   Host 'localhost' also resolves to:
|   Use the 'newtargets' script-arg to add the results as targets
|_  Use the --resolve-all option to scan all resolved addresses without using this script.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 189.89 seconds
```

But this told us nothing.