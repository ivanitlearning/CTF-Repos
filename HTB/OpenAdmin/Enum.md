# Manual post-exploitation enum

## Enumerating files/dirs by last modified date

From linpeas we see:

```shell
[+] Last time logon each user
Username         Port     From             Latest
root             tty1                      Sat Jan  4 21:23:05 +0000 2020
jimmy            pts/1    10.10.14.3       Thu Jan  2 20:50:03 +0000 2020
joanna           pts/2    10.10.14.3       Thu Jan  2 21:12:40 +0000 2020
```
Just like what IppSec did in Postman I used `find` to search for files/dirs modified close to the time of last login of the two users.

```shell
www-data@openadmin /var/www/ona/local $ find / -newermt 2020-01-01 ! -newermt 2020-01-03 2>/dev/null
/lib
/lib/systemd/system-generators
/lib/systemd/system
/lib/udev
/lib/udev/rules.d
/lib/ifupdown
/usr/lib
/usr/lib/python3/dist-packages
/usr/share
/usr/share/man/man5
/usr/share/man/man8
/usr/share/bug
/usr/share/lintian/overrides
/usr/share/bash-completion/completions
/usr/share/doc
/usr/share/doc/ifupdown
/usr/share/doc/ifupdown/examples
/usr/share/doc/ifupdown/contrib
/usr/share/apport/package-hooks
/usr/share/dbus-1/system.d
/usr/share/dbus-1/system-services
/usr/bin
/usr/sbin
/etc
/etc/hosts
/etc/rcS.d
/etc/rcS.d/S01networking
/etc/gshadow
/etc/systemd/system
/etc/systemd/system/multi-user.target.wants
/etc/systemd/system/multi-user.target.wants/networking.service
/etc/systemd/system/network-online.target.wants
/etc/systemd/system/network-online.target.wants/networking.service
/etc/rsyslog.d
/etc/dhcp/dhclient-exit-hooks.d
/etc/rc6.d
/etc/rc6.d/K01networking
/etc/group
/etc/init.d
/etc/default
/etc/default/grub
/etc/network
/etc/network/interfaces
/etc/rc0.d
/etc/rc0.d/K01networking
/etc/profile.d
/etc/cloud
/etc/cloud/cloud.cfg.d
/var/lib/apt
/var/lib/apt/extended_states
/var/lib/apt/periodic/upgrade-stamp
/var/lib/apt/periodic/unattended-upgrades-stamp
/var/lib/apt/periodic/update-success-stamp
/var/lib/apt/lists
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-backports_InRelease
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-updates_InRelease
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-security_InRelease
/var/lib/update-notifier/hwe-eol
/var/lib/update-notifier/dpkg-run-stamp
/var/lib/update-notifier/updates-available
/var/lib/systemd
/var/lib/systemd/deb-systemd-helper-enabled
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/networking.service
/var/lib/systemd/deb-systemd-helper-enabled/networking.service.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/network-online.target.wants
/var/lib/systemd/deb-systemd-helper-enabled/network-online.target.wants/networking.service
/var/lib/dhcp
/var/lib/dhcp/dhclient.leases
/var/lib/dpkg
/var/lib/dpkg/status
/var/lib/dpkg/status-old
/var/lib/dpkg/info
/var/lib/dpkg/info/ifupdown.list
/var/lib/dpkg/updates
/var/lib/dpkg/triggers/Lock
/var/lib/dpkg/lock
/var/lib/cloud
/var/lib/cloud/instance
/var/lib/cloud/data
/var/lib/cloud/data/instance-id
/var/lib/cloud/data/previous-datasource
/var/lib/cloud/data/previous-instance-id
/var/lib/cloud/data/result.json
/var/lib/cloud/data/status.json
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/obj.pkl
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/boot-finished
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/user-data.txt
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/cloud-config.txt
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/user-data.txt.i
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/vendor-data.txt
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/vendor-data.txt.i
/var/lib/cloud/instances/4f2a8709-07da-4a21-a7a6-3d7e7511bff9/datasource
/var/cache/man
/var/cache/apt/archives
/var/cache/debconf
/var/cache/debconf/templates.dat
/var/cache/debconf/config.dat
/var/log/vmware-network.6.log
/var/log/vmware-network.4.log
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/user-1000@5c68048457e54aed9972b4a4257402ad-00000000000007f2-000597db9bb54cf2.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/system@b893c07163c04770943d9ad7f22a8dc3-0000000000000001-00059b2802415a28.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/system@00059b28024a6b16-583a6f500ff2927e.journal~
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/user-1001.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/system@2821a1ed620d4a36aa08262f72e5d797-0000000000000001-000597db80f46263.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/system@b893c07163c04770943d9ad7f22a8dc3-0000000000006eb9-00059b2e51759d52.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/user-1001@7dc36da6f7444663a306b69a0b2ab60e-0000000000003d52-000597f71fac23a8.journal
/var/log/journal/44bf1480ab2c456192be5f80ba18261f/user-1000.journal
/var/log/btmp
/var/log/vmware-network.5.log
/var/log/apt
/var/log/apt/history.log
/var/log/apt/eipp.log.xz
/var/log/apt/term.log
/var/log/cloud-init.log
/var/log/dpkg.log
/var/log/cloud-init-output.log
/var/backups
/var/backups/apt.extended_states.0
/sbin
/boot/grub
/boot/grub/grub.cfg
```

Unfortunately, nothing stood out.