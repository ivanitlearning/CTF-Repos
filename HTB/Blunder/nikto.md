# nikto

nitko returned this

```shell
root@kali:~/CTF/HTB/Blunder# nikto -h http://10.10.10.191
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.191
+ Target Hostname:    10.10.10.191
+ Target Port:        80
+ Start Time:         2020-11-29 01:38:21 (GMT8)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Retrieved x-powered-by header: Bludit
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ All CGI directories 'found', use '-C none' to test none
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ /admin/config.php: PHP Config file may contain database IDs and passwords.
+ /admin/cplogfile.log: DevBB 1.0 final (http://www.mybboard.com) log file is readable remotely. Upgrade to the latest version.
+ /admin/system_footer.php: myphpnuke version 1.8.8_final_7 reveals detailed system information.
+ OSVDB-3233: /admin/admin_phpinfo.php4: Mon Album from http://www.3dsrc.com version 0.6.2d allows remote admin access. This should be protected.
+ OSVDB-5034: /admin/login.php?action=insert&username=test&password=test: phpAuction may allow user admin accounts to be inserted without proper authentication. Attempt to log in with user 'test' password 'test' to verify.
+ OSVDB-376: /admin/contextAdmin/contextAdmin.html: Tomcat may be configured to let attackers read arbitrary files. Restrict access to /admin.
+ OSVDB-2813: /admin/database/wwForum.mdb: Web Wiz Forums pre 7.5 is vulnerable to Cross-Site Scripting attacks. Default login/pass is Administrator/letmein
+ OSVDB-2922: /admin/wg_user-info.ml: WebGate Web Eye exposes user names and passwords.
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3093: /admin/auth.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/cfg/configscreen.inc.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/cfg/configsite.inc.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/cfg/configsql.inc.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/cfg/configtache.inc.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/cms/htmltags.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/credit_card_info.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/exec.php3: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/modules/cache.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/objects.inc.php4: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/script.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/settings.inc.php+: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/templates/header.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3093: /admin/upload.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-4238: /admin/adminproc.asp: Xpede administration page may be available. The /admin directory should be protected.
+ OSVDB-4239: /admin/datasource.asp: Xpede page reveals SQL account name. The /admin directory should be protected.
+ OSVDB-9624: /admin/admin.php?adminpy=1: PY-Membres 4.2 may allow administrator access.
+ OSVDB-3092: /install.php: install.php file found.
+ /admin/account.asp: Admin login page/section found.
+ /admin/account.html: Admin login page/section found.
+ /admin/account.php: Admin login page/section found.
+ /admin/controlpanel.asp: Admin login page/section found.
+ /admin/controlpanel.html: Admin login page/section found.
+ /admin/controlpanel.php: Admin login page/section found.
+ /admin/cp.asp: Admin login page/section found.
+ /admin/cp.html: Admin login page/section found.
+ /admin/cp.php: Admin login page/section found.
+ /admin/home.asp: Admin login page/section found.
+ /admin/home.php: Admin login page/section found.
+ /admin/index.asp: Admin login page/section found.
+ /admin/index.html: Admin login page/section found.
+ /admin/login.asp: Admin login page/section found.
+ /admin/login.html: Admin login page/section found.
+ /admin/login.php: Admin login page/section found.
+ /admin/html: Tomcat Manager / Host Manager interface found (pass protected)
+ /admin/status: Tomcat Server Status interface found (pass protected)
+ /admin/sites/new: ComfortableMexicanSofa CMS Engine Admin Backend (pass protected)
+ /.gitignore: .gitignore file found. It is possible to grasp the directory structure.
+ 26494 requests: 0 error(s) and 54 item(s) reported on remote host
+ End Time:           2020-11-29 01:45:59 (GMT8) (458 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


      *********************************************************************
      Portions of the server's headers (Apache/2.4.41) are not in
      the Nikto 2.1.6 database or are newer than the known string. Would you like
      to submit this information (*no server specific data*) to CIRT.net
      for a Nikto update (or you may email to sullo@cirt.net) (y/n)? y

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ The site uses SSL and Expect-CT header is not present.
- Sent updated info to cirt.net -- Thank you!
```

