# Enumerating AD with Bloodhound

To ingest the data, first we [use SharpHound.ps1](https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors).

```text
*Evil-WinRM* PS C:\Users\svc-print\Downloads> Set-ExecutionPolicy Bypass -Scope process -Force
*Evil-WinRM* PS C:\Users\svc-print\Downloads> Import-Module C:\Users\svc-print\Downloads\SharpHound.ps1
*Evil-WinRM* PS C:\Users\svc-print\Downloads> Invoke-Bloodhound -CollectionMethod All -Domain fabricorp.local -LDAPUser "svc-print" -LDAPPass '$fab@s3Rv1ce$1'
*Evil-WinRM* PS C:\Users\svc-print\Downloads> dir -Force


    Directory: C:\Users\svc-print\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/19/2021   6:06 AM           9519 20210119060559_BloodHound.zip
-a----        1/19/2021   6:01 AM         973221 SharpHound.ps1
-a----        1/19/2021   6:06 AM          12601 ZGQ3NWM5ZTEtNzZhYy00NzYxLWFjNjEtOWE2NGE0ODc5YmRm.bin

*Evil-WinRM* PS C:\Users\svc-print\Downloads> Get-FileHash 20210119060559_BloodHound.zip

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          B0C329CA70EF5B71ABE4D1025E0E168E0C25A5778264007148338791C70A6BEB       C:\Users\svc-print\Downloads\20210119060559_BloodHound.zip
root@kali:~/CTF/HTB/Fuse/PE# sha256sum 20210119060559_BloodHound.zip
b0c329ca70ef5b71abe4d1025e0e168e0c25a5778264007148338791c70a6beb  20210119060559_BloodHound.zip
```

Note as above I used Powershell's Get-FileHash to generate the file checksums to ensure the files are copied over properly. On Kali we see there're 6 JSON files in the archive.

```text
root@kali:~/CTF/HTB/Fuse/PE# unzip -l 20210119060559_BloodHound.zip
Archive:  20210119060559_BloodHound.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    77594  2021-01-19 06:06   20210119060559_groups.json
    31693  2021-01-19 06:06   20210119060559_users.json
     3926  2021-01-19 06:06   20210119060559_gpos.json
     1527  2021-01-19 06:06   20210119060559_ous.json
     3200  2021-01-19 06:06   20210119060559_domains.json
     3088  2021-01-19 06:06   20210119060559_computers.json
---------                     -------
   121028                     6 files
```

## Bloodhound

Loading the JSON files into Bloodhound I selected the query **Shortest Paths to Domain Admins from Owned Principals**

![AD_bloodhound](Pics\AD_bloodhound.png)

Only one edge is potentially useful here, Has Session from the computer object to Administrator. Inspecting it we see

> ### Info
>
> The user ADMINISTRATOR@FABRICORP.LOCAL has a session on the computer FUSE.FABRICORP.LOCAL.
>
> When a user authenticates to a computer, they often leave credentials exposed on the system, which can be retrieved through LSASS injection, token manipulation/theft, or injecting into a user's process.
>
> Any user that is an administrator to the system has the capability to retrieve the credential material from memory if it still exists.
>
> Note: A session does not guarantee credential material is present, only possible.

and

> ### Abuse Info
> 
> Password Theft
> 
> When a user has a session on the computer, you may be able to obtain credentials for the user via credential dumping or token impersonation. You must be able to move laterally to the computer, have administrative access on the computer, and the user must have a non-network logon session on the computer.
> 
> Once you have established a Cobalt Strike Beacon, Empire agent, or other implant on the target, you can use mimikatz to dump credentials of the user that has a session on the computer. While running in a high integrity process with SeDebugPrivilege, execute one or more of mimikatz's credential gathering techniques (e.g.: sekurlsa::wdigest, sekurlsa::logonpasswords, etc.), then parse or investigate the output to find clear-text credentials for other users logged onto the system.
> 
> You may also gather credentials when a user types them or copies them to their clipboard! Several keylogging capabilities exist, several agents and toolsets have them built-in. For instance, you may use meterpreter's "keyscan_start" command to start keylogging a user, then "keyscan_dump" to return the captured keystrokes. Or, you may use PowerSploit's Invoke-ClipboardMonitor to periodically gather the contents of the user's clipboard.
> 
> Token Impersonation
> 
> You may run into a situation where a user is logged onto the system, but you can't gather that user's credential. This may be caused by a host-based security product, lsass protection, etc. In those circumstances, you may abuse Windows' token model in several ways. First, you may inject your agent into that user's process, which will give you a process token as that user, which you can then use to authenticate to other systems on the network. Or, you may steal a process token from a remote process and start a thread in your agent's process with that user's token. For more information about token abuses, see the References tab.
> 
> User sessions can be short lived and only represent the sessions that were present at the time of collection. A user may have ended their session by the time you move to the computer to target them. However, users tend to use the same machines, such as the workstations or servers they are assigned to use for their job duties, so it can be valuable to check multiple times if a user session has started.

It doesn't look like we can hijack that session though nor steal the token since we aren't admin.