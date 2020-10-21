# SMB enumeration with fsmith creds

Checking out the **IPC$** share. This usually doesn't show anything interesting but I still do it.
```plaintext
root@Kali:~/HTB/Sauna# smbmap -u fsmith -p Thestrokes23 -H sauna.egotistical-bank.local -R IPC$
[+] Finding open SMB ports....
[+] User SMB session establishd on sauna.egotistical-bank.local...
[+] IP: sauna.egotistical-bank.local:445	Name: sauna.egotistical-bank.local                      
	Disk                                                  	Permissions
	----                                                  	-----------
	IPC$                                              	READ ONLY
	.\
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	InitShutdown
	-r--r--r--                4 Mon Jan  1 06:55:25 1601	lsass
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	ntsvcs
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	scerpc
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-34c-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	epmapper
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-1bc-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	LSM_API_service
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	eventlog
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-43c-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	atsvc
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-5b4-0
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-250-0
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-250-1
	-r--r--r--                4 Mon Jan  1 06:55:25 1601	wkssvc
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	RpcProxy\49673
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	6dbd38e14caea761
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	RpcProxy\593
	-r--r--r--                4 Mon Jan  1 06:55:25 1601	srvsvc
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	spoolss
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-b64-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	netdfs
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	vgauth-service
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-240-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	ROUTER
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-75c-0
	-r--r--r--                3 Mon Jan  1 06:55:25 1601	W32TIME_ALT
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	Winsock2\CatalogChangeListener-bcc-0
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	iisipmb9bad7d6-7c79-47c3-89dc-828bc4fdc194
	-r--r--r--                1 Mon Jan  1 06:55:25 1601	iislogpipe53bf7ab7-35a3-42c1-8b8f-6bed648e0de5
```
The print$ share is somewhat unusual because we don't see them often.

