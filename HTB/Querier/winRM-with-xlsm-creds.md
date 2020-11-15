# Testing winRM access with xlsm creds

I tried both usernames **Luis** and **reporting**

```shell
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p PcwTWTHRwryjc$c6 10.10.10.125

root@Kali:~/HTB/Querier# crackmapexec winrm 10.10.10.125
WINRM       10.10.10.125    5985   QUERIER          [*] http://10.10.10.125:5985/wsman
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p PcwTWTHRwryjc$c6 -d local.htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] local.htb\luis:PcwTWTHRwryjc "Failed to authenticate the user luis with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p "PcwTWTHRwryjc$c6" -d local.htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] local.htb\luis:PcwTWTHRwryjc "Failed to authenticate the user luis with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p 'PcwTWTHRwryjc$c6' -d local.htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] local.htb\luis:PcwTWTHRwryjc$c6 "Failed to authenticate the user luis with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u reporting -p 'PcwTWTHRwryjc$c6' -d local.htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] local.htb\reporting:PcwTWTHRwryjc$c6 "Failed to authenticate the user reporting with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u reporting -p 'PcwTWTHRwryjc$c6' -d htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] htb\reporting:PcwTWTHRwryjc$c6 "Failed to authenticate the user reporting with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p 'PcwTWTHRwryjc$c6' -d htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] htb\luis:PcwTWTHRwryjc$c6 "Failed to authenticate the user luis with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u luis -p 'PcwTWTHRwryjc$c6' -d htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] htb\luis:PcwTWTHRwryjc$c6 "Failed to authenticate the user luis with ntlm"
```

**reporting** was equally unsuccessful

```shell
root@Kali:~/HTB/Querier# crackmapexec winrm -u reporting -p 'PcwTWTHRwryjc$c6' -d local.htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] local.htb\reporting:PcwTWTHRwryjc$c6 "Failed to authenticate the user reporting with ntlm"
root@Kali:~/HTB/Querier# crackmapexec winrm -u reporting -p 'PcwTWTHRwryjc$c6' -d htb 10.10.10.125
WINRM       10.10.10.125    5985   10.10.10.125     [*] http://10.10.10.125:5985/wsman
WINRM       10.10.10.125    5985   10.10.10.125     [-] htb\reporting:PcwTWTHRwryjc$c6 "Failed to authenticate the user reporting with ntlm"
```

As was evil-winrm

```shell

```