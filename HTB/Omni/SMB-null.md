# SMB null enumeration

crackmapexec didn't work

```text
root@kali:~/CTF/HTB/Omni# crackmapexec smb 10.10.10.204
root@kali:~/CTF/HTB/Omni# crackmapexec smb 10.10.10.204 --shares
```

Neither did rpcclient

```text
root@kali:~/CTF/HTB/Omni# rpcclient -U '' 10.10.10.204
Cannot connect to server.  Error was NT_STATUS_IO_TIMEOUT
root@kali:~/CTF/HTB/Omni# rpcclient -U '' -N 10.10.10.204
Cannot connect to server.  Error was NT_STATUS_IO_TIMEOUT
```

