# rpcclient enumeration

With TempUser's creds we can investigate users C.Smith and Administrator

```shell
rpcclient $> queryuser 0x3ec
        User Name   :   C.Smith
        Full Name   :   Carl Smith
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:
        Description :   Flag User
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :      Sun, 26 Jan 2020 15:26:18 +08
        Logoff Time              :      Thu, 01 Jan 1970 07:30:00 +0730
        Kickoff Time             :      Thu, 01 Jan 1970 07:30:00 +0730
        Password last set Time   :      Fri, 09 Aug 2019 03:49:07 +08
        Password can change Time :      Fri, 09 Aug 2019 03:49:07 +08
        Password must change Time:      Thu, 14 Sep 30828 10:48:05 +08
        unknown_2[0..31]...
        user_rid :      0x3ec
        group_rid:      0x201
        acb_info :      0x00000210
        fields_present: 0x00ffffff
        logon_divs:     168
        bad_password_count:     0x00000000
        logon_count:    0x00000000
        padding1[0..7]...
        logon_hrs[0..21]...
rpcclient $> queryuser 0x1f4
        User Name   :   Administrator
        Full Name   :
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:
        Description :   Built-in account for administering the computer/domain
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :      Sun, 26 Jan 2020 15:20:33 +08
        Logoff Time              :      Thu, 01 Jan 1970 07:30:00 +0730
        Kickoff Time             :      Thu, 01 Jan 1970 07:30:00 +0730
        Password last set Time   :      Fri, 09 Aug 2019 02:21:23 +08
        Password can change Time :      Fri, 09 Aug 2019 02:21:23 +08
        Password must change Time:      Thu, 14 Sep 30828 10:48:05 +08
        unknown_2[0..31]...
        user_rid :      0x1f4
        group_rid:      0x201
        acb_info :      0x00000010
        fields_present: 0x00ffffff
        logon_divs:     168
        bad_password_count:     0x00000000
        logon_count:    0x0000001c
        padding1[0..7]...
        logon_hrs[0..21]...
```

