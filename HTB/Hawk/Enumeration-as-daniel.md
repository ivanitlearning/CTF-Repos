# Enumeration as daniel
Enumerating files in his home dir
```shell
daniel@hawk ~ $ cat .lesshst 
.less-history-file:
.shell
"'sh'
"'bash'
"'python3'
"'python3 -c "import pty;pty.spawn('/bin/bash')"
"'awk "BEGIN {system('/bin/sh')}"'
daniel@hawk ~ $ cat .lhistory 
?
history
ll
pwd
/bin/bash
echo 'system{/bin/bash}'
man ls
exit
?
ftp
exit
vim
exit
??
?
lynx --editor=/usr/bin/vim 127.0.0.1
exit
?
find . -name test -exec 'whoami' \;
find . -name test -exec 'whoami'
find . -name test -exec whoami
exit
?
awk 'BEGIN {system("/bin/sh")}'
awk 'BEGIN {system("/bin/bash")}'
exit
links
ls -l
whoami
man ls
exit


daniel@hawk ~/.links2 $ ls -lah
total 16K
drwx------ 2 daniel daniel 4.0K Jun 12  2018 .
drwxr-xr-x 5 daniel daniel 4.0K Jul  1  2018 ..
-rw------- 1 daniel daniel  889 Jun 12  2018 bookmarks.html
-rw------- 1 daniel daniel   10 Jun 12  2018 links.his
daniel@hawk ~/.links2 $ cat bookmarks.html 
<HTML>
<HEAD>
<!-- This is an automatically generated file.
It will be read and overwritten.
Do Not Edit! -->
<TITLE>Links bookmarks</TITLE>
</HEAD>
<H1>Links bookmarks</H1>

<DL><P>
    <DT><H3>Links</H3>
<DL>
    <DT><H3>English</H3>
<DL>
    <DT><A HREF="http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/calibration.html">Calibration Procedure</A>
    <DT><A HREF="http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/">Links Homepage</A>
    <DT><A HREF="http://links.twibright.com/user_en.html">Links Manual</A>
</DL>
    <DT><H3>Cesky</H3>
<DL>
    <DT><A HREF="http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/kalibrace.html">Kalibracni procedura</A>
    <DT><A HREF="http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/index_cz.html">Links: domaci stranka</A>
    <DT><A HREF="http://links.twibright.com/user.html">Manual k Linksu</A>
</DL>
</DL>
</DL><P>
</HTML>
daniel@hawk ~/.links2 $ cat links.his 
127.0.0.1
```