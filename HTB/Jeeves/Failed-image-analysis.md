# Failed Image analysis

Note: This is a rabbit hole which leads nowhere. I'm just documenting what I tried. 

First we download both images from the Webserver with `wget` to preserve the last modified time, then run `exiftool` to enumerate metadata.
```shell
root@Kali:~/HTB/Jeeves# wget http://10.10.10.63/Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg
--2020-10-24 19:02:07--  http://10.10.10.63/Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg
Connecting to 10.10.10.63:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 23964 (23K) [image/jpeg]
Saving to: ‘Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg’

Ask-Jeeves-whatever-happened-to-32225 100%[=======================================================================>]  23.40K  --.-KB/s    in 0.01s   

2020-10-24 19:02:07 (1.83 MB/s) - ‘Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg’ saved [23964/23964]

root@Kali:~/HTB/Jeeves# wget http://10.10.10.63/jeeves.PNG
--2020-10-24 19:02:27--  http://10.10.10.63/jeeves.PNG
Connecting to 10.10.10.63:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 463431 (453K) [image/png]
Saving to: ‘jeeves.PNG’

jeeves.PNG                            100%[=======================================================================>] 452.57K  --.-KB/s    in 0.1s    

2020-10-24 19:02:27 (4.07 MB/s) - ‘jeeves.PNG’ saved [463431/463431]

root@Kali:~/HTB/Jeeves# exiftool Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg 
ExifTool Version Number         : 11.93
File Name                       : Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg
Directory                       : .
File Size                       : 23 kB
File Modification Date/Time     : 2017:11:06 08:39:14+08:00
File Access Date/Time           : 2020:10:24 19:02:07+08:00
File Inode Change Date/Time     : 2020:10:24 19:02:07+08:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : inches
X Resolution                    : 72
Displayed Units X               : inches
Y Resolution                    : 72
Displayed Units Y               : inches
Global Angle                    : 120
Copyright Flag                  : False
Photoshop Thumbnail             : (Binary data 3510 bytes, use -b option to extract)
Photoshop Quality               : 8
Photoshop Format                : Standard
Progressive Scans               : 3 Scans
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Comment                         : File written by Adobe Photoshop� 5.2
DCT Encode Version              : 100
APP14 Flags 0                   : (none)
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Image Width                     : 270
Image Height                    : 301
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 270x301
Megapixels                      : 0.081

root@Kali:~/HTB/Jeeves# exiftool jeeves.PNG 
ExifTool Version Number         : 11.93
File Name                       : jeeves.PNG
Directory                       : .
File Size                       : 453 kB
File Modification Date/Time     : 2017:11:06 10:08:06+08:00
File Access Date/Time           : 2020:10:24 19:02:27+08:00
File Inode Change Date/Time     : 2020:10:24 19:02:27+08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1212
Image Height                    : 804
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 3779
Pixels Per Unit Y               : 3779
Pixel Units                     : meters
Image Size                      : 1212x804
Megapixels                      : 0.974
```
There appears to be some binary data appended to **Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg**, so let's extract it with
```shell
root@Kali:~/HTB/Jeeves/images# exiftool Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg -b > askjeeeves
root@Kali:~/HTB/Jeeves/images# file askjeeeves 
askjeeeves: data
```
That didn't help much so let's use `binwalk`, which tells us there's really nothing special with the Ask-Jeeves image but there might be something with the other jeeves.png image.
```shell
root@Kali:~/HTB/Jeeves/images# binwalk Ask-Jeeves-whatever-happened-to-32225327-270-301.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
430           0x1AE           JPEG image data, JFIF standard 1.02
4322          0x10E2          Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"

root@Kali:~/HTB/Jeeves/images# binwalk jeeves.PNG -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1212 x 804, 8-bit/color RGBA, non-interlaced
91            0x5B            Zlib compressed data, compressed

root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# ls -lah
total 464K
drwxr-xr-x 2 root root 4.0K Oct 24 19:06 .
drwxr-xr-x 3 root root 4.0K Oct 24 19:06 ..
-rw-r--r-- 1 root root    0 Oct 24 19:06 5B
-rw-r--r-- 1 root root 453K Oct 24 19:06 5B.zlib

root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# file 5B.zlib
5B.zlib: zlib compressed data
```
Now that is unusual. What is this zlib compressed data? I [followed this](https://unix.stackexchange.com/questions/22834/how-to-uncompress-zlib-data-in-unix) to unzip zlib archive but it just threw a bunch of errors.

```shell
root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" |cat - 5B.zlib |gzip -dc >5B.out

gzip: stdin: invalid compressed data--crc error

gzip: stdin: invalid compressed data--length error


root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# file 5B.out
5B.out: data
root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# strings 5B.out | head
O>rG
CCCCC
/////
yyyyyyyy
yyyyyyyy
yyyyyy
yyyyyyyyy
yyyy
yyyyyyyyyyyyyy
yyyyyyyyyyyyy
```

Tried another alternative in the StackOverFlow thread

```shell
root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# printf "\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x00" |cat - 5B.zlib |gzip -dc >5B.out

gzip: stdin: invalid compressed data--format violated
root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# ls -lah 5B.out
-rw-r--r-- 1 root root 0 Oct 24 19:20 5B.out

root@Kali:~/HTB/Jeeves/images# python zlib.py _jeeves.PNG.extracted/*
Traceback (most recent call last):
  File "zlib.py", line 10, in <module>
    data = zlib.decompress(compressed.read())
zlib.error: Error -3 while decompressing data: incorrect header check
```

And also perl, but neither could it extract anything readable

```shell
root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# cat 5B.zlib | perl -e 'use Compress::Raw::Zlib;my $d=new Compress::Raw::Zlib::Inflate();my $o;undef $/;$d->inflate(<>,$o);print $o;' > 5B.out

root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# file 5B.out
5B.out: data

root@Kali:~/HTB/Jeeves/images/_jeeves.PNG.extracted# ls -lah 5B.out
-rw-r--r-- 1 root root 3.8M Oct 24 19:27 5B.out
```

