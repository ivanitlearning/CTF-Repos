# Enumerating MS-SQL with mssqlclient.py

### DBMS enumeration

Let's check the DBMS version running

```plaintext
SQL> select @@version;
                                                                                                                                                                                                                                                                  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

Microsoft SQL Server 2017 (RTM) - 14.0.1000.169 (X64) 
	Aug 22 2017 17:04:49 
	Copyright (C) 2017 Microsoft Corporation
	Standard Edition (64-bit) on Windows Server 2019 Standard 10.0 <X64> (Build 17763: ) (Hypervisor)
```

Check what users are available in MS-SQL and what we're running as:

```plaintext
SQL> SELECT system_user;
                                                                                                                                   

--------------------------------------------------------------------------------------------------------------------------------   

QUERIER\reporting                                                                                                                  
SQL> SELECT name FROM master..syslogins
name                                                                                                                               

--------------------------------------------------------------------------------------------------------------------------------   

sa                                                                                                                                 

QUERIER\reporting
```

Let's check what roles we have

```plaintext
SQL> SELECT is_srvrolemember('bulkadmin');
              

-----------   

          0   

SQL> SELECT is_srvrolemember('systemadmin');
              

-----------   

       NULL
```

Ok so we aren't an admin here, which explains why we can't enable **xp_cmdshell**. Let's try to list the password hashes

```plaintext
SQL> SELECT name, password_hash FROM master.sys.sql_logins
name                                                                                                                                                                                                                                                                                                                                                                                 password_hash   

--------------------------------------------------------------------------------------------------------------------------------   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

sa                                                                                                                                                                                                                                                                                                                                                                                            NULL   
```

For some reason it's NULL. Let's select everything from that table instead.

```plaintext
SQL> SELECT * FROM master.sys.sql_logins 
name                                                                                                                               principal_id                                                                                                                                                                          sid   type   type_desc                                                      is_disabled   create_date   modify_date   default_database_name                                                                                                              default_language_name                                                                                                              credential_id   is_policy_checked   is_expiration_checked                                                                                                                                                                                                                                                     password_hash   

--------------------------------------------------------------------------------------------------------------------------------   ------------   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------   ----   ------------------------------------------------------------   -----------   -----------   -----------   --------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   -------------   -----------------   ---------------------   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

sa                                                                                                                                            1                                                                                                                                                                        b'01'   b'S'   SQL_LOGIN                                                                1   2003-04-08 09:10:35   2019-01-28 23:52:01   master                                                                                                                             us_english                                                                                                                                  NULL                   1                       0                                                                                                                                                                                                                                                              NULL   
```

Still nothing. Referencing [this for](https://serverfault.com/questions/292329/where-are-sql-2008-login-passwords-stored) where MS-SQL login passwords are stored

```plaintext
SQL> SELECT * FROM master.sys.server_principals
name                                                                                                                               principal_id                                                                                                                                                                          sid   type   type_desc                                                      is_disabled   create_date   modify_date   default_database_name                                                                                                              default_language_name                                                                                                              credential_id   owning_principal_id   is_fixed_role   

--------------------------------------------------------------------------------------------------------------------------------   ------------   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------   ----   ------------------------------------------------------------   -----------   -----------   -----------   --------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   -------------   -------------------   -------------   

sa                                                                                                                                            1                                                                                                                                                                        b'01'   b'S'   SQL_LOGIN                                                                1   2003-04-08 09:10:35   2019-01-28 23:52:01   master                                                                                                                             us_english                                                                                                                                  NULL                  NULL               0   

public                                                                                                                                        2                                                                                                                                                                        b'02'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               0   

sysadmin                                                                                                                                      3                                                                                                                                                                        b'03'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

securityadmin                                                                                                                                 4                                                                                                                                                                        b'04'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

serveradmin                                                                                                                                   5                                                                                                                                                                        b'05'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

setupadmin                                                                                                                                    6                                                                                                                                                                        b'06'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

processadmin                                                                                                                                  7                                                                                                                                                                        b'07'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

diskadmin                                                                                                                                     8                                                                                                                                                                        b'08'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

dbcreator                                                                                                                                     9                                                                                                                                                                        b'09'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

bulkadmin                                                                                                                                    10                                                                                                                                                                        b'0a'   b'R'   SERVER_ROLE                                                              0   2009-04-13 12:59:06   2009-04-13 12:59:06   NULL                                                                                                                               NULL                                                                                                                                        NULL                     1               1   

QUERIER\reporting                                                                                                                           266                                                                                                                  b'010500000000000515000000e5cfd9d970fd97dacb23a5d1ea030000'   b'U'   WINDOWS_LOGIN                                                            0   2019-01-29 00:10:07   2019-01-29 00:10:07   volume                                                                                                                             us_english                                                                                                                                  NULL                  NULL               0   
```

That literal byte-string looks like its hex-encoded. But it isn't.

```shell
root@Kali:~/HTB/Querier# echo 010500000000000515000000e5cfd9d970fd97dacb23a5d1ea030000 | xxd -r -p
����p����#���
```

Ok maybe we should have checked what permissions we have.

```plaintext
SQL> SELECT * FROM fn_my_permissions(NULL, 'SERVER');
entity_name                                                                                                                        subentity_name                                                                                                                     permission_name                                                

--------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   ------------------------------------------------------------   

server                                                                                                                                                                                                                                                                CONNECT SQL                                                    

server                                                                                                                                                                                                                                                                VIEW ANY DATABASE                     
```

Ok that tells us we only have permissions to connect and enumerate databases so let's do that next.

### Enumerate DBs

Listing the available DBs

```plaintext
SQL> SELECT name FROM master..sysdatabases;
name                                                                                                                               

--------------------------------------------------------------------------------------------------------------------------------   

master                                                                                                                             

tempdb                                                                                                                             

model                                                                                                                              

msdb                                                                                                                               

volume
```

Of the above, the [defaults are](https://www.vembu.com/blog/system-databases-sql-server/) **master**, **model**, **msdb**, **tempdb**. The current selected DB is

```plaintext
SQL> SELECT DB_NAME()
                                                                                                                                   

--------------------------------------------------------------------------------------------------------------------------------   

volume
```

But there is unfortunately nothing in both the volume and master DBs.

```plaintext
SQL> select * from volume.information_schema.tables;
TABLE_CATALOG                                                                                                                      TABLE_SCHEMA                                                                                                                       TABLE_NAME                                                                                                                         TABLE_TYPE   

--------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   ----------   

SQL> select * from master.information_schema.tables;
TABLE_CATALOG                                                                                                                      TABLE_SCHEMA                                                                                                                       TABLE_NAME                                                                                                                         TABLE_TYPE   

--------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   --------------------------------------------------------------------------------------------------------------------------------   ----------   

master                                                                                                                             dbo                                                                                                                                spt_fallback_db                                                                                                                    b'BASE TABLE'   

master                                                                                                                             dbo                                                                                                                                spt_fallback_dev                                                                                                                   b'BASE TABLE'   

master                                                                                                                             dbo                                                                                                                                spt_fallback_usg                                                                                                                   b'BASE TABLE'   

master                                                                                                                             dbo                                                                                                                                spt_values                                                                                                                         b'VIEW'      

master                                                                                                                             dbo                                                                                                                                spt_monitor                                                                                                                        b'BASE TABLE'
```

