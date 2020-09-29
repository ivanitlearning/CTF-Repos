# /feed



I ran `exiftool` to check what /feed actually was.

```shell
root@Kali:~/HTB/DevOops# curl http://10.10.10.91:5000/feed
Warning: Binary output can mess up your terminal. Use "--output -" to tell 
Warning: curl to output it to your terminal anyway, or consider "--output 
Warning: <FILE>" to save to a file.

root@Kali:~/HTB/DevOops# curl http://10.10.10.91:5000/feed -o feed
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  533k  100  533k    0     0  1418k      0 --:--:-- --:--:-- --:--:-- 1418k
root@Kali:~/HTB/DevOops# file feed
feed: PNG image data, 2166 x 1648, 8-bit/color RGBA, non-interlaced
root@Kali:~/HTB/DevOops# exiftool feed 
ExifTool Version Number         : 11.93
File Name                       : feed
Directory                       : .
File Size                       : 533 kB
File Modification Date/Time     : 2020:09:12 01:00:24+08:00
File Access Date/Time           : 2020:09:12 01:00:27+08:00
File Inode Change Date/Time     : 2020:09:12 01:00:24+08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 2166
Image Height                    : 1648
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Profile Name                    : ICC Profile
Profile CMM Type                : Apple Computer Inc.
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2018:01:02 13:07:14
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Apple Computer Inc.
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Apple Computer Inc.
Profile ID                      : 0
Profile Description             : Display
Profile Description ML (hr-HR)  : LCD u boji
Profile Description ML (ko-KR)  : 컬러 LCD
Profile Description ML (nb-NO)  : Farge-LCD
Profile Description ML (hu-HU)  : Színes LCD
Profile Description ML (cs-CZ)  : Barevný LCD
Profile Description ML (da-DK)  : LCD-farveskærm
Profile Description ML (nl-NL)  : Kleuren-LCD
Profile Description ML (fi-FI)  : Väri-LCD
Profile Description ML (it-IT)  : LCD colori
Profile Description ML (ro-RO)  : LCD color
Profile Description ML (es-ES)  : LCD color
Profile Description ML (uk-UA)  : Кольоровий LCD
Profile Description ML (he-IL)  : ‏LCD צבעוני
Profile Description ML (zh-TW)  : 彩色 LCD
Profile Description ML (vi-VN)  : LCD Màu
Profile Description ML (sk-SK)  : Farebný LCD
Profile Description ML (zh-CN)  : 彩色 LCD
Profile Description ML (ru-RU)  : Цветной ЖК-дисплей
Profile Description ML (fr-FR)  : LCD couleur
Profile Description ML (hi-IN)  : रंगीन LCD
Profile Description ML (th-TH)  : LCD สี
Profile Description ML (ca-ES)  : LCD en color
Profile Description ML (es-XL)  : LCD color
Profile Description ML (de-DE)  : Farb-LCD
Profile Description ML          : Color LCD
Profile Description ML (pt-BR)  : LCD Colorido
Profile Description ML (pl-PL)  : Kolor LCD
Profile Description ML (el-GR)  : Έγχρωμη οθόνη LCD
Profile Description ML (sv-SE)  : Färg-LCD
Profile Description ML (tr-TR)  : Renkli LCD
Profile Description ML (pt-PT)  : LCD a Cores
Profile Description ML (ja-JP)  : カラーLCD
Profile Copyright               : Copyright Apple Inc., 2018
Media White Point               : 0.94955 1 1.08902
Red Matrix Column               : 0.51344 0.24071 -0.00105
Green Matrix Column             : 0.2971 0.70439 0.04253
Blue Matrix Column              : 0.15366 0.05492 0.78343
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Video Card Gamma                : (Binary data 48 bytes, use -b option to extract)
Native Display Info             : (Binary data 62 bytes, use -b option to extract)
Chromatic Adaptation            : 1.04861 0.02332 -0.05034 0.03018 0.99002 -0.01714 -0.00922 0.01503 0.75172
Make And Model                  : (Binary data 40 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Pixels Per Unit X               : 5669
Pixels Per Unit Y               : 5669
Pixel Units                     : meters
XMP Toolkit                     : XMP Core 5.4.0
Exif Image Width                : 2166
Exif Image Height               : 1648
Image Size                      : 2166x1648
Megapixels                      : 3.6
```

