# command_output folder on /mnt/forensic

I briefly looked through the files and found nothing notable

```text
root@kali:/mnt/forensic/commands_output# ls -lah
total 573K
drwxr-xr-x 2 root root 4.0K Feb 24  2020 .
drwxr-xr-x 2 root root 4.0K Feb 23  2020 ..
-rwxr-xr-x 1 root root  528 Feb 23  2020 domain_admins.txt
-rwxr-xr-x 1 root root  962 Feb 23  2020 domain_groups.txt
-rwxr-xr-x 1 root root  17K Feb 29  2020 domain_users.txt
-rwxr-xr-x 1 root root 507K Feb 23  2020 firewall_rules.txt
-rwxr-xr-x 1 root root 1.8K Feb 23  2020 ipconfig.txt
-rwxr-xr-x 1 root root 3.8K Feb 23  2020 netstat.txt
-rwxr-xr-x 1 root root 3.9K Feb 23  2020 route.txt
-rwxr-xr-x 1 root root 4.5K Feb 23  2020 systeminfo.txt
-rwxr-xr-x 1 root root 9.8K Feb 23  2020 tasklist.txt
root@kali:/mnt/forensic/commands_output# cat domain_admins.txt
▒▒Group name     Domain Admins
Comment        Designated administrators of the domain

Members

-------------------------------------------------------------------------------
Administrator       Ipwn3dYourCompany
The command completed successfully.

root@kali:/mnt/forensic/commands_output# cat domain_groups.txt
▒▒
Group Accounts for \\DC01

-------------------------------------------------------------------------------
*Cloneable Domain Controllers
*DnsUpdateProxy
*Domain Admins
*Domain Computers
*Domain Controllers
*Domain Guests
*Domain Users
*Enterprise Admins
*Enterprise Key Admins
*Enterprise Read-only Domain Controllers
*Group Policy Creator Owners
*Key Admins
*Protected Users
*Read-only Domain Controllers
*Schema Admins
The command completed successfully.
root@kali:/mnt/forensic/commands_output# cat netstat.txt
▒▒
Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    127.0.0.1:389          DC01:49679             ESTABLISHED
  TCP    127.0.0.1:389          DC01:49681             ESTABLISHED
  TCP    127.0.0.1:389          DC01:49698             ESTABLISHED
  TCP    127.0.0.1:389          DC01:51060             ESTABLISHED
  TCP    127.0.0.1:389          DC01:51125             ESTABLISHED
  TCP    127.0.0.1:49679        DC01:ldap              ESTABLISHED
  TCP    127.0.0.1:49681        DC01:ldap              ESTABLISHED
  TCP    127.0.0.1:49698        DC01:ldap              ESTABLISHED
  TCP    127.0.0.1:51060        DC01:ldap              ESTABLISHED
  TCP    127.0.0.1:51125        DC01:ldap              ESTABLISHED
  TCP    192.168.86.156:389     DC01:51016             ESTABLISHED
  TCP    192.168.86.156:389     DC01:60961             ESTABLISHED
  TCP    192.168.86.156:389     DC01:60987             ESTABLISHED
  TCP    192.168.86.156:389     DC01:60993             ESTABLISHED
  TCP    192.168.86.156:51016   DC01:ldap              ESTABLISHED
  TCP    192.168.86.156:60961   DC01:ldap              ESTABLISHED
  TCP    192.168.86.156:60987   DC01:ldap              ESTABLISHED
  TCP    192.168.86.156:60993   DC01:ldap              ESTABLISHED
  TCP    192.168.86.156:63810   40.67.251.132:https    ESTABLISHED
  TCP    192.168.86.156:63830   40.67.251.132:https    ESTABLISHED
  TCP    [::1]:49667            DC01:60989             ESTABLISHED
  TCP    [::1]:49667            DC01:63777             ESTABLISHED
  TCP    [::1]:49667            DC01:63836             ESTABLISHED
  TCP    [::1]:51178            DC01:epmap             TIME_WAIT
  TCP    [::1]:60989            DC01:49667             ESTABLISHED
  TCP    [::1]:63777            DC01:49667             ESTABLISHED
  TCP    [::1]:63836            DC01:49667             ESTABLISHED
root@kali:/mnt/forensic/commands_output# cat tasklist.txt
▒▒
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0        144 K
Registry                        68 Services                   0     60,316 K
smss.exe                       244 Services                   0          8 K
csrss.exe                      340 Services                   0        456 K
csrss.exe                      412 Console                    1      1,420 K
wininit.exe                    420 Services                   0         12 K
winlogon.exe                   468 Console                    1      1,160 K
services.exe                   532 Services                   0      4,348 K
lsass.exe                      540 Services                   0     39,144 K
svchost.exe                    724 Services                   0      7,772 K
svchost.exe                    756 Services                   0      6,688 K
dwm.exe                        848 Console                    1     41,360 K
svchost.exe                    920 Services                   0      3,248 K
svchost.exe                    928 Services                   0     27,548 K
svchost.exe                    948 Services                   0      5,392 K
svchost.exe                    968 Services                   0        432 K
svchost.exe                    996 Services                   0      4,704 K
svchost.exe                   1012 Services                   0     12,196 K
svchost.exe                    332 Services                   0      8,136 K
svchost.exe                   1036 Services                   0      4,632 K
svchost.exe                   1220 Services                   0        156 K
svchost.exe                   1272 Services                   0      1,300 K
svchost.exe                   1800 Services                   0      1,084 K
svchost.exe                   1952 Services                   0      3,108 K
fontdrvhost.exe               2036 Console                    1      1,528 K
fontdrvhost.exe               2044 Services                   0         16 K
spoolsv.exe                    876 Services                   0         16 K
svchost.exe                    836 Services                   0      2,860 K
Microsoft.ActiveDirectory     1412 Services                   0     30,740 K
svchost.exe                   1600 Services                   0     12,300 K
dfsrs.exe                     1708 Services                   0      9,652 K
dns.exe                       1796 Services                   0      4,576 K
ismserv.exe                   1496 Services                   0      1,576 K
dfssvc.exe                     568 Services                   0      2,008 K
MsMpEng.exe                   2076 Services                   0     55,692 K
wlms.exe                      2088 Services                   0      1,532 K
msdtc.exe                     1676 Services                   0         16 K
svchost.exe                   1868 Services                   0      3,428 K
svchost.exe                   2480 Services                   0      6,136 K
sihost.exe                    3464 Console                    1      3,592 K
svchost.exe                   3472 Console                    1      2,328 K
taskhostw.exe                 3548 Console                    1      3,916 K
ctfmon.exe                    3756 Console                    1      4,540 K
explorer.exe                  3936 Console                    1     33,528 K
ShellExperienceHost.exe       3688 Console                    1         16 K
SearchUI.exe                  3156 Console                    1         16 K
RuntimeBroker.exe             4184 Console                    1        264 K
RuntimeBroker.exe             4256 Console                    1      4,856 K
ServerManager.exe             4332 Console                    1     63,888 K
RuntimeBroker.exe             4616 Console                    1        556 K
smartscreen.exe               4780 Console                    1      1,888 K
dllhost.exe                    892 Console                    1      1,560 K
NisSrv.exe                    2692 Services                   0      1,240 K
powershell.exe                1988 Console                    1      2,092 K
conhost.exe                   4284 Console                    1      2,104 K
taskhostw.exe                 5064 Console                    1      2,872 K
mmc.exe                       2456 Console                    1     23,536 K
powershell.exe                1732 Console                    1    115,336 K
conhost.exe                   4432 Console                    1      8,072 K
WmiPrvSE.exe                  3404 Services                   0     15,288 K
tasklist.exe                  3092 Console                    1      7,464 K
root@kali:/mnt/forensic/commands_output# cat route.txt
▒▒===========================================================================
Interface List
  3...08 00 27 f3 dc 8d ......Intel(R) PRO/1000 MT Desktop Adapter
  1...........................Software Loopback Interface 1
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0     192.168.86.1   192.168.86.156    281
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    331
     192.168.86.0    255.255.255.0         On-link    192.168.86.156    281
   192.168.86.156  255.255.255.255         On-link    192.168.86.156    281
   192.168.86.255  255.255.255.255         On-link    192.168.86.156    281
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    331
        224.0.0.0        240.0.0.0         On-link    192.168.86.156    281
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    331
  255.255.255.255  255.255.255.255         On-link    192.168.86.156    281
===========================================================================
Persistent Routes:
  Network Address          Netmask  Gateway Address  Metric
          0.0.0.0          0.0.0.0     192.168.86.1  Default
===========================================================================

IPv6 Route Table
===========================================================================
Active Routes:
 If Metric Network Destination      Gateway
  1    331 ::1/128                  On-link
  1    331 ff00::/8                 On-link
===========================================================================
Persistent Routes:
  None
```

firewall rules were really long so I omitted that.