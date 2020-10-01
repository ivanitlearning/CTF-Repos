# Installing Bloodhound

## neo4j

You need to first have **neo4j** installed. I had it installed but got this error when I tried to run it.
```shell
root@Kali:~/HTB/Active# neo4j start console
ERROR! Neo4j cannot be started using java version 1.8.0_212. 
* Please use Oracle(R) Java(TM) 11, OpenJDK(TM) 11 to run Neo4j.
* Please see https://neo4j.com/docs/ for Neo4j installation instructions.
````
### Reinstalling Java

So I had to install Java 11 for it to work. It needs both Oracle Java and OpenJDK 11. What's the difference between the two? According to [this](https://linuxconcept.com/install-java-on-debian-9-operating-system/)
> Java also has two different flavors, one is Open JDK, and another one is Oracle Java, both have the same functionalities and capabilities, the only difference is Oracle Java has some more commercial features. The default Java flavor of Linux Operating System is OpenJDK.

So I did this to add to my sources.list
```shell
root@Kali:~/HTB/Active# apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 73C3DB2A
Executing: /tmp/apt-key-gpghome.2NEme1TljF/gpg.1.sh --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 73C3DB2A
gpg: key EA8CACC073C3DB2A: public key "Launchpad PPA for Linux Uprising" imported
gpg: Total number processed: 1
gpg:               imported: 1
root@Kali:~/HTB/Active# echo 'deb http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic main' | sudo tee /etc/apt/sources.list.d/linuxuprising-java.list
deb http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic main
root@Kali:~/HTB/Active# apt update
Hit:1 http://downloads.metasploit.com/data/releases/metasploit-framework/apt lucid InRelease
Hit:2 https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch InRelease                                                    
Get:3 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic InRelease [15.9 kB]                                                           
Ign:4 http://repo.mongodb.org/apt/debian jessie/mongodb-org/4.0 InRelease                                            
Hit:5 http://repo.mongodb.org/apt/debian jessie/mongodb-org/4.0 Release                             
Get:6 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic/main amd64 Packages [2256 B]        
Hit:8 http://kali.cs.nctu.edu.tw/kali kali-rolling InRelease                                                                                
Get:9 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic/main i386 Packages [1648 B]
Hit:10 http://old.kali.org/kali sana InRelease                                                  
Get:11 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic/main Translation-en [756 B]
Fetched 20.5 kB in 2s (12.9 kB/s)                   
Reading package lists... Done
Building dependency tree       
Reading state information... Done
2074 packages can be upgraded. Run 'apt list --upgradable' to see them.
root@Kali:~/HTB/Active# apt search oracle-java11-installer
Sorting... Done
Full Text Search... Done
oracle-java11-installer-local/bionic 11.0.8-1~linuxuprising0 amd64
  Oracle Java(TM) Development Kit (JDK) 11
```
Next I installed it but got an error
```shell
root@Kali:~/HTB/Active# apt install oracle-java11-installer-local 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  python3-brotli python3-click python3-colorama python3-h11 python3-h2 python3-hpack python3-hyperframe python3-kaitaistruct python3-passlib
  python3-pyperclip python3-ruamel.yaml python3-sortedcontainers python3-wsproto
Use 'apt autoremove' to remove them.
The following additional packages will be installed:
  oracle-java11-set-default-local
Suggested packages:
  visualvm ttf-baekmuk | ttf-unfonts | ttf-unfonts-core ttf-kochi-gothic | ttf-sazanami-gothic ttf-kochi-mincho | ttf-sazanami-mincho
  ttf-arphic-uming firefox | firefox-2 | iceweasel | mozilla-firefox | iceape-browser | mozilla-browser | epiphany-gecko | epiphany-webkit
  | epiphany-browser | galeon | midbrowser | moblin-web-browser | xulrunner | xulrunner-1.9 | konqueror | chromium-browser | midori | google-chrome
The following NEW packages will be installed:
  oracle-java11-installer-local oracle-java11-set-default-local
