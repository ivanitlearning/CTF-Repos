# SMB share enumeration for tlavel

I had to change passwords because some script on the box was resetting it.

```text
root@kali:~/CTF/HTB/Fuse# smbclient -U 'tlavel'%'Password1' -L \\\\10.10.10.193

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        HP-MFT01        Printer   HP-MFT01
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        print$          Disk      Printer Drivers
        SYSVOL          Disk      Logon server share
SMB1 disabled -- no workgroup available
```

smbmap

```text
root@kali:~/CTF/HTB/Fuse# smbmap -u tlavel -p Password3 -d fabricorp.local -H 10.10.10.193
[+] Finding open SMB ports....
[+] User SMB session established on 10.10.10.193...
[+] IP: 10.10.10.193:445        Name: fuse.fabricorp.local
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        HP-MFT01                                                NO ACCESS       HP-MFT01
        .
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    InitShutdown
        fr--r--r--                6 Mon Jan  1 06:55:25 1601    lsass
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    ntsvcs
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    scerpc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-36c-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    epmapper
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-1e8-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    LSM_API_service
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    eventlog
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-3cc-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    atsvc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-11c-0
        fr--r--r--                4 Mon Jan  1 06:55:25 1601    wkssvc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-278-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-278-1
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    RpcProxy\49675
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    6e3822d184e0cef7
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    RpcProxy\593
        fr--r--r--                4 Mon Jan  1 06:55:25 1601    srvsvc
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    spoolss
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-428-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    efsrpc
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    netdfs
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    vgauth-service
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-270-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    W32TIME_ALT
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-814-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-834-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    HPUPDMon
        IPC$                                                    READ ONLY       Remote IPC
        .
        dr--r--r--                0 Sat May 30 07:29:21 2020    .
        dr--r--r--                0 Sat May 30 07:29:21 2020    ..
        NETLOGON                                                READ ONLY       Logon server share
        .
        dr--r--r--                0 Sat May 30 08:12:41 2020    .
        dr--r--r--                0 Sat May 30 08:12:41 2020    ..
        dr--r--r--                0 Wed May 27 14:34:48 2020    color
        dr--r--r--                0 Sat May 30 08:12:41 2020    IA64
        dr--r--r--                0 Mon Jun  1 17:03:44 2020    W32X86
        dr--r--r--                0 Mon Jun  1 17:03:46 2020    x64
        print$                                                  READ ONLY       Printer Drivers
        .
        dr--r--r--                0 Sat May 30 07:29:21 2020    .
        dr--r--r--                0 Sat May 30 07:29:21 2020    ..
        dr--r--r--                0 Sat May 30 07:29:21 2020    fabricorp.local
        SYSVOL                                                  READ ONLY       Logon server share
```

Checking the print$ share

```text
root@kali:~/CTF/HTB/Fuse# smbclient -U 'fabricorp.local\\tlavel'%'Password5' "\\\\10.10.10.193\\print$"
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat May 30 08:12:41 2020
  ..                                  D        0  Sat May 30 08:12:41 2020
  color                               D        0  Sat Jul 16 21:18:08 2016
  IA64                                D        0  Sat May 30 08:12:41 2020
  W32X86                              D        0  Mon Jun  1 17:03:44 2020
  x64                                 D        0  Mon Jun  1 17:03:46 2020

                10340607 blocks of size 4096. 6870309 blocks available
smb: \>
```

We have no write access

```text
smb: \color\> put test.txt
NT_STATUS_ACCESS_DENIED opening remote file \color\test.txt

smb: \color\> ls
  .                                   D        0  Sat Jul 16 21:18:08 2016
  ..                                  D        0  Sat Jul 16 21:18:08 2016
  D50.camp                            A     1058  Sat Jul 16 21:12:09 2016
  D65.camp                            A     1079  Sat Jul 16 21:12:09 2016
  Graphics.gmmp                       A      797  Sat Jul 16 21:12:09 2016
  MediaSim.gmmp                       A      838  Sat Jul 16 21:12:09 2016
  Photo.gmmp                          A      786  Sat Jul 16 21:12:09 2016
  Proofing.gmmp                       A      822  Sat Jul 16 21:12:09 2016
  RSWOP.icm                           A   218103  Sat Jul 16 21:12:09 2016
  sRGB Color Space Profile.icm        A     3144  Sat Jul 16 21:12:09 2016
  wscRGB.cdmp                         A    17155  Sat Jul 16 21:12:09 2016
  wsRGB.cdmp                          A     1578  Sat Jul 16 21:12:09 2016

                10340607 blocks of size 4096. 6870227 blocks available
```

