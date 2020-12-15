# DNS enumeration

Try a domain lookup given what we know

```shell
root@kali:~/CTF/HTB/Cascade# nslookup cascade.local 10.10.10.182
Server:         10.10.10.182
Address:        10.10.10.182#53

Name:   cascade.local
Address: 10.10.10.182
Name:   cascade.local
Address: 10.10.10.183
Name:   cascade.local
Address: dead:beef::8a8:d14d:1d23:bbe2

root@kali:~/CTF/HTB/Cascade# nslookup 10.10.10.182 10.10.10.182
** server can't find 182.10.10.10.in-addr.arpa: SERVFAIL
```

Now a zone transfer

```shell
root@kali:~/CTF/HTB/Cascade# host -t axfr cascade.local cascade.local
Trying "cascade.local"
Using domain server:
Name: cascade.local
Address: 10.10.10.182#53
Aliases:

Host cascade.local not found: 5(REFUSED)
; Transfer failed.
```

Lastly check exploits for Microsoft DNS 6.1

```shell
root@kali:~/CTF/HTB/Cascade# searchsploit Microsoft DNS
--------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                 |  Path
--------------------------------------------------------------------------------------------------------------- ---------------------------------
Microsoft DNS RPC Service - 'extractQuotedChar()' Remote Overflow 'SMB' (MS07-029) (Metasploit)                | windows/remote/16366.rb
Microsoft DNS RPC Service - 'extractQuotedChar()' TCP Overflow (MS07-029) (Metasploit)                         | windows/remote/16748.rb
Microsoft DNS Server - Dynamic DNS Update/Change                                                               | windows/remote/3544.c
Microsoft Internet Explorer 5.0.1 - Wildcard DNS Cross-Site Scripting                                          | windows/remote/24213.txt
Microsoft Message Queueing Service - DNS Name Path Overflow (MS07-065) (Metasploit)                            | windows/remote/16750.rb
Microsoft Windows - 'dnslint.exe' Drive-By Download                                                            | windows/remote/45079.txt
Microsoft Windows - DNS DnssrvQuery Remote Stack Overflow                                                      | windows/remote/3740.c
Microsoft Windows - DNS Resolution Remote Denial of Service (PoC) (MS06-041)                                   | windows/dos/2900.py
Microsoft Windows - DNS RPC Remote Buffer Overflow (2)                                                         | windows/remote/3746.txt
Microsoft Windows Server 2000 SP4 - DNS RPC Remote Buffer Overflow                                             | windows/remote/3737.py
Microsoft Windows Server 2000/2003 - Recursive DNS Spoofing (1)                                                | windows/remote/30635.pl
Microsoft Windows Server 2000/2003 - Recursive DNS Spoofing (2)                                                | windows/remote/30636.pl
--------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

I could have tried subdomain enumeration but since this is a DC, I decided against it as the approach may be elsewhere.