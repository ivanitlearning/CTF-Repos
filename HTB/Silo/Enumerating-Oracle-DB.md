# Enumerating Oracle DB

Before typing any commands after login it helps to set the pagesize and linesize so the results wrap around properly and doesn't split into multiple tables

```oracle
SQL> SET PAGESIZE 500;
SQL> SET LINESIZE 500;
```

List all tables our user has access to

```oracle
SQL> SELECT owner, table_name FROM all_tables;

OWNER                          TABLE_NAME
------------------------------ ------------------------------
SYS                            DUAL
SYS                            SYSTEM_PRIVILEGE_MAP
SYS                            TABLE_PRIVILEGE_MAP
SYS                            STMT_AUDIT_OPTION_MAP
SYS                            AUDIT_ACTIONS
SYS                            WRR$_REPLAY_CALL_FILTER
SYS                            HS_BULKLOAD_VIEW_OBJ
SYS                            HS$_PARALLEL_METADATA
SYS                            HS_PARTITION_COL_NAME
SYS                            HS_PARTITION_COL_TYPE
SYSTEM                         HELP
CTXSYS                         DR$OBJECT_ATTRIBUTE
CTXSYS                         DR$POLICY_TAB
CTXSYS                         DR$THS
CTXSYS                         DR$THS_PHRASE
CTXSYS                         DR$NUMBER_SEQUENCE
MDSYS                          SRSNAMESPACE_TABLE
MDSYS                          OGIS_SPATIAL_REFERENCE_SYSTEMS
MDSYS                          OGIS_GEOMETRY_COLUMNS
MDSYS                          SDO_UNITS_OF_MEASURE
MDSYS                          SDO_PRIME_MERIDIANS
MDSYS                          SDO_ELLIPSOIDS
MDSYS                          SDO_DATUMS
MDSYS                          SDO_COORD_SYS
MDSYS                          SDO_COORD_AXIS_NAMES
MDSYS                          SDO_COORD_AXES
MDSYS                          SDO_COORD_REF_SYS
MDSYS                          SDO_COORD_OP_METHODS
MDSYS                          SDO_COORD_OPS
MDSYS                          SDO_PREFERRED_OPS_SYSTEM
MDSYS                          SDO_PREFERRED_OPS_USER
MDSYS                          SDO_COORD_OP_PATHS
MDSYS                          SDO_COORD_OP_PARAMS
MDSYS                          SDO_COORD_OP_PARAM_USE
MDSYS                          SDO_COORD_OP_PARAM_VALS
MDSYS                          SDO_CS_SRS
MDSYS                          NTV2_XML_DATA
MDSYS                          SDO_CRS_GEOGRAPHIC_PLUS_HEIGHT
MDSYS                          SDO_PROJECTIONS_OLD_SNAPSHOT
MDSYS                          SDO_ELLIPSOIDS_OLD_SNAPSHOT
MDSYS                          SDO_DATUMS_OLD_SNAPSHOT
MDSYS                          SDO_XML_SCHEMAS
APEX_040000                    WWV_FLOW_DUAL100
SCOTT                          DEPT
SCOTT                          EMP
SCOTT                          BONUS
SCOTT                          SALGRADE
APEX_040000                    WWV_FLOW_TEMP_TABLE
APEX_040000                    WWV_FLOW_LOV_TEMP
MDSYS                          SDO_TOPO_DATA$
MDSYS                          SDO_TOPO_RELATION_DATA
MDSYS                          SDO_TOPO_TRANSACT_DATA
MDSYS                          SDO_CS_CONTEXT_INFORMATION
MDSYS                          SDO_TXN_IDX_EXP_UPD_RGN
MDSYS                          SDO_TXN_IDX_DELETES
MDSYS                          SDO_TXN_IDX_INSERTS
MDSYS                          SDO_ST_TOLERANCE
XDB                            XDB$XIDX_IMP_T
SYS                            KU$_DATAPUMP_MASTER_10_1
SYS                            KU$_DATAPUMP_MASTER_11_1
SYS                            KU$_DATAPUMP_MASTER_11_1_0_7
SYS                            KU$_DATAPUMP_MASTER_11_2
SYS                            IMPDP_STATS
SYS                            ODCI_PMO_ROWIDS$
SYS                            ODCI_WARNINGS$
SYS                            ODCI_SECOBJ$
SYS                            KU$_LIST_FILTER_TEMP_2
SYS                            KU$_LIST_FILTER_TEMP
SYS                            KU$NOEXP_TAB
SYSTEM                         OL$NODES
SYSTEM                         OL$HINTS
SYSTEM                         OL$
SYS                            PLAN_TABLE$
SYS                            WRI$_ADV_ASA_RECO_DATA
SYS                            PSTUBTBL

75 rows selected.
```

View a table owned by our user scott, say **EMP**

```oracle
SQL> SELECT * FROM EMP;

     EMPNO ENAME      JOB              MGR HIREDATE         SAL       COMM     DEPTNO
---------- ---------- --------- ---------- --------- ---------- ---------- ----------
      7369 SMITH      CLERK           7902 17-DEC-80        800                    20
      7499 ALLEN      SALESMAN        7698 20-FEB-81       1600        300         30
      7521 WARD       SALESMAN        7698 22-FEB-81       1250        500         30
      7566 JONES      MANAGER         7839 02-APR-81       2975                    20
      7654 MARTIN     SALESMAN        7698 28-SEP-81       1250       1400         30
      7698 BLAKE      MANAGER         7839 01-MAY-81       2850                    30
      7782 CLARK      MANAGER         7839 09-JUN-81       2450                    10
      7788 SCOTT      ANALYST         7566 19-APR-87       3000                    20
      7839 KING       PRESIDENT            17-NOV-81       5000                    10
      7844 TURNER     SALESMAN        7698 08-SEP-81       1500          0         30
      7876 ADAMS      CLERK           7788 23-MAY-87       1100                    20
      7900 JAMES      CLERK           7698 03-DEC-81        950                    30
      7902 FORD       ANALYST         7566 03-DEC-81       3000                    20
      7934 MILLER     CLERK           7782 23-JAN-82       1300                    10

14 rows selected.
```

