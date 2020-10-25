# Enumerating files as www-data
Let's do a check on files owned by daniel
```shell
www-data@hawk /tmp $ find / -user daniel -ls 2>/dev/null
   163841      4 drwxr-xr-x   5 daniel   daniel       4096 Jul  1  2018 /home/daniel
   133644      0 lrwxrwxrwx   1 daniel   daniel          9 Jul  1  2018 /home/daniel/.python_history -> /dev/null
   423667      4 drwx------   3 daniel   daniel       4096 Jun 12  2018 /home/daniel/.gnupg
   133115      4 -rw-------   1 daniel   daniel        136 Jun 12  2018 /home/daniel/.lesshst
   423660      4 drwx------   2 daniel   daniel       4096 Jun 12  2018 /home/daniel/.links2
   559713      4 drwx------   2 daniel   daniel       4096 Jun 12  2018 /home/daniel/.cache
   133116      4 -rw-------   1 daniel   daniel        342 Jun 12  2018 /home/daniel/.lhistory
   133094      0 lrwxrwxrwx   1 daniel   daniel          9 Jul  1  2018 /home/daniel/.bash_history -> /dev/null
   133091      4 -rw-------   1 daniel   daniel        814 Jun 12  2018 /home/daniel/.viminfo
   131997      4 -rw-r--r--   1 daniel   daniel         33 Jun 16  2018 /home/daniel/user.txt
```
Checking files modified before/after daniel's last login (within a day)

