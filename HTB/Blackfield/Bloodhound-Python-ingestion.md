# Bloodhound Python ingestion

These commands run the bloodhound-python ingestor

```text
root@kali:~/CTF/HTB/Blackfield/bloodhound# bloodhound-python -d blackfield.local -u support@blackfield.local -p '#00^BlackKnight' -gc blackfield.local -c all -ns 10.10.10.192 -v
DEBUG: Authentication: username/password
DEBUG: Resolved collection methods: rdp, dcom, session, objectprops, psremote, trusts, group, localadmin, acl
DEBUG: Using DNS to retrieve domain information
DEBUG: Querying domain controller information from DNS
DEBUG: Using domain hint: blackfield.local
INFO: Found AD domain: blackfield.local
DEBUG: Found primary DC: dc01.blackfield.local
DEBUG: Found Global Catalog server: dc01.blackfield.local
DEBUG: Using LDAP server: dc01.blackfield.local
DEBUG: Using base DN: DC=blackfield,DC=local
INFO: Connecting to LDAP server: dc01.blackfield.local
DEBUG: Authenticating to LDAP server
DEBUG: No LAPS attributes found in schema
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 18 computers
DEBUG: Writing users to file: users.json
INFO: Connecting to LDAP server: dc01.blackfield.local
DEBUG: Authenticating to LDAP server
DEBUG: Querying resolver LDAP for SID S-1-5-21-4194615774-2175524697-3563712290-512
DEBUG: Querying resolver LDAP for SID S-1-5-21-4194615774-2175524697-3563712290-519
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
DEBUG: Querying resolver LDAP for SID S-1-5-21-4194615774-2175524697-3563712290-1104
DEBUG: Don't care about acetype 6
DEBUG: Don't care about acetype 6
INFO: Found 315 users
DEBUG: Finished writing users
DEBUG: Writing groups to file: groups.json
INFO: Connecting to GC LDAP server: blackfield.local
DEBUG: Authenticating to LDAP server
DEBUG: Querying GC for DN CN=Group Policy Creator Owners,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=Domain Admins,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=Cert Publishers,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=Enterprise Admins,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=Schema Admins,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=Domain Controllers,CN=Users,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=BLACKFIELD,DC=local
DEBUG: Querying GC for DN CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=BLACKFIELD,DC=local
INFO: Found 51 groups
DEBUG: Finished writing groups
DEBUG: Opening file for writing: domains.json
DEBUG: Querying resolver LDAP for SID S-1-5-21-4194615774-2175524697-3563712290-498
DEBUG: Querying resolver LDAP for SID S-1-5-21-4194615774-2175524697-3563712290-516
INFO: Found 0 trusts
DEBUG: Finished writing domain info
INFO: Starting computer enumeration with 10 workers
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
DEBUG: Start working
INFO: Querying computer: DC01.BLACKFIELD.local
DEBUG: Querying computer: DC01.BLACKFIELD.local
DEBUG: Resolved: 10.10.10.192
DEBUG: Trying connecting to computer: DC01.BLACKFIELD.local
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\srvsvc]
DEBUG: Access denied while enumerating Sessions on DC01.BLACKFIELD.local, likely a patched OS
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: Found 544 SID: S-1-5-21-4194615774-2175524697-3563712290-500
DEBUG: Found 544 SID: S-1-5-21-4194615774-2175524697-3563712290-519
DEBUG: Sid is cached: ENTERPRISE ADMINS@BLACKFIELD.LOCAL
DEBUG: Found 544 SID: S-1-5-21-4194615774-2175524697-3563712290-512
DEBUG: Sid is cached: DOMAIN ADMINS@BLACKFIELD.LOCAL
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\lsarpc]
DEBUG: Resolved SID to name: ADMINISTRATOR@BLACKFIELD.LOCAL
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\samr]
DEBUG: Opening domain handle
DEBUG: Found 580 SID: S-1-5-21-4194615774-2175524697-3563712290-1413
DEBUG: DCE/RPC binding: ncacn_np:10.10.10.192[\PIPE\lsarpc]
DEBUG: Resolved SID to name: SVC_BACKUP@BLACKFIELD.LOCAL
DEBUG: Write worker obtained a None value, exiting
DEBUG: Write worker is done, closing files
INFO: Done in 00M 03S
```

Then we check if the JSON files have been downloaded and start neo4j

```text
root@kali:~/CTF/HTB/Blackfield/bloodhound# ls
computers.json  domains.json  groups.json  users.json
root@kali:~/CTF/HTB/Blackfield/bloodhound# neo4j start console
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
Started neo4j (pid 50620). It is available at http://localhost:7474/
There may be a short delay until the server is ready.
See /usr/share/neo4j/logs/neo4j.log for current status.
root@kali:~/CTF/HTB/Blackfield/bloodhound# netstat -ant | grep 7474
tcp6       0      0 127.0.0.1:7474          :::*                    LISTEN
```

