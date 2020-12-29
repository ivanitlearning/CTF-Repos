# Encode password file to base64 w/ powershell

This is learned from IppSec. First copy it to a PS variable. Note it still doesn't display properly.

```text
PS C:\users\Phineas\Desktop> $contents = Get-Content "Oracle issue.txt"
PS C:\users\Phineas\Desktop> $contents
Support vendor engaged to troubleshoot Windows / Oracle performance issue (full memory dump requested):

Dropbox link provided to vendor (and password under separate cover).

Dropbox link
https://www.dropbox.com/sh/69skryzfszb7elq/AADZnQEbbqDoIf5L2d0PBxENa?dl=0

link password:
?%Hm8646uC$
```

Then encode to UTF-8 base64. Note you need to use UTF8 here not the Unicode encoding you might see for [example here](https://adsecurity.org/?p=478).

```text
PS C:\users\Phineas\Desktop> $Bytes = [System.Text.Encoding]::UTF8.GetBytes($contents)
PS C:\users\Phineas\Desktop> [Convert]::ToBase64String($Bytes)
W0NvbnZlcnRdOjpUb0Jhc2U2NFN0cmluZygkQnl0ZXMpCmhvb3QgV2luZG93cyAvIE9yYWNsZSBwZXJmb3JtYW5jZSBpc3N1ZSAoZnVsbCBtZW1vcnkgZHVtcCByZXF1ZXN0ZWQpOiAgRHJvcGJveCBsaW5rIHByb3ZpZGVkIHRvIHZlbmRvciAoYW5kIHBhc3N3b3JkIHVuZGVyIHNlcGFyYXRlIGNvdmVyKS4gIERyb3Bib3ggbGluayAgaHR0cHM6Ly93d3cuZHJvcGJveC5jb20vc2gvNjlza3J5emZzemI3ZWxxL0FBRFpuUUViYnFEb0lmNUwyZDBQQnhFTmE/ZGw9MCAgbGluayBwYXNzd29yZDogwqMlSG04NjQ2dUMk
```

Then in Kali the magical character displays correctly when decoded.

```text
root@kali:~/CTF/HTB/Silo# echo W0NvbnZlcnRdOjpUb0Jhc2U2NFN0cmluZygkQnl0ZXMpCmhvb3QgV2luZG93cyAvIE9yYWNsZSBwZXJmb3JtYW5jZSBpc3N1ZSAoZnVsbCBtZW1vcnkgZHVtcCByZXF1ZXN0ZWQpOiAgRHJvcGJveCBsaW5rIHByb3ZpZGVkIHRvIHZlbmRvciAoYW5kIHBhc3N3b3JkIHVuZGVyIHNlcGFyYXRlIGNvdmVyKS4gIERyb3Bib3ggbGluayAgaHR0cHM6Ly93d3cuZHJvcGJveC5jb20vc2gvNjlza3J5emZzemI3ZWxxL0FBRFpuUUViYnFEb0lmNUwyZDBQQnhFTmE/ZGw9MCAgbGluayBwYXNzd29yZDogwqMlSG04NjQ2dUMk | base64 -d
[Convert]::ToBase64String($Bytes)
hoot Windows / Oracle performance issue (full memory dump requested):  Dropbox link provided to vendor (and password under separate cover).  Dropbox link  https://www.dropbox.com/sh/69skryzfszb7elq/AADZnQEbbqDoIf5L2d0PBxENa?dl=0  link password: £%Hm8646uC$
```

