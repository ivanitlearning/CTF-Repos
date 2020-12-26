using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using HqkLdap.My;
using Microsoft.VisualBasic.CompilerServices;

namespace HqkLdap
{
    // Token: 0x0200000A RID: 10
    [StandardModule]
    internal sealed class MainModule
    {
        // Token: 0x06000027 RID: 39 RVA: 0x000026BC File Offset: 0x00000ABC
        [STAThread]
        public static void Main()
        {
            string decryptedPassword = string.Empty;
            decryptedPassword = CR.DS("yyEq0Uvvhq2uQOcWG8peLoeRQehqip/fKdeG/kjEVb4=");
            Console.WriteLine(decryptedPassword);
            //checked
            //{
            //	try
            //	{
            //                 if (MyProject.Application.CommandLineArgs.Count != 1)
            //                 {
            //                     Console.WriteLine("Invalid number of command line arguments");
            //                 }
            //                 else if (!File.Exists(MyProject.Application.CommandLineArgs[0]))
            //                 {
            //                     Console.WriteLine("Specified config file does not exist");
            //                 }
            //                 else if (!File.Exists("HqkDbImport.exe"))
            //                 {
            //                     Console.WriteLine("Please ensure the optional database import module is installed");
            //                 }
            //                 else
            //                 {
            //                     LdapSearchSettings ldapSearchSettings = new LdapSearchSettings();
            //                     string[] array = File.ReadAllLines(MyProject.Application.CommandLineArgs[0]);
            //                     foreach (string text in array)
            //                     {
            //                         if (text.StartsWith("Domain=", StringComparison.CurrentCultureIgnoreCase))
            //                         {
            //                             ldapSearchSettings.Domain = text.Substring(text.IndexOf('=') + 1);
            //                         }
            //                         else if (text.StartsWith("User=", StringComparison.CurrentCultureIgnoreCase))
            //                         {
            //                             ldapSearchSettings.Username = text.Substring(text.IndexOf('=') + 1);
            //                         }
            //                         else if (text.StartsWith("Password=", StringComparison.CurrentCultureIgnoreCase))
            //                         {
            //                             ldapSearchSettings.Password = CR.DS(text.Substring(text.IndexOf('=') + 1));
            //                         }
            //                     }
            //                     
            //                     

            //          Ldap ldap = new Ldap();
            //			ldap.Username = ldapSearchSettings.Username;
            //			ldap.Password = ldapSearchSettings.Password;
            //			ldap.Domain = ldapSearchSettings.Domain;
            //			Console.WriteLine("Performing LDAP query...");
            //			List<string> list = ldap.FindUsers();
            //			Console.WriteLine(Conversions.ToString(list.Count) + " user accounts found. Importing to database...");
            //			try
            //			{
            //				foreach (string text2 in list)
            //				{
            //					Console.WriteLine(text2);
            //					Process.Start("HqkDbImport.exe /ImportLdapUser " + text2);
            //				}
            //			}
            //			finally
            //			{
            //				List<string>.Enumerator enumerator;
            //				((IDisposable)enumerator).Dispose();
            //			}
            //		}
            //	}
            //	catch (Exception ex)
            //	{
            //		Console.WriteLine("Unexpected error: " + ex.Message);
            //	}
            //}
        }
    }
}