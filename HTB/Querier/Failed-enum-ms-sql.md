# Failed MSQ-SQL enumeration

Couldn't enumerate anything with `sqsh`

```shell
root@Kali:~/HTB/Querier# sqsh -S 10.10.10.125 -U reporting -P "PcwTWTHRwryjc$c6" -D volume
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
Login failed for user 'reporting'.
Password: ^C

root@Kali:~/HTB/Querier# sqsh -S 10.10.10.125 -U luis -P "PcwTWTHRwryjc$c6" -D volume
sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
This is free software with ABSOLUTELY NO WARRANTY
For more information type '\warranty'
Login failed for user 'luis'.
Password: ^C
```

So I upgraded with `apt install mssql-cli ` but it still couldn't login

```shell
root@Kali:~/HTB/Querier# mssql-cli -U reporting -P PcwTWTHRwryjc$c6 -S 10.10.10.125
Error message: Login failed for user 'reporting'.
root@Kali:~/HTB/Querier# mssql-cli -U Luis -P PcwTWTHRwryjc$c6 -S 10.10.10.125
Error message: Login failed for user 'Luis'.
root@Kali:~/HTB/Querier# mssql-cli -U querier\Luis -P PcwTWTHRwryjc$c6 -S 10.10.10.125
Error message: Login failed for user 'querierLuis'.
root@Kali:~/HTB/Querier# mssql-cli -U querier/Luis -P PcwTWTHRwryjc$c6 -S 10.10.10.125
Error message: Login failed for user 'querier/Luis'.

root@Kali:~/HTB/Querier# mssql-cli -E -U querier\reporting -S 10.10.10.125
Error message: Cannot authenticate using Kerberos. Ensure Kerberos has been initialized on the client with 'kinit' and a Service Principal Name has been registered for the SQL Server to allow Kerberos authentication.
ErrorCode=InternalError, Exception=Interop+NetSecurityNative+GssApiException: GSSAPI operation failed with error - An invalid status code was supplied (SPNEGO cannot find mechanisms to negotiate).
   at System.Net.Security.NegotiateStreamPal.GssInitSecurityContext(SafeGssContextHandle& context, SafeGssCredHandle credential, Boolean isNtlm, SafeGssNameHandle targetName, GssFlags inFlags, Byte[] buffer, Byte[]& outputBuffer, UInt32& outFlags, Int32& isNtlmUsed)
   at System.Net.Security.NegotiateStreamPal.EstablishSecurityContext(SafeFreeNegoCredentials credential, SafeDeleteContext& context, String targetName, ContextFlagsPal inFlags, SecurityBuffer inputBuffer, SecurityBuffer outputBuffer, ContextFlagsPal& outFlags)
   at System.Data.SqlClient.SNI.SNIProxy.GenSspiClientContext(SspiClientContextStatus sspiClientContextStatus, Byte[] receivedBuff, Byte[]& sendBuff, Byte[] serverName)
   at System.Data.SqlClient.SNI.TdsParserStateObjectManaged.GenerateSspiClientContext(Byte[] receivedBuff, UInt32 receivedLength, Byte[]& sendBuff, UInt32& sendLength, Byte[] _sniSpnBuffer)
   at System.Data.SqlClient.TdsParser.SNISSPIData(Byte[] receivedBuff, UInt32 receivedLength, Byte[]& sendBuff, UInt32& sendLength)
```

 Next I tried `crackmapexec` but still got nothing.

```shell
root@Kali:~/HTB/Querier# crackmapexec mssql -u reporting -p "PcwTWTHRwryjc$c6" -d querier.htb.local -x "whoami" 10.10.10.125
MSSQL       10.10.10.125    1433   None             [-] ERROR(QUERIER): Line 1: Login failed. The login is from an untrusted domain and cannot be used with Integrated authentication.
root@Kali:~/HTB/Querier# crackmapexec mssql -u reporting -p "PcwTWTHRwryjc$c6" -d querier.htb.local -X '$PSVersionTable' 10.10.10.125
MSSQL       10.10.10.125    1433   None             [-] ERROR(QUERIER): Line 1: Login failed. The login is from an untrusted domain and cannot be used with Integrated authentication.
root@Kali:~/HTB/Querier# crackmapexec mssql -u reporting -p "PcwTWTHRwryjc$c6" -d querier -X '$PSVersionTable' 10.10.10.125
MSSQL       10.10.10.125    1433   None             [-] ERROR(QUERIER): Line 1: Login failed. The login is from an untrusted domain and cannot be used with Integrated authentication.
```