0 upgraded, 2 newly installed, 0 to remove and 2074 not upgraded.
Need to get 37.7 kB of archives.
After this operation, 139 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic/main amd64 oracle-java11-installer-local amd64 11.0.8-1~linuxuprising0 [34.0 kB]
Get:2 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic/main amd64 oracle-java11-set-default-local amd64 11.0.8-1~linuxuprising0 [3634 B]
Fetched 37.7 kB in 1s (41.7 kB/s)                    
Preconfiguring packages ...
Selecting previously unselected package oracle-java11-installer-local.
(Reading database ... 483867 files and directories currently installed.)
Preparing to unpack .../oracle-java11-installer-local_11.0.8-1~linuxuprising0_amd64.deb ...
Unpacking oracle-java11-installer-local (11.0.8-1~linuxuprising0) ...
Setting up oracle-java11-installer-local (11.0.8-1~linuxuprising0) ...
Before installing this package,
please download the Oracle JDK 11 .tar.gz file
with the same version as this package (version 11.0.4),
and place it in /var/cache/oracle-jdk11-installer-local,

E.g.:
sudo mkdir -p /var/cache/oracle-jdk11-installer-local
sudo cp jdk-11.0.4_linux-x64_bin.tar.gz /var/cache/oracle-jdk11-installer-local/
sha256sum mismatch jdk-11.0.8_linux-x64_bin.tar.gz
Oracle JDK 11 is NOT installed.
dpkg: error processing package oracle-java11-installer-local (--configure):
 installed oracle-java11-installer-local package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 oracle-java11-installer-local
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

Note that although it says to get version 11.0.4, don't! It won't work. Instead download 11.0.8 from [here](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html). You have to login to download it unfortunately. Then I copied it to the suggested location and continued the `apt` installation

```shell
root@Kali:~/HTB/Active# cp jdk-11.0.8_linux-x64_bin.tar.gz /var/cache/oracle-jdk11-installer-local/
root@Kali:~/HTB/Active# apt install oracle-java11-installer-local 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
oracle-java11-installer-local is already the newest version (11.0.8-1~linuxuprising0).
The following packages were automatically installed and are no longer required:
  default-jdk-headless libice-dev libpthread-stubs0-dev libsm-dev libx11-dev libx11-doc libxau-dev libxcb1-dev libxdmcp-dev libxt-dev
  openjdk-11-jdk-headless python3-brotli python3-click python3-colorama python3-h11 python3-h2 python3-hpack python3-hyperframe python3-kaitaistruct
  python3-passlib python3-pyperclip python3-ruamel.yaml python3-sortedcontainers python3-wsproto x11proto-core-dev x11proto-dev x11proto-input-dev
  x11proto-kb-dev xorg-sgml-doctools xtrans-dev
Use 'apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 2070 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up oracle-java11-installer-local (11.0.8-1~linuxuprising0) ...
Installing from local file /var/cache/oracle-jdk11-installer-local/jdk-11.0.8_linux-x64_bin.tar.gz

You may want to remove any previous jdk .tar.gz versions from
/var/cache/oracle-jdk11-installer-local
update-alternatives: using /usr/lib/jvm/java-11-oracle/bin/jconsole to provide /usr/bin/jconsole (jconsole) in auto mode
update-binfmts: warning: current package is openjdk-11, but binary format already installed by openjdk-8
Oracle JDK 11 installed

#####Important########
To set Oracle JDK11 as default, install the "oracle-java11-set-default-local" package.
E.g.: sudo apt install oracle-java11-set-default-local
root@Kali:~/HTB/Active# java -version
openjdk version "1.8.0_212"
OpenJDK Runtime Environment (build 1.8.0_212-8u212-b01-1-b01)
OpenJDK 64-Bit Server VM (build 25.212-b01, mixed mode)
root@Kali:~/HTB/Active# neo4j start console
ERROR! Neo4j cannot be started using java version 1.8.0_212. 
* Please use Oracle(R) Java(TM) 11, OpenJDK(TM) 11 to run Neo4j.
* Please see https://neo4j.com/docs/ for Neo4j installation instructions.
```

