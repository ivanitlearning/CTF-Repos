# Installing Bloodhound-python

Get [it here](https://github.com/fox-it/BloodHound.py). 

## digestmod error

After installing I encountered this error

```shell
root@Kali:~/HTB/Active# bloodhound-python -d active.htb -u SVC_TGS@active.htb -p GPPstillStandingStrong2k18 -gc active.htb -c all -ns 10.10.10.100
INFO: Found AD domain: active.htb
INFO: Connecting to LDAP server: dc.active.htb
Traceback (most recent call last):
  File "/usr/local/bin/bloodhound-python", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/__init__.py", line 284, in main
    bloodhound.run(collect=collect,
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/__init__.py", line 72, in run
    self.pdc.prefetch_info('objectprops' in collect, 'acl' in collect)
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/ad/domain.py", line 394, in prefetch_info
    self.get_objecttype()
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/ad/domain.py", line 224, in get_objecttype
    self.ldap_connect()
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/ad/domain.py", line 68, in ldap_connect
    ldap = self.ad.auth.getLDAPConnection(hostname=ip,
  File "/usr/local/lib/python3.8/dist-packages/bloodhound/ad/authentication.py", line 78, in getLDAPConnection
    if not conn.bind():
  File "/usr/lib/python3/dist-packages/ldap3/core/connection.py", line 563, in bind
    response = self.do_ntlm_bind(controls)
  File "/usr/lib/python3/dist-packages/ldap3/core/connection.py", line 1302, in do_ntlm_bind
    request = bind_operation(self.version, 'SICILY_RESPONSE_NTLM', ntlm_client, result['server_creds'])
  File "/usr/lib/python3/dist-packages/ldap3/operation/bind.py", line 81, in bind_operation
    server_creds = name.create_authenticate_message()
  File "/usr/lib/python3/dist-packages/ldap3/utils/ntlm.py", line 379, in create_authenticate_message
    nt_challenge_response = self.compute_nt_response()
  File "/usr/lib/python3/dist-packages/ldap3/utils/ntlm.py", line 485, in compute_nt_response
    response_key_nt = self.ntowf_v2()
  File "/usr/lib/python3/dist-packages/ldap3/utils/ntlm.py", line 497, in ntowf_v2
    return hmac.new(password_digest, (self.user_name.upper() + self.user_domain).encode('utf-16-le')).digest()
  File "/usr/lib/python3.8/hmac.py", line 153, in new
    return HMAC(key, msg, digestmod)
  File "/usr/lib/python3.8/hmac.py", line 51, in __init__
    raise TypeError("Missing required parameter 'digestmod'.")
TypeError: Missing required parameter 'digestmod'.
```

Fix it with `apt remove python3-ldap3`,  then install it from pip3 package with `pip3 install ldap3`. It should work now