```plaintext
root@Kali:~/HTB/Sauna# smbmap -u fsmith -p Thestrokes23 -H sauna.egotistical-bank.local -R print$
[+] Finding open SMB ports....
[+] User SMB session establishd on sauna.egotistical-bank.local...
[+] IP: sauna.egotistical-bank.local:445	Name: sauna.egotistical-bank.local                      
	Disk                                                  	Permissions
	----                                                  	-----------
	print$                                            	READ ONLY
	.\
	dr--r--r--                0 Thu Jan 23 13:32:39 2020	.
	dr--r--r--                0 Thu Jan 23 13:32:39 2020	..
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	color
	dr--r--r--                0 Thu Jan 23 13:32:39 2020	IA64
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	W32X86
	dr--r--r--                0 Fri Jan 24 07:10:42 2020	x64
	.\\color\
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	.
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	..
	-r--r--r--             1058 Thu Jan 23 13:27:41 2020	D50.camp
	-r--r--r--             1079 Thu Jan 23 13:27:41 2020	D65.camp
	-r--r--r--              797 Thu Jan 23 13:27:41 2020	Graphics.gmmp
	-r--r--r--              838 Thu Jan 23 13:27:41 2020	MediaSim.gmmp
	-r--r--r--              786 Thu Jan 23 13:27:41 2020	Photo.gmmp
	-r--r--r--              822 Thu Jan 23 13:27:41 2020	Proofing.gmmp
	-r--r--r--           218103 Thu Jan 23 13:28:53 2020	RSWOP.icm
	-r--r--r--             3144 Thu Jan 23 13:27:41 2020	sRGB Color Space Profile.icm
	-r--r--r--            17155 Thu Jan 23 13:28:53 2020	wscRGB.cdmp
	-r--r--r--             1578 Thu Jan 23 13:27:41 2020	wsRGB.cdmp
	.\\W32X86\
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	..
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	3
	dr--r--r--                0 Fri Jan 24 07:10:46 2020	PCC
	.\\W32X86\3\
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	..
	-r--r--r--          1035776 Fri Jan 24 07:10:43 2020	mxdwdrv.dll
	-r--r--r--          2865152 Fri Jan 24 07:10:43 2020	PrintConfig.dll
	-r--r--r--               53 Thu Jan 23 13:32:41 2020	unishare-pipelineconfig.xml
	-r--r--r--             3360 Thu Jan 23 13:32:41 2020	unishare.gpd
	.\\W32X86\PCC\
	dr--r--r--                0 Fri Jan 24 07:10:46 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:46 2020	..
	-r--r--r--          3697492 Fri Jan 24 07:10:46 2020	ntprint.inf_x86_9543832f82bb474f.cab
	-r--r--r--          1089648 Fri Jan 24 07:10:44 2020	prnms003.inf_x86_e5fa944b0ac46f93.cab
	.\\x64\
	dr--r--r--                0 Fri Jan 24 07:10:42 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:42 2020	..
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	3
	dr--r--r--                0 Fri Jan 24 07:10:45 2020	PCC
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	{8AB4F307-6E14-4E91-A0D2-6CD0FAC37F42}
	.\\x64\3\
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	..
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	en-US
	-r--r--r--            14088 Thu Jan 23 13:32:42 2020	LOCALE.GPD
	-r--r--r--            78336 Thu Jan 23 22:54:38 2020	mfricr64.dll
	-r--r--r--               73 Thu Jan 23 13:32:42 2020	MSXPSINC.GPD
	-r--r--r--               72 Thu Jan 23 13:32:42 2020	MSXPSINC.PPD
	-r--r--r--           869888 Fri Jan 24 07:10:43 2020	MXDWDRV.DLL
	-r--r--r--            25489 Thu Jan 23 13:32:42 2020	P6DISP.GPD
	-r--r--r--             3293 Thu Jan 23 13:32:42 2020	P6FONT.GPD
	-r--r--r--           288256 Thu Jan 23 13:32:42 2020	PCL4RES.DLL
	-r--r--r--          1025536 Thu Jan 23 13:32:42 2020	PCL5ERES.DLL
	-r--r--r--          1025024 Thu Jan 23 13:32:42 2020	PCL5URES.DLL
	-r--r--r--           204288 Thu Jan 23 13:32:43 2020	PCLXL.DLL
	-r--r--r--            10375 Thu Jan 23 13:32:43 2020	PCLXL.GPD
	-r--r--r--             1156 Thu Jan 23 13:32:43 2020	PJL.GPD
	-r--r--r--            23040 Fri Jan 24 07:10:39 2020	PJLMON.DLL
	-r--r--r--          3535360 Fri Jan 24 07:10:43 2020	PrintConfig.dll
	-r--r--r--          1122304 Fri Jan 24 07:10:39 2020	PS5UI.DLL
	-r--r--r--            26038 Thu Jan 23 13:32:43 2020	PSCRIPT.HLP
	-r--r--r--          1062732 Thu Jan 23 13:32:43 2020	PSCRIPT.NTF
	-r--r--r--           642560 Fri Jan 24 07:10:39 2020	PSCRIPT5.DLL
	-r--r--r--          1293180 Thu Jan 23 13:32:43 2020	PSCRPTFE.NTF
	-r--r--r--             5561 Thu Jan 23 13:32:43 2020	PS_SCHM.GDL
	-r--r--r--          1836032 Thu Jan 23 22:54:38 2020	RD058d64.dll
	-r--r--r--           337920 Thu Jan 23 22:54:38 2020	rica58cb.dll
	-r--r--r--          5185536 Thu Jan 23 22:54:38 2020	rica58cd.dll
	-r--r--r--            31809 Thu Jan 23 22:54:37 2020	rica58cd.psz
	-r--r--r--           939365 Thu Jan 23 22:54:38 2020	rica58cf.cfz
	-r--r--r--           196356 Thu Jan 23 22:54:37 2020	rica58ch.chm
	-r--r--r--          1680384 Thu Jan 23 22:54:38 2020	rica58ci.dll
	-r--r--r--           297472 Thu Jan 23 22:54:40 2020	rica58cj.dll
	-r--r--r--              534 Thu Jan 23 22:54:38 2020	rica58cl.ini
	-r--r--r--            55808 Thu Jan 23 22:54:38 2020	rica58ct.dll
	-r--r--r--          7550202 Thu Jan 23 22:54:38 2020	rica58cz.dlz
	-r--r--r--          2844160 Thu Jan 23 22:54:40 2020	rica58gr.dll
	-r--r--r--          5273600 Thu Jan 23 22:54:38 2020	rica58ug.dll
	-r--r--r--            15026 Thu Jan 23 22:54:38 2020	rica58ug.miz
	-r--r--r--          3177984 Thu Jan 23 22:54:38 2020	rica58ui.dll
	-r--r--r--             1251 Thu Jan 23 22:54:37 2020	rica58ui.irj
	-r--r--r--               69 Thu Jan 23 22:54:37 2020	rica58ui.rcf
	-r--r--r--              202 Thu Jan 23 22:54:37 2020	rica58ui.rdj
	-r--r--r--             4608 Thu Jan 23 22:54:38 2020	rica58ur.dll
	-r--r--r--            51712 Thu Jan 23 22:54:38 2020	ricdb64.dll
	-r--r--r--            23812 Thu Jan 23 13:32:43 2020	STDDTYPE.GDL
	-r--r--r--            14362 Thu Jan 23 13:32:43 2020	STDNAMES.GPD
	-r--r--r--            59116 Thu Jan 23 13:32:43 2020	STDSCHEM.GDL
	-r--r--r--             2278 Thu Jan 23 13:32:43 2020	STDSCHMX.GDL
	-r--r--r--              698 Thu Jan 23 13:32:43 2020	TTFSUB.GPD
	-r--r--r--           526336 Fri Jan 24 07:10:39 2020	UNIDRV.DLL
	-r--r--r--            21225 Thu Jan 23 13:32:43 2020	UNIDRV.HLP
	-r--r--r--          1168896 Fri Jan 24 07:10:39 2020	UNIDRVUI.DLL
	-r--r--r--           855040 Fri Jan 24 07:10:39 2020	UNIRES.DLL
	-r--r--r--               53 Thu Jan 23 13:32:40 2020	unishare-pipelineconfig.xml
	-r--r--r--             3360 Thu Jan 23 13:32:40 2020	unishare.gpd
	.\\x64\3\en-US\
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	.
	dr--r--r--                0 Thu Jan 23 13:29:26 2020	..
	-r--r--r--             4608 Thu Jan 23 13:28:53 2020	tsprint.dll.mui
	.\\x64\PCC\
	dr--r--r--                0 Fri Jan 24 07:10:45 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:45 2020	..
	-r--r--r--          3844411 Fri Jan 24 07:10:45 2020	ntprint.inf_amd64_9543832f82bb474f.cab
	-r--r--r--         14808051 Thu Jan 23 22:54:42 2020	oemsetup.inf_amd64_8d99dd951229a6eb.cab
	-r--r--r--            12465 Thu Jan 23 13:32:44 2020	prnms001.inf_amd64_f340cb58fcd23202.cab
	-r--r--r--          1292340 Fri Jan 24 07:10:43 2020	prnms003.inf_amd64_a337db27fa50b915.cab
	-r--r--r--            12645 Thu Jan 23 13:32:43 2020	prnms009.inf_amd64_80184dcbef6775bc.cab
	.\\x64\{8AB4F307-6E14-4E91-A0D2-6CD0FAC37F42}\
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	.
	dr--r--r--                0 Fri Jan 24 07:10:43 2020	..
	-r--r--r--          3535360 Fri Jan 24 07:10:42 2020	PrintConfig.dll
```
Unfortunately it just shows us config files and printer drivers. Now let's enumerating SYSVOL share to see if this is like [Active](https://ivanitlearning.wordpress.com/2020/10/02/hackthebox-active/) where we can find some xml file containing passwords or hashes.
```plaintext
root@Kali:~/HTB/Sauna# smbmap -u fsmith -p Thestrokes23 -H sauna.egotistical-bank.local -R SYSVOL
[+] Finding open SMB ports....
[+] User SMB session establishd on sauna.egotistical-bank.local...
[+] IP: sauna.egotistical-bank.local:445	Name: sauna.egotistical-bank.local                      
	Disk                                                  	Permissions
	----                                                  	-----------
	SYSVOL                                            	READ ONLY
	.\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	EGOTISTICAL-BANK.LOCAL
	.\\EGOTISTICAL-BANK.LOCAL\
	dr--r--r--                0 Thu Jan 23 13:51:08 2020	.
	dr--r--r--                0 Thu Jan 23 13:51:08 2020	..
	dr--r--r--                0 Sun Oct 18 01:35:06 2020	DfsrPrivate
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	Policies
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	scripts
	.\\EGOTISTICAL-BANK.LOCAL\Policies\
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	.
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	..
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	{2619FB25-7519-4AEA-9C1E-348725EF2858}
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	{31B2F340-016D-11D2-945F-00C04FB984F9}
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	{6AC1786C-016F-11D2-945F-00C04fB984F9}
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	.
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	..
	-r--r--r--               59 Sun Jan 26 04:48:44 2020	GPT.INI
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	Machine
	dr--r--r--                0 Sun Jan 26 04:48:44 2020	User
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\Machine\
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	.
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	..
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	Microsoft
	dr--r--r--                0 Sun Jan 26 04:49:04 2020	Scripts
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\Machine\Microsoft\
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	.
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	..
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	Windows NT
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\Machine\Microsoft\Windows NT\
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	.
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	..
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	SecEdit
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\Machine\Microsoft\Windows NT\SecEdit\
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	.
	dr--r--r--                0 Sun Jan 26 04:49:11 2020	..
	-r--r--r--              142 Sun Jan 26 04:49:11 2020	GptTmpl.inf
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{2619FB25-7519-4AEA-9C1E-348725EF2858}\Machine\Scripts\
	dr--r--r--                0 Sun Jan 26 04:49:04 2020	.
	dr--r--r--                0 Sun Jan 26 04:49:04 2020	..
	dr--r--r--                0 Sun Jan 26 04:49:04 2020	Shutdown
	dr--r--r--                0 Sun Jan 26 04:49:04 2020	Startup
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	-r--r--r--               22 Thu Jan 23 13:51:29 2020	GPT.INI
	dr--r--r--                0 Thu Jan 23 13:51:29 2020	MACHINE
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	USER
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\
	dr--r--r--                0 Thu Jan 23 13:51:29 2020	.
	dr--r--r--                0 Thu Jan 23 13:51:29 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	Microsoft
	-r--r--r--             2806 Thu Jan 23 13:51:29 2020	Registry.pol
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	Windows NT
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows NT\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	SecEdit
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows NT\SecEdit\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	-r--r--r--             1098 Thu Jan 23 13:44:49 2020	GptTmpl.inf
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	-r--r--r--               22 Fri Jan 24 00:49:29 2020	GPT.INI
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	MACHINE
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	USER
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	Microsoft
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	Windows NT
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	.
	dr--r--r--                0 Thu Jan 23 13:44:49 2020	..
	dr--r--r--                0 Fri Jan 24 00:49:29 2020	SecEdit
	.\\EGOTISTICAL-BANK.LOCAL\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows NT\SecEdit\
	dr--r--r--                0 Fri Jan 24 00:49:29 2020	.
	dr--r--r--                0 Fri Jan 24 00:49:29 2020	..
	-r--r--r--             4170 Fri Jan 24 00:49:29 2020	GptTmpl.inf
```
No XML files found. Moving on. BTW I did wonder if `smbmap` missed out on directories like **User** above so I manually checked with `smbclient`. It was empty or contained empty directories. There was nothing in the **NETLOGON** share too.

```plaintext
root@Kali:~/HTB/Sauna# smbmap -u fsmith -p Thestrokes23 -H sauna.egotistical-bank.local -R NETLOGON
[+] Finding open SMB ports....
[+] User SMB session establishd on sauna.egotistical-bank.local...
[+] IP: sauna.egotistical-bank.local:445	Name: sauna.egotistical-bank.local                      
	Disk                                                  	Permissions
	----                                                  	-----------
	NETLOGON                                          	READ ONLY
	.\
root@Kali:~/HTB/Sauna# smbclient -U 'fsmith%Thestrokes23' //sauna.egotistical-bank.local/NETLOGON
WARNING: The "syslog" option is deprecated
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Jan 23 13:44:23 2020
  ..                                  D        0  Thu Jan 23 13:44:23 2020

		5101823 blocks of size 4096. 1893281 blocks available
```