```shell
www-data@hawk /tmp $ find / -newermt 2018-06-30 ! -newermt 2018-07-02 2>/dev/null
/lib/x86_64-linux-gnu
/lib/firmware/amd-ucode
/snap/core
/snap/core/current
/root
/boot
/boot/initrd.img-4.15.0-23-generic
/home/daniel
/home/daniel/.python_history
/home/daniel/.bash_history
/var/lib/snapd/system-key
/var/lib/snapd/assertions/asserts-v0/snap-revision
/var/lib/snapd/assertions/asserts-v0/snap-revision/cDS_x7t9m0mkLyK4b_uRFRKSqKRgv1Gos1DKlDEM-n2mD93qHBPCW4p3T9IGoDNM
/var/lib/snapd/assertions/asserts-v0/snap-revision/cDS_x7t9m0mkLyK4b_uRFRKSqKRgv1Gos1DKlDEM-n2mD93qHBPCW4p3T9IGoDNM/active
/var/lib/snapd/seccomp/bpf
/var/lib/snapd/seccomp/bpf/snap.core.hook.configure.bin
/var/lib/snapd/apparmor/profiles
/var/lib/snapd/apparmor/profiles/snap-update-ns.core
/var/lib/snapd/apparmor/profiles/snap.core.hook.configure
/var/lib/snapd/snaps/core_4830.snap
/var/lib/dpkg/info/openssl.list
/var/lib/dpkg/info/libgcrypt20:amd64.list
/var/lib/dpkg/info/libssl1.0.0:amd64.list
/var/lib/dpkg/info/libssl1.1:amd64.list
/var/lib/dpkg/info/amd64-microcode.list
/var/lib/dpkg/triggers
/var/lib/dpkg/triggers/Unincorp
/var/lib/apt/lists
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-updates_main_binary-amd64_Packages
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-updates_multiverse_binary-amd64_Packages
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-updates_InRelease
/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_xenial-security_InRelease
/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_bionic-security_InRelease
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-updates_universe_binary-amd64_Packages
/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic-backports_InRelease
/var/lib/apt/periodic/update-success-stamp
/var/lib/initramfs-tools/4.15.0-23-generic
/var/log/journal/a37481d05c5a4b11b197e7cc217e727f/user-1002.journal
/var/snap/core
/var/snap/core/current
/var/cache/debconf
/var/cache/debconf/templates.dat-old
/var/cache/debconf/templates.dat
/var/cache/debconf/config.dat
/var/cache/snapd
/var/cache/snapd/sections
/var/cache/snapd/names
/var/cache/snapd/commands.db
/var/cache/apparmor
/var/cache/apparmor/snap-update-ns.core
/var/cache/apparmor/snap.core.hook.configure
/usr/lib/x86_64-linux-gnu/openssl-1.0.0/engines
/usr/lib/x86_64-linux-gnu/engines-1.1
/usr/lib/ssl
/usr/lib/ssl/misc
/usr/share/man/man7
/usr/share/initramfs-tools/hooks
/usr/share/doc/libgcrypt20
/usr/share/doc/amd64-microcode
/usr/share/doc/openssl
/usr/share/doc/openssl/HOWTO
/usr/share/doc/libssl1.0.0
/usr/share/doc/libssl1.1
/etc/ssl
/etc/modprobe.d
/etc/systemd/system/snap-core-4830.mount
/etc/systemd/system/multi-user.target.wants/snap-core-4830.mount
/etc/apparmor.d
/etc/apparmor.d/snap.core.4830.usr.lib.snapd.snap-confine
/etc/apparmor.d/cache
/etc/apparmor.d/cache/snap.core.4830.usr.lib.snapd.snap-confine
```
Checking files modified within a day of root's last login
```shell
www-data@hawk /tmp $ find / -newermt 2018-07-13 ! -newermt 2018-07-15 2>/dev/null
/lib
/lib/udev
/lib/udev/rules.d
/lib/ifupdown
/lib/systemd/system
/boot/grub
/boot/grub/grub.cfg
/sbin
/var/lib/ubuntu-release-upgrader/release-upgrade-available
/var/lib/update-notifier
/var/lib/update-notifier/updates-available
/var/lib/update-notifier/fsck-at-reboot
/var/lib/update-notifier/hwe-eol
/var/lib/update-notifier/dpkg-run-stamp
/var/lib/dpkg
/var/lib/dpkg/status-old
/var/lib/dpkg/updates
/var/lib/dpkg/lock
/var/lib/dpkg/info
/var/lib/dpkg/info/ifupdown.list
/var/lib/dpkg/status
/var/lib/dpkg/triggers/Lock
/var/lib/apt
/var/lib/apt/extended_states
/var/lib/systemd/deb-systemd-helper-enabled
/var/lib/systemd/deb-systemd-helper-enabled/ureadahead.service.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/networking.service.dsh-also
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants
/var/lib/systemd/deb-systemd-helper-enabled/multi-user.target.wants/networking.service
/var/lib/systemd/deb-systemd-helper-enabled/network-online.target.wants
/var/lib/systemd/deb-systemd-helper-enabled/network-online.target.wants/networking.service
/var/log/lastlog
/var/log/journal/a37481d05c5a4b11b197e7cc217e727f/system@919face7fb3c4c9c8c5ed880d6ed4ef3-0000000000000001-00056e5c5b7e529f.journal
/var/log/dpkg.log
/var/log/vmware-vmsvc.1.log
/var/log/apt
/var/log/apt/term.log
/var/log/apt/eipp.log.xz
/var/log/apt/history.log
/var/cache/man
/var/cache/apt/archives/partial
/usr/share/lintian/overrides
/usr/share/bug
/usr/share/man/man8
/usr/share/man/man5
/usr/share/doc
/usr/share/doc/ifupdown
/usr/share/doc/ifupdown/examples
/usr/share/doc/ifupdown/contrib
/etc
/etc/network
/etc/network/interfaces
/etc/netplan
/etc/rc6.d
/etc/rc6.d/K01networking
/etc/default
/etc/default/grub
/etc/hosts
/etc/init.d
/etc/rc0.d
/etc/rc0.d/K01networking
/etc/gshadow
/etc/rcS.d
/etc/rcS.d/S01networking
/etc/systemd/system/multi-user.target.wants
/etc/systemd/system/multi-user.target.wants/networking.service
/etc/systemd/system/network-online.target.wants
/etc/systemd/system/network-online.target.wants/networking.service
/etc/group
```