After a while I decided to mount it instead.

```text
root@kali:~/CTF/HTB/Fuse# mount -t cifs "//10.10.10.193/print$" -o username=tlavel,password=Password6,domain="fabricorp.local" /mnt/tlavel/print
root@kali:~/CTF/HTB/Fuse# ls -lah /mnt/tlavel/print/
total 4.0K
drwxr-xr-x 2 root root    0 May 30  2020 .
drwxr-xr-x 3 root root 4.0K Jan 19 20:22 ..
drwxr-xr-x 2 root root    0 Jul 16  2016 color
drwxr-xr-x 2 root root    0 May 30  2020 IA64
drwxr-xr-x 2 root root    0 Jun  1  2020 W32X86
drwxr-xr-x 2 root root    0 Jun  1  2020 x64

root@kali:/mnt/tlavel/print# tree -L 8
.
├── color
│   ├── D50.camp
│   ├── D65.camp
│   ├── Graphics.gmmp
│   ├── MediaSim.gmmp
│   ├── Photo.gmmp
│   ├── Proofing.gmmp
│   ├── RSWOP.icm
│   ├── sRGB Color Space Profile.icm
│   ├── wscRGB.cdmp
│   └── wsRGB.cdmp
├── IA64
├── W32X86
│   ├── 3
│   │   ├── mxdwdrv.dll
│   │   ├── PrintConfig.dll
│   │   ├── unishare.gpd
│   │   └── unishare-pipelineconfig.xml
│   ├── {BB95B51E-0165-449F-A3A9-41764F5FD934}
│   │   └── PrintConfig.dll
│   └── PCC
│       ├── ntprint.inf_x86_dcef07064d319714.cab
│       └── prnms003.inf_x86_613ce7e3b2821cb8.cab
└── x64
    ├── 3
    │   ├── cioum64.msi
    │   ├── cioum.dll
    │   ├── en-US
    │   │   ├── PCL4RES.DLL.mui
    │   │   ├── PCL5ERES.DLL.mui
    │   │   ├── PCL5URES.DLL.mui
    │   │   ├── PCLXL.DLL.mui
    │   │   ├── PrintConfig.dll.mui
    │   │   ├── PS5UI.DLL.mui
    │   │   ├── PSCRIPT5.DLL.mui
    │   │   ├── UNIDRVUI.DLL.mui
    │   │   └── UNIRES.DLL.mui
    │   ├── FxCompChannel_x64.dll
    │   ├── hpbcfgre.dll
    │   ├── hpbdrvjct1004.dll
    │   ├── hpbuio64.dll
    │   ├── hpbuiodm64.dll
    │   ├── hpc6m240.gpd
    │   ├── hpc6r240.dll
    │   ├── hpcc6240.dll
    │   ├── hpcdmc64.dll
    │   ├── hpcev240.dll
    │   ├── hpchl240.cab
    │   ├── hpcls240.dll
    │   ├── hpcpe240.dll
    │   ├── hpcpn240.dll
    │   ├── hpcpp240.dll
    │   ├── hpcpu240.cfg
    │   ├── hpcsat20.dll
    │   ├── hpcsc240.dtd
    │   ├── hpcsm240.gpd
    │   ├── hpcss240.dll
    │   ├── hpcst240.dll
    │   ├── hpcu2406.BUD
    │   ├── hpcu2406dm.xml
    │   ├── hpcu2406.gpd
    │   ├── hpcu2406.hpx
    │   ├── hpcu2406SPS.xml
    │   ├── hpcu2406.xml
    │   ├── hpcu240.dem
    │   ├── hpcu240u.ini
    │   ├── hpcui240.dll
    │   ├── hpcur240.dll
    │   ├── hpfie240.dll
    │   ├── hpfxcomw.dll
    │   ├── hpmdp240.dll
    │   ├── hpmpm082.dll
    │   ├── hpmpw082.dll
    │   ├── hpmsl240.dll
    │   ├── hpmur240.dll
    │   ├── hpmux240.dll
    │   ├── hppdcompio.dll
    │   ├── HPSecurePrint64.dll
    │   ├── hpspw240.dll
    │   ├── hpsysobj.dll
    │   ├── LOCALE.GPD
    │   ├── MSXPSINC.GPD
    │   ├── MSXPSINC.PPD
    │   ├── mui
    │   │   └── 0409
    │   │       ├── PSCRIPT.HLP
    │   │       └── UNIDRV.HLP
    │   ├── MXDWDRV.DLL
    │   ├── P6DISP.GPD
    │   ├── P6FONT.GPD
    │   ├── PCL4RES.DLL
    │   ├── PCL5ERES.DLL
    │   ├── PCL5URES.DLL
    │   ├── pclxl.DLL
    │   ├── pclxl.gpd
    │   ├── pjl.gpd
    │   ├── PJLMON.DLL
    │   ├── PrintConfig.dll
    │   ├── PS5UI.DLL
    │   ├── PSCRIPT5.DLL
    │   ├── PSCRIPT.HLP
    │   ├── PSCRIPT.NTF
    │   ├── PSCRPTFE.NTF
    │   ├── PS_SCHM.GDL
    │   ├── stddtype.gdl
    │   ├── stdnames.gpd
    │   ├── stdschem.gdl
    │   ├── stdschmx.gdl
    │   ├── TTFSUB.GPD
    │   ├── unidrv.dll
    │   ├── unidrv.hlp
    │   ├── unidrvui.dll
    │   ├── unires.dll
    │   ├── unishare.gpd
    │   └── unishare-pipelineconfig.xml
    ├── {A93D2C7C-3D97-464A-8A68-C4378572B2A8}
    │   └── PrintConfig.dll
    ├── {AFE7B823-9022-4115-8EF7-E23779245CB9}
    │   └── PrintConfig.dll
    └── PCC
        ├── hpcu240u.inf_amd64_ddac10eb3da45aeb.cab
        ├── ntprint.inf_amd64_dcef07064d319714.cab
        ├── prnms001.inf_amd64_10bd6dee10a7dfd0.cab
        ├── prnms003.inf_amd64_9f9e8613fb51c32e.cab
        └── prnms009.inf_amd64_bd3f6a64dee1535d.cab

14 directories, 111 files
```

