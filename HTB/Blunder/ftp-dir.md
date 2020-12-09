# /ftp in / directory

There are three files in **/ftp**

```shell
www-data@blunder /ftp $ ls -lah
total 11M
drwxr-xr-x  2 nobody nogroup 4.0K Nov 27  2019 .
drwxr-xr-x 21 root   root    4.0K Apr 27  2020 ..
-rw-r--r--  1 root   root     11M Nov 27  2019 D5100_EN.pdf
-rw-r--r--  1 root   root    265K Nov 27  2019 config
-rw-r--r--  1 root   root     828 Nov 27  2019 config.json
-rw-r--r--  1 root   root     260 Nov 27  2019 note.txt
www-data@blunder /ftp $ cat config.json
```

config.json

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

note.txt looks interesting and seemed like a hint.

```shell
www-data@blunder /ftp $ cat note.txt
Hey Sophie
I've left the thing you're looking for in here for you to continue my work
when I leave. The other thing is the same although Ive left it elsewhere too.

Its using the method we talked about; dont leave it on a post-it note this time!

Thanks
Shaun
```

Maybe it's referring to the 265kb file **config**. It appeared to be a gzip file and a tar.gz file so I unzipped twice and had to rename the extensions to get the gunzip, tarball tools to work.

```shell
root@kali:~/CTF/HTB/Blunder# file config
config: gzip compressed data, from Unix, original size modulo 2^32 286720
root@kali:~/CTF/HTB/Blunder/ftp# mv config config.gz
root@kali:~/CTF/HTB/Blunder/ftp# gunzip config.gz
root@kali:~/CTF/HTB/Blunder/ftp# file config
config: POSIX tar archive (GNU)
root@kali:~/CTF/HTB/Blunder/ftp# tar xzvf config

gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error is not recoverable: exiting now

root@kali:~/CTF/HTB/Blunder/ftp# tar -xvf config.tar.gz
buzz.wav
root@kali:~/CTF/HTB/Blunder/ftp# ls -lah
total 568K
drwxr-xr-x 2 root root 4.0K Nov 29 19:28 .
drwxr-xr-x 4 root root 4.0K Nov 29 19:25 ..
-rw-r--r-- 1 root root 278K Nov 27  2019 buzz.wav
-rw-r--r-- 1 root root 280K Nov 29 19:24 config.tar.gz
```

It turned to be a nonsensical wave file of a buzzing sound. The last file, D5100_EN.pdf was a digital camera manual.

![95473879aa3d41f6b8d5762bb0c33f3f](.\Pics\95473879aa3d41f6b8d5762bb0c33f3f.png)