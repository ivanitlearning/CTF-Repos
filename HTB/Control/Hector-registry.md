# Enumerating service registry ACLs

Running the commands we see

```text
*Evil-WinRM* PS C:\Temp> Get-Content C:\Users\Hector\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
get-childitem HKLM:\SYSTEM\CurrentControlset | format-list
get-acl HKLM:\SYSTEM\CurrentControlSet | format-list

Running these gave

*Evil-WinRM* PS C:\> get-childitem HKLM:\SYSTEM\CurrentControlset | format-list


Property      : {BootDriverFlags, CurrentUser, EarlyStartServices, PreshutdownOrder...}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Control
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Control
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 121
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 11
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Control

Property      : {NextParentID.daba3ff.2, NextParentID.61aaa01.3, NextParentID.1bd7f811.4, NextParentID.2032e665.5...}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Enum
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Enum
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 17
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 27
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Enum

Property      : {}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Hardware Profiles
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Hardware Profiles
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 3
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 0
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Hardware Profiles

Property      : {}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Policies
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Policies
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 0
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 0
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Policies

Property      : {}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Services
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Services
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 667
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 0
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Services

Property      : {}
PSPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Software
PSParentPath  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset
PSChildName   : Software
PSDrive       : HKLM
PSProvider    : Microsoft.PowerShell.Core\Registry
PSIsContainer : True
SubKeyCount   : 1
View          : Default
Handle        : Microsoft.Win32.SafeHandles.SafeRegistryHandle
ValueCount    : 0
Name          : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Software



*Evil-WinRM* PS C:\> get-acl HKLM:\SYSTEM\CurrentControlSet | format-list


Path   : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet
Owner  : BUILTIN\Administrators
Group  : NT AUTHORITY\SYSTEM
Access : BUILTIN\Administrators Allow  FullControl
         NT AUTHORITY\Authenticated Users Allow  ReadKey
         NT AUTHORITY\Authenticated Users Allow  -2147483648
         S-1-5-32-549 Allow  ReadKey
         S-1-5-32-549 Allow  -2147483648
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadKey
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -2147483648
         S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 Allow  ReadKey
         S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 Allow  -2147483648
Audit  :
Sddl   : O:BAG:SYD:AI(A;;KA;;;BA)(A;ID;KR;;;AU)(A;CIIOID;GR;;;AU)(A;ID;KR;;;SO)(A;CIIOID;GR;;;SO)(A;ID;KA;;;BA)(A;CIIOID;GA;;;BA)(A;ID;KA;;;SY)(A;CIIOID;GA;;;SY)(A;CIIOID;GA;;;CO)(A;ID;KR;;;AC)(A;CIIOID;GR;;;AC)(A;ID;KR;;;S-1-15-3-1024-1065365936-12
         81604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681)(A;CIIOID;GR;;;S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681)
```

This is actually slightly off because we're not concerned here with **HKLM:\SYSTEM\CurrentControlSet** but its childitem **HKLM:\SYSTEM\CurrentControlSet\Services**. Let's first get the ACL of that reg directory

```text
PS C:\Users\Hector> (get-acl HKLM:\SYSTEM\CurrentControlSet\Services) | FL *
(get-acl HKLM:\SYSTEM\CurrentControlSet\Services) | FL *


PSPath                  : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services
PSParentPath            : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet
PSChildName             : Services
PSDrive                 : HKLM
PSProvider              : Microsoft.PowerShell.Core\Registry
CentralAccessPolicyId   :
CentralAccessPolicyName :
Path                    : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services
Owner                   : NT AUTHORITY\SYSTEM
Group                   : NT AUTHORITY\SYSTEM
Access                  : {System.Security.AccessControl.RegistryAccessRule,
                          System.Security.AccessControl.RegistryAccessRule,
                          System.Security.AccessControl.RegistryAccessRule,
                          System.Security.AccessControl.RegistryAccessRule...}
Sddl                    : O:SYG:SYD:PAI(A;CIIO;KA;;;CO)(A;CI;KR;;;AU)(A;CI;KA;;;SY)(A;CI;KA;;;BA)(A;CI;KA;;;S-1-5-21-32
                          71572904-80546332-2170161114-1000)(A;CI;KR;;;AC)
AccessToString          : CREATOR OWNER Allow  FullControl
                          NT AUTHORITY\Authenticated Users Allow  ReadKey
                          NT AUTHORITY\SYSTEM Allow  FullControl
                          BUILTIN\Administrators Allow  FullControl
                          CONTROL\Hector Allow  FullControl
                          APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadKey
AuditToString           :
AccessRightType         : System.Security.AccessControl.RegistryRights
AccessRuleType          : System.Security.AccessControl.RegistryAccessRule
AuditRuleType           : System.Security.AccessControl.RegistryAuditRule
AreAccessRulesProtected : True
AreAuditRulesProtected  : False
AreAccessRulesCanonical : True
AreAuditRulesCanonical  : True
```

We want just the Sddl property, and let's convert it with **ConvertFrom-SddlString** to something readable.

```text
PS C:\Users\Hector> ConvertFrom-SddlString (get-acl HKLM:\SYSTEM\CurrentControlSet\Services).Sddl
ConvertFrom-SddlString (get-acl HKLM:\SYSTEM\CurrentControlSet\Services).Sddl


Owner            : NT AUTHORITY\SYSTEM
Group            : NT AUTHORITY\SYSTEM
DiscretionaryAcl : {NT AUTHORITY\Authenticated Users: AccessAllowed (ExecuteKey, ListDirectory,
                   ReadExtendedAttributes, ReadPermissions, WriteExtendedAttributes), NT AUTHORITY\SYSTEM:
                   AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl,
                   GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions,
                   TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey), BUILTIN\Administrators:
                   AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl,
                   GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions,
                   TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey), CONTROL\Hector:
                   AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl,
                   GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions,
                   TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey)...}
SystemAcl        : {}
RawDescriptor    : System.Security.AccessControl.CommonSecurityDescriptor
```

We see it's in the DirectionaryAcl property so let's zoom it on that.

```text
PS C:\Users\Hector> (ConvertFrom-SddlString (get-acl HKLM:\SYSTEM\CurrentControlSet\Services).Sddl).DiscretionaryAcl
(ConvertFrom-SddlString (get-acl HKLM:\SYSTEM\CurrentControlSet\Services).Sddl).DiscretionaryAcl
NT AUTHORITY\Authenticated Users: AccessAllowed (ExecuteKey, ListDirectory, ReadExtendedAttributes, ReadPermissions, WriteExtendedAttributes)
NT AUTHORITY\SYSTEM: AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl, GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions, TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey)
BUILTIN\Administrators: AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl, GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions, TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey)
CONTROL\Hector: AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl, GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions, TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey)
APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES: AccessAllowed (ExecuteKey, ListDirectory, ReadExtendedAttributes, ReadPermissions, WriteExtendedAttributes)
```

And from there we see this one line

```text
CONTROL\Hector: AccessAllowed (ChangePermissions, CreateDirectories, Delete, ExecuteKey, FullControl, GenericExecute, GenericWrite, ListDirectory, ReadExtendedAttributes, ReadPermissions, TakeOwnership, Traverse, WriteData, WriteExtendedAttributes, WriteKey)
```

Basically FullControl means our user has full control over the services registry directory.