There was nothing in the LOGON share

```text
root@kali:~/CTF/HTB/Fuse# mount -t cifs "//10.10.10.193/NETLOGON" -o username=tlavel,password=Password7,domain="fabricorp.local" /mnt/tlavel/NETLOGON
root@kali:~/CTF/HTB/Fuse# ls -lah /mnt/tlavel/NETLOGON/
total 4.0K
drwxr-xr-x 2 root root    0 May 30  2020 .
drwxr-xr-x 4 root root 4.0K Jan 19 20:33 ..
```

There was something in SYSVOL

```text
root@kali:~/CTF/HTB/Fuse# mount -t cifs "//10.10.10.193/SYSVOL" -o username=tlavel,password=Password8,domain="fabricorp.local" /mnt/tlavel/SYSVOL

root@kali:~/CTF/HTB/Fuse# tree -L 9 /mnt/tlavel/SYSVOL
/mnt/tlavel/SYSVOL
└── fabricorp.local
    ├── Policies
    │   ├── {31B2F340-016D-11D2-945F-00C04FB984F9}
    │   │   ├── GPT.INI
    │   │   ├── MACHINE
    │   │   │   └── Microsoft
    │   │   │       └── Windows NT
    │   │   │           └── SecEdit
    │   │   │               └── GptTmpl.inf
    │   │   └── USER
    │   └── {6AC1786C-016F-11D2-945F-00C04fB984F9}
    │       ├── GPT.INI
    │       ├── MACHINE
    │       │   └── Microsoft
    │       │       └── Windows NT
    │       │           └── SecEdit
    │       │               └── GptTmpl.inf
    │       └── USER
    └── scripts

15 directories, 4 files
```

