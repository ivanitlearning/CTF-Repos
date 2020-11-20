# Failed procmon.sh usage

Apart from pspy I tried procmon.sh which IppSec introduces in his [Nineveh video](https://www.youtube.com/watch?v=K9DKULxSBK4). For some reason the script failed to detect reporter.py was being run, which is a shame since it runs on bash and is compatible on all nix systems with bash, whereas pspy (a compiled binary) may not be and may have to be recompiled.

```bash
#!/bin/bash

IFS=$'\n'
old_process=$(ps -eo command)

while true; do
  new_process=$(ps -eo command)
  diff <(echo "$old_process") <(echo "$new_process") |grep [\<\>]
  sleep 1
  old_process=$new_process
done
```

Output:

```shell
friend@FriendZone:/tmp$ ./procmon.sh
> /usr/sbin/smbd --foreground --no-process-group
< /usr/sbin/smbd --foreground --no-process-group
> /usr/sbin/smbd --foreground --no-process-group
< /usr/sbin/smbd --foreground --no-process-group
< [kworker/u256:0]
< [kworker/u256:2]
< [kworker/u256:3]
> [kworker/u256:0]
```

An alternate one failed too.

```bash
#!/bin/bash

# Loop by line
IFS=$'\n'

old_process=$(ps aux --forest | grep -v "ps aux --forest" | grep -v "sleep 1" | grep -v $0)

while true; do
  new_process=$(ps aux --forest | grep -v "ps aux --forest" | grep -v "sleep 1" | grep -v $0)
  diff <(echo "$old_process") <(echo "$new_process") | grep [\<\>]
  sleep 1
  old_process=$new_process
done
```

Output:

```shell
friend@FriendZone:/tmp$ ./procmon2.sh
< root        244  0.0  1.8 127908 16756 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
> root        244  0.0  1.8 127908 16768 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
< root         89  0.0  0.0      0     0 ?        I    17:47   0:01  \_ [kworker/0:2]
> root         89  0.0  0.0      0     0 ?        I    17:47   0:02  \_ [kworker/0:2]
< root       3304  0.0  0.0      0     0 ?        I    18:30   0:00  \_ [kworker/u256:4]
< root        244  0.0  1.8 127908 16768 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
> root        244  0.0  1.8 127908 16788 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
< root        244  0.0  1.8 127908 16788 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
> root        244  0.0  1.8 127908 16792 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
> root       9883  0.0  0.0      0     0 ?        I    18:45   0:00  \_ [kworker/u256:2]
< root        244  0.0  1.8 127908 16792 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
> root        244  0.0  1.8 127908 16796 ?        S<s  17:47   0:00 /lib/systemd/systemd-journald
< root        242  0.0  1.1 192520 10448 ?        Ssl  17:47   0:02 /usr/bin/vmtoolsd
> root        242  0.0  1.1 192520 10448 ?        Ssl  17:47   0:03 /usr/bin/vmtoolsd
^C
friend@FriendZone:/tmp$ date
Sun Nov 15 18:48:31 EET 2020
```