To view our user's current privileges

```oracle
SQL> SELECT * FROM user_role_privs;

USERNAME                       GRANTED_ROLE                   ADM DEF OS_
------------------------------ ------------------------------ --- --- ---
SCOTT                          CONNECT                        NO  YES NO
SCOTT                          RESOURCE                       NO  YES NO
```

Once we login as sysdba we get a lot more

```oracle
SQL> SELECT * FROM user_role_privs;

USERNAME                       GRANTED_ROLE                   ADM DEF OS_
------------------------------ ------------------------------ --- --- ---
SYS                            ADM_PARALLEL_EXECUTE_TASK      YES YES NO
SYS                            APEX_ADMINISTRATOR_ROLE        YES YES NO
SYS                            AQ_ADMINISTRATOR_ROLE          YES YES NO
SYS                            AQ_USER_ROLE                   YES YES NO
SYS                            AUTHENTICATEDUSER              YES YES NO
SYS                            CONNECT                        YES YES NO
SYS                            CTXAPP                         YES YES NO
SYS                            DATAPUMP_EXP_FULL_DATABASE     YES YES NO
SYS                            DATAPUMP_IMP_FULL_DATABASE     YES YES NO
SYS                            DBA                            YES YES NO
SYS                            DBFS_ROLE                      YES YES NO
SYS                            DELETE_CATALOG_ROLE            YES YES NO
SYS                            EXECUTE_CATALOG_ROLE           YES YES NO
SYS                            EXP_FULL_DATABASE              YES YES NO
SYS                            GATHER_SYSTEM_STATISTICS       YES YES NO
SYS                            HS_ADMIN_EXECUTE_ROLE          YES YES NO
SYS                            HS_ADMIN_ROLE                  YES YES NO
SYS                            HS_ADMIN_SELECT_ROLE           YES YES NO
SYS                            IMP_FULL_DATABASE              YES YES NO
SYS                            LOGSTDBY_ADMINISTRATOR         YES YES NO
SYS                            OEM_ADVISOR                    YES YES NO
SYS                            OEM_MONITOR                    YES YES NO
SYS                            PLUSTRACE                      YES YES NO
SYS                            RECOVERY_CATALOG_OWNER         YES YES NO
SYS                            RESOURCE                       YES YES NO
SYS                            SCHEDULER_ADMIN                YES YES NO
SYS                            SELECT_CATALOG_ROLE            YES YES NO
SYS                            XDBADMIN                       YES YES NO
SYS                            XDB_SET_INVOKER                YES YES NO
SYS                            XDB_WEBSERVICES                YES YES NO
SYS                            XDB_WEBSERVICES_OVER_HTTP      YES YES NO
SYS                            XDB_WEBSERVICES_WITH_PUBLIC    YES YES NO

32 rows selected.
```

To read a table **COUNTRIES** owned by another user, **HR** which is readable by our user. [Ref](https://stackoverflow.com/questions/122302/as-system-in-sqlplus-how-do-i-query-another-users-table)

```oracle
SQL> SELECT * FROM HR.COUNTRIES;

CO COUNTRY_NAME                              REGION_ID
-- ---------------------------------------- ----------
AR Argentina                                         2
AU Australia                                         3
BE Belgium                                           1
BR Brazil                                            2
CA Canada                                            2
CH Switzerland                                       1
CN China                                             3
DE Germany                                           1
DK Denmark                                           1
EG Egypt                                             4
FR France                                            1

CO COUNTRY_NAME                              REGION_ID
-- ---------------------------------------- ----------
IL Israel                                            4
IN India                                             3
IT Italy                                             1
JP Japan                                             3
KW Kuwait                                            4
ML Malaysia                                          3
MX Mexico                                            2
NG Nigeria                                           4
NL Netherlands                                       1
SG Singapore                                         3
UK United Kingdom                                    1

CO COUNTRY_NAME                              REGION_ID
-- ---------------------------------------- ----------
US United States of America                          2
ZM Zambia                                            4
ZW Zimbabwe                                          4

25 rows selected.
```

But this won't show anything if the table is empty. To check if a given table **LOGMNR_USER$** is empty (note NUM_ROWS)

```oracle
SQL> SELECT num_rows FROM all_tables WHERE table_name = 'LOGMNR_USER$';

  NUM_ROWS
----------
         0
```

To be fruitful we can list all the non-empty tables owned by a user SYSTEM

```oracle
SQL> SELECT table_name FROM all_tables WHERE OWNER = 'SYSTEM' AND num_rows != 0;

TABLE_NAME
------------------------------
MVIEW$_ADV_PARAMETERS
AQ$_QUEUE_TABLES
AQ$_QUEUES
AQ$_INTERNET_AGENTS
AQ$_INTERNET_AGENT_PRIVS
REPCAT$_RESOLUTION_METHOD
REPCAT$_AUDIT_ATTRIBUTE
REPCAT$_TEMPLATE_STATUS
REPCAT$_TEMPLATE_TYPES
REPCAT$_OBJECT_TYPES
LOGSTDBY$SKIP_SUPPORT
HELP

12 rows selected.
```