But checking those out I found nothing useful

```text
root@kali:/mnt/tlavel/SYSVOL/fabricorp.local/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit# cat GptTmpl.inf
▒▒[Unicode]
Unicode=yes
[System Access]
MinimumPasswordAge = 1
MaximumPasswordAge = 42
MinimumPasswordLength = 7
PasswordComplexity = 1
PasswordHistorySize = 24
LockoutBadCount = 0
RequireLogonToChangePassword = 0
ForceLogoffWhenHourExpire = 0
ClearTextPassword = 0
LSAAnonymousNameLookup = 0
[Kerberos Policy]
MaxTicketAge = 10
MaxRenewAge = 7
MaxServiceAge = 600
MaxClockSkew = 5
TicketValidateClient = 1
[Registry Values]
MACHINE\System\CurrentControlSet\Control\Lsa\NoLMHash=4,1
[Version]
signature="$CHICAGO$"
Revision=1

root@kali:/mnt/tlavel/SYSVOL# cat fabricorp.local/Policies/\{6AC1786C-016F-11D2-945F-00C04fB984F9\}/MACHINE/Microsoft/Windows\ NT/SecEdit/GptTmpl.inf
▒▒[Unicode]
Unicode=yes
[Registry Values]
MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LDAPServerIntegrity=4,1
MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal=4,1
MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1
MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableSecuritySignature=4,1
[Version]
signature="$CHICAGO$"
Revision=1
[Privilege Rights]
SeAssignPrimaryTokenPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-20,*S-1-5-19
SeAuditPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-20,*S-1-5-19
SeBackupPrivilege = *S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544
SeBatchLogonRight = *S-1-5-32-559,*S-1-5-32-551,*S-1-5-32-544,*S-1-5-32-568
SeChangeNotifyPrivilege = *S-1-5-32-554,*S-1-5-11,*S-1-5-32-544,*S-1-5-20,*S-1-5-19,*S-1-1-0
SeCreatePagefilePrivilege = *S-1-5-32-544
SeDebugPrivilege = *S-1-5-32-544
SeIncreaseBasePriorityPrivilege = *S-1-5-32-544
SeIncreaseQuotaPrivilege = *S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415,*S-1-5-32-544,*S-1-5-20,*S-1-5-19
SeInteractiveLogonRight = *S-1-5-9,*S-1-5-32-550,*S-1-5-32-549,*S-1-5-32-548,*S-1-5-32-551,*S-1-5-32-544
SeLoadDriverPrivilege = *S-1-5-32-550,*S-1-5-32-544
SeMachineAccountPrivilege = *S-1-5-11
SeNetworkLogonRight = *S-1-5-32-554,*S-1-5-9,*S-1-5-11,*S-1-5-32-544,*S-1-1-0
SeProfileSingleProcessPrivilege = *S-1-5-32-544
SeRemoteShutdownPrivilege = *S-1-5-32-549,*S-1-5-32-544
SeRestorePrivilege = *S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544
SeSecurityPrivilege = *S-1-5-32-544
SeShutdownPrivilege = *S-1-5-32-550,*S-1-5-32-549,*S-1-5-32-551,*S-1-5-32-544
SeSystemEnvironmentPrivilege = *S-1-5-32-544
SeSystemProfilePrivilege = *S-1-5-80-3139157870-2983391045-3678747466-658725712-1809340420,*S-1-5-32-544
SeSystemTimePrivilege = *S-1-5-32-549,*S-1-5-32-544,*S-1-5-19
SeTakeOwnershipPrivilege = *S-1-5-32-544
SeUndockPrivilege = *S-1-5-32-544
SeEnableDelegationPrivilege = *S-1-5-32-544
```

