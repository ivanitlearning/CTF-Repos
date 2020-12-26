# \Users share enumeration

Tried null enum of the \Users share, couldn't get anything

```shell
root@kali:~/CTF/HTB/Nest/shares/Users# smbclient -N \\\\10.10.10.178\\Users
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Jan 26 07:04:21 2020
  ..                                  D        0  Sun Jan 26 07:04:21 2020
  Administrator                       D        0  Fri Aug  9 23:08:23 2019
  C.Smith                             D        0  Sun Jan 26 15:21:44 2020
  L.Frost                             D        0  Fri Aug  9 01:03:01 2019
  R.Thompson                          D        0  Fri Aug  9 01:02:50 2019
  TempUser                            D        0  Thu Aug  8 06:55:56 2019

                10485247 blocks of size 4096. 6545808 blocks available
smb: \> prompt OFF
smb: \> recurse ON
smb: \> mget *
NT_STATUS_ACCESS_DENIED listing \Administrator\*
NT_STATUS_ACCESS_DENIED listing \C.Smith\*
NT_STATUS_ACCESS_DENIED listing \L.Frost\*
NT_STATUS_ACCESS_DENIED listing \R.Thompson\*
NT_STATUS_ACCESS_DENIED listing \TempUser\*
Segmentation fault
```