Unfortuately neo4j still couldn't run. One last thing to do. Change the default Java version to Java 11.

```shell
root@Kali:~/HTB/Active# apt install oracle-java11-set-default-local
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  default-jdk-headless libice-dev libpthread-stubs0-dev libsm-dev libx11-dev libx11-doc libxau-dev libxcb1-dev libxdmcp-dev libxt-dev
  openjdk-11-jdk-headless python3-brotli python3-click python3-colorama python3-h11 python3-h2 python3-hpack python3-hyperframe python3-kaitaistruct
  python3-passlib python3-pyperclip python3-ruamel.yaml python3-sortedcontainers python3-wsproto x11proto-core-dev x11proto-dev x11proto-input-dev
  x11proto-kb-dev xorg-sgml-doctools xtrans-dev
Use 'apt autoremove' to remove them.
The following NEW packages will be installed:
  oracle-java11-set-default-local
0 upgraded, 1 newly installed, 0 to remove and 2070 not upgraded.
Need to get 0 B/3634 B of archives.
After this operation, 16.4 kB of additional disk space will be used.
Selecting previously unselected package oracle-java11-set-default-local.
(Reading database ... 483454 files and directories currently installed.)
Preparing to unpack .../oracle-java11-set-default-local_11.0.8-1~linuxuprising0_amd64.deb ...
Unpacking oracle-java11-set-default-local (11.0.8-1~linuxuprising0) ...
Setting up oracle-java11-set-default-local (11.0.8-1~linuxuprising0) ...
root@Kali:~/HTB/Active# java -version
java version "11.0.8" 2020-07-14 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.8+10-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.8+10-LTS, mixed mode)
```
Now we can run **neo4j**

```shell
root@Kali:~/HTB/Active# neo4j start console
Directories in use:
  home:         /usr/share/neo4j
  config:       /usr/share/neo4j/conf
  logs:         /usr/share/neo4j/logs
  plugins:      /usr/share/neo4j/plugins
  import:       /usr/share/neo4j/import
  data:         /usr/share/neo4j/data
  certificates: /usr/share/neo4j/certificates
  run:          /usr/share/neo4j/run
Starting Neo4j.
WARNING: Max 1024 open files allowed, minimum of 40000 recommended. See the Neo4j manual.
./bin/neo4j: line 394: /usr/share/neo4j/logs/neo4j.log: No such file or directory
Unable to start. See /usr/share/neo4j/logs/neo4j.log for details.
```
Oops we still have an error.

```shell
root@Kali:~/HTB/Active# ls /usr/share/neo4j/logs/neo4j.log
ls: cannot access '/usr/share/neo4j/logs/neo4j.log': No such file or directory
root@Kali:~/HTB/Active# ls /usr/share/neo4j/logs
ls: cannot access '/usr/share/neo4j/logs': No such file or directory
```
So it's because no such directory exist. Create it and the error goes away. Now we can start it and see it's listening on localhost:7474
```shell
root@Kali:~/HTB/Active# mkdir /usr/share/neo4j/logs
root@Kali:~/HTB/Active# neo4j start console
Directories in use:
  home:         /usr/share/neo4j
  config:       /usr/share/neo4j/conf
  logs:         /usr/share/neo4j/logs
  plugins:      /usr/share/neo4j/plugins
  import:       /usr/share/neo4j/import
  data:         /usr/share/neo4j/data
  certificates: /usr/share/neo4j/certificates
  run:          /usr/share/neo4j/run
Starting Neo4j.
WARNING: Max 1024 open files allowed, minimum of 40000 recommended. See the Neo4j manual.
Started neo4j (pid 10144). It is available at http://localhost:7474/
There may be a short delay until the server is ready.
See /usr/share/neo4j/logs/neo4j.log for current status.
root@Kali:~/HTB/Active# netstat -ant | grep 7474
tcp6       0      0 127.0.0.1:7474          :::*                    LISTEN     
```

Now we should be able to install Bloodhound with `pip3 install bloodhound`.