Then `binwalk` to see if there were hidden files inside. Having found nothing I extracted the binary data with `exiftool`.

```shell
root@Kali:~/HTB/DevOops/feed# binwalk feed -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 2166 x 1648, 8-bit/color RGBA, non-interlaced


root@Kali:~/HTB/DevOops/feed# exiftool feed -b > extract
root@Kali:~/HTB/DevOops/feed# file extract 
extract: data
root@Kali:~/HTB/DevOops/feed# strings extract 
11.93feed.5462632020:09:12 01:00:24+08:002020:09:12 01:02:03+08:002020:09:12 01:01:39+08:00644PNGPNGimage/png2166164886000ICC Profileappl528mntrRGB XYZ 2018:01:02 13:07:14acspAPPL0APPL0 000.9642 1 0.82491appl0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0DisplayLCD u boji
 LCDFarge-LCDSz
nes LCDBarevn
 LCDLCD-farvesk
rmKleuren-LCDV
ri-LCDLCD coloriLCD colorLCD color
 LCD
LCD 
 LCDLCD M
uFarebn
 LCD
 LCD
LCD couleur
 LCDLCD 
LCD en colorLCD colorFarb-LCDColor LCDLCD ColoridoKolor LCD
 LCDF
rg-LCDRenkli LCDLCD a Cores
LCDCopyright Apple Inc., 20180.94955 1 1.089020.51344 0.24071 -0.001050.2971 0.70439 0.042530.15366 0.05492 0.78343curv
	%	:	O	d	y	
 A l 
!H!u!
"'"U"
#8#f#
$M$|$
%	%8%h%
&'&W&
'I'z'
(?(q(
)8)k)
*5*h*
+6+i+
,9,n,
-A-v-
/$/Z/
050l0
2*2c2
4+4e4
676r6
7$7`7
:6:t:
;-;k;
<'<e<
="=a=
> >`>
?!?a?
@#@d@
A)AjA
B0BrB
C:C}C
F"FgF
G5G{G
J7J}J
L*LrL
N%NnN
P'PqP
R1R|R
U(UuU
X/X}X
]']x]
vcgt
ndin
1.04861 0.02332 -0.05034 0.03018 0.99002 -0.01714 -0.00922 0.01503 0.75172mmod
curv
	%	:	O	d	y	
 A l 
!H!u!
"'"U"
#8#f#
$M$|$
%	%8%h%
&'&W&
'I'z'
(?(q(
)8)k)
*5*h*
+6+i+
,9,n,
-A-v-
/$/Z/
050l0
2*2c2
4+4e4
676r6
7$7`7
:6:t:
;-;k;
<'<e<
="=a=
> >`>
?!?a?
@#@d@
A)AjA
B0BrB
C:C}C
F"FgF
G5G{G
J7J}J
L*LrL
N%NnN
P'PqP
R1R|R
U(UuU
X/X}X
]']x]
curv
	%	:	O	d	y	
 A l 
!H!u!
"'"U"
#8#f#
$M$|$
%	%8%h%
&'&W&
'I'z'
(?(q(
)8)k)
*5*h*
+6+i+
,9,n,
-A-v-
/$/Z/
050l0
2*2c2
4+4e4
676r6
7$7`7
:6:t:
;-;k;
<'<e<
="=a=
> >`>
?!?a?
@#@d@
A)AjA
B0BrB
C:C}C
F"FgF
G5G{G
J7J}J
L*LrL
N%NnN
P'PqP
R1R|R
U(UuU
X/X}X
]']x]
566956691XMP Core 5.4.0216616482166 16483.569568
```

Seeing the above I tried `strings feed` which showed
```xml
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 5.4.0">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:exif="http://ns.adobe.com/exif/1.0/">
         <exif:PixelXDimension>2166</exif:PixelXDimension>
         <exif:PixelYDimension>1648</exif:PixelYDimension>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
```
Lastly, I [tried this](https://compress-or-die.com/analyze-process) but didn't find anything