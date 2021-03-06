# Log files in share \Data

ArkAdRecycleBin.log
```text
1/10/2018 15:43 [MAIN_THREAD]   ** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
1/10/2018 15:43 [MAIN_THREAD]   Validating settings...
1/10/2018 15:43 [MAIN_THREAD]   Error: Access is denied
1/10/2018 15:43 [MAIN_THREAD]   Exiting with error code 5
2/10/2018 15:56 [MAIN_THREAD]   ** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
2/10/2018 15:56 [MAIN_THREAD]   Validating settings...
2/10/2018 15:56 [MAIN_THREAD]   Running as user CASCADE\ArkSvc
2/10/2018 15:56 [MAIN_THREAD]   Moving object to AD recycle bin CN=Test,OU=Users,OU=UK,DC=cascade,DC=local
2/10/2018 15:56 [MAIN_THREAD]   Successfully moved object. New location CN=Test\0ADEL:ab073fb7-6d91-4fd1-b877-817b9e1b0e6d,CN=Deleted Objects,DC=cascade,DC=local
2/10/2018 15:56 [MAIN_THREAD]   Exiting with error code 0
8/12/2018 12:22 [MAIN_THREAD]   ** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
8/12/2018 12:22 [MAIN_THREAD]   Validating settings...
8/12/2018 12:22 [MAIN_THREAD]   Running as user CASCADE\ArkSvc
8/12/2018 12:22 [MAIN_THREAD]   Moving object to AD recycle bin CN=TempAdmin,OU=Users,OU=UK,DC=cascade,DC=local
8/12/2018 12:22 [MAIN_THREAD]   Successfully moved object. New location CN=TempAdmin\0ADEL:f0cc344d-31e0-4866-bceb-a842791ca059,CN=Deleted Objects,DC=cascade,DC=local
8/12/2018 12:22 [MAIN_THREAD]   Exiting with error code 0
```
dcdiag.log
```text
Directory Server Diagnosis

Performing initial setup:
   Trying to find home server...
   Home Server = CASC-DC1
   * Identified AD Forest.
   Done gathering initial info.

Doing initial required tests

   Testing server: Default-First-Site-Name\CASC-DC1
      Starting test: Connectivity
         ......................... CASC-DC1 passed test Connectivity

Doing primary tests

   Testing server: Default-First-Site-Name\CASC-DC1
      Starting test: Advertising
         ......................... CASC-DC1 passed test Advertising
      Starting test: FrsEvent
         ......................... CASC-DC1 passed test FrsEvent
      Starting test: DFSREvent
         ......................... CASC-DC1 passed test DFSREvent
      Starting test: SysVolCheck
         ......................... CASC-DC1 passed test SysVolCheck
      Starting test: KccEvent
         ......................... CASC-DC1 passed test KccEvent
      Starting test: KnowsOfRoleHolders
         ......................... CASC-DC1 passed test KnowsOfRoleHolders
      Starting test: MachineAccount
         ......................... CASC-DC1 passed test MachineAccount
      Starting test: NCSecDesc
         ......................... CASC-DC1 passed test NCSecDesc
      Starting test: NetLogons
         ......................... CASC-DC1 passed test NetLogons
      Starting test: ObjectsReplicated
         ......................... CASC-DC1 passed test ObjectsReplicated
      Starting test: Replications
         ......................... CASC-DC1 passed test Replications
      Starting test: RidManager
         ......................... CASC-DC1 passed test RidManager
      Starting test: Services
         ......................... CASC-DC1 passed test Services
      Starting test: SystemLog
         A warning event occurred.  EventID: 0x8000001D
            Time Generated: 01/10/2020   15:48:14
            Event String:
            The Key Distribution Center (KDC) cannot find a suitable certificate to use for smart card logons, or the KDC certificate could not be verified. Smart card logon may not function correctly if this problem is not resolved. To correct this problem, either verify the existing KDC certificate using certutil.exe or enroll for a new KDC certificate.
         An error event occurred.  EventID: 0xC00038D6
            Time Generated: 01/10/2020   15:48:43
            Event String:
            The DFS Namespace service could not initialize cross forest trust information on this domain controller, but it will periodically retry the operation. The return code is in the record data.
         A warning event occurred.  EventID: 0x000003F6
            Time Generated: 01/10/2020   15:48:43
            Event String:
            Name resolution for the name _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.cascade.local timed out after none of the configured DNS servers responded.
         A warning event occurred.  EventID: 0x0000000C
            Time Generated: 01/10/2020   15:48:43
            Event String:
            Time Provider NtpClient: This machine is configured to use the domain hierarchy to determine its time source, but it is the AD PDC emulator for the domain at the root of the forest, so there is no machine above it in the domain hierarchy to use as a time source. It is recommended that you either configure a reliable time service in the root domain, or manually configure the AD PDC to synchronize with an external time source. Otherwise, this machine will function as the authoritative time source in the domain hierarchy. If an external time source is not configured or used for this computer, you may choose to disable the NtpClient.
         A warning event occurred.  EventID: 0x000727AA
            Time Generated: 01/10/2020   15:50:52
            Event String:
            The WinRM service failed to create the following SPNs: WSMAN/CASC-DC1.cascade.local; WSMAN/CASC-DC1.
         ......................... CASC-DC1 failed test SystemLog
      Starting test: VerifyReferences
         ......................... CASC-DC1 passed test VerifyReferences


   Running partition tests on : ForestDnsZones
      Starting test: CheckSDRefDom
         ......................... ForestDnsZones passed test CheckSDRefDom
      Starting test: CrossRefValidation
         ......................... ForestDnsZones passed test
         CrossRefValidation

   Running partition tests on : DomainDnsZones
      Starting test: CheckSDRefDom
         ......................... DomainDnsZones passed test CheckSDRefDom
      Starting test: CrossRefValidation
         ......................... DomainDnsZones passed test
         CrossRefValidation

   Running partition tests on : Schema
      Starting test: CheckSDRefDom
         ......................... Schema passed test CheckSDRefDom
      Starting test: CrossRefValidation
         ......................... Schema passed test CrossRefValidation

   Running partition tests on : Configuration
      Starting test: CheckSDRefDom
         ......................... Configuration passed test CheckSDRefDom
      Starting test: CrossRefValidation
         ......................... Configuration passed test CrossRefValidation

   Running partition tests on : cascade
      Starting test: CheckSDRefDom
         ......................... cascade passed test CheckSDRefDom
      Starting test: CrossRefValidation
         ......................... cascade passed test CrossRefValidation

   Running enterprise tests on : cascade.local
      Starting test: LocatorCheck
         ......................... cascade.local passed test LocatorCheck
      Starting test: Intersite
         ......................... cascade.local passed test Intersite
```