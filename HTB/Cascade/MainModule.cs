using System;
using System.Collections;
using System.Data.SQLite;
using System.DirectoryServices;
using CascAudiot.My;
using CascCrypto;
using Microsoft.VisualBasic.CompilerServices;

namespace CascAudiot
{
	// Token: 0x02000008 RID: 8
	[StandardModule]
	internal sealed class MainModule
	{
		// Token: 0x0600000F RID: 15 RVA: 0x00002128 File Offset: 0x00000328
		[STAThread]
		public static void Main()
		{
			if (MyProject.Application.CommandLineArgs.Count != 1)
			{
				Console.WriteLine("Invalid number of command line args specified. Must specify database path only");
				return;
			}
			checked
			{
				//using (SQLiteConnection sqliteConnection = new SQLiteConnection("Data Source=" + MyProject.Application.CommandLineArgs[0] + ";Version=3;"))
				{
					string str = string.Empty;
					string password = string.Empty;
					string str2 = string.Empty;
					try
					{
						//sqliteConnection.Open();
						//using (SQLiteCommand sqliteCommand = new SQLiteCommand("SELECT * FROM LDAP", sqliteConnection))
						{
							//using (SQLiteDataReader sqliteDataReader = sqliteCommand.ExecuteReader())
							{
								//sqliteDataReader.Read();
								//str = Conversions.ToString(sqliteDataReader["Uname"]);
								//str2 = Conversions.ToString(sqliteDataReader["Domain"]);
                                //string encryptedString = Conversions.ToString(sqliteDataReader["Pwd"]);
                                string encryptedString = "BQO5l5Kj9MdErXx6Q6AGOw==";

                                try
								{
									password = Crypto.DecryptString(encryptedString, "c4scadek3y654321");
                                    Console.WriteLine(password);

                                }
								catch (Exception ex)
								{
									Console.WriteLine("Error decrypting password: " + ex.Message);
									return;
								}
							}
						}
						//sqliteConnection.Close();
					}
					catch (Exception ex2)
					{
						Console.WriteLine("Error getting LDAP connection data From database: " + ex2.Message);
						return;
					}
					int num = 0;
					using (DirectoryEntry directoryEntry = new DirectoryEntry())
					{
						directoryEntry.Username = str2 + "\\" + str;
						directoryEntry.Password = password;
						directoryEntry.AuthenticationType = AuthenticationTypes.Secure;
						using (DirectorySearcher directorySearcher = new DirectorySearcher(directoryEntry))
						{
							directorySearcher.Tombstone = true;
							directorySearcher.PageSize = 1000;
							directorySearcher.Filter = "(&(isDeleted=TRUE)(objectclass=user))";
							directorySearcher.PropertiesToLoad.AddRange(new string[]
							{
								"cn",
								"sAMAccountName",
								"distinguishedName"
							});
							using (SearchResultCollection searchResultCollection = directorySearcher.FindAll())
							{
								Console.WriteLine("Found " + Conversions.ToString(searchResultCollection.Count) + " results from LDAP query");
								//sqliteConnection.Open();
								try
								{
									try
									{
										foreach (object obj in searchResultCollection)
										{
											SearchResult searchResult = (SearchResult)obj;
											string value = string.Empty;
											string value2 = string.Empty;
											string value3 = string.Empty;
											if (searchResult.Properties.Contains("cn"))
											{
												value = Conversions.ToString(searchResult.Properties["cn"][0]);
											}
											if (searchResult.Properties.Contains("sAMAccountName"))
											{
												value2 = Conversions.ToString(searchResult.Properties["sAMAccountName"][0]);
											}
											if (searchResult.Properties.Contains("distinguishedName"))
											{
												value3 = Conversions.ToString(searchResult.Properties["distinguishedName"][0]);
											}
											//using (SQLiteCommand sqliteCommand2 = new SQLiteCommand("INSERT INTO DeletedUserAudit (Name,Username,DistinguishedName) VALUES (@Name,@Username,@Dn)", sqliteConnection))
											{
												/* sqliteCommand2.Parameters.AddWithValue("@Name", value);
												sqliteCommand2.Parameters.AddWithValue("@Username", value2);
												sqliteCommand2.Parameters.AddWithValue("@Dn", value3);
												num += sqliteCommand2.ExecuteNonQuery(); */
											}
										}
									}
									finally
									{
										IEnumerator enumerator;
										/*if (enumerator is IDisposable)
										{
											(enumerator as IDisposable).Dispose();
										}*/
									}
								}
								finally
								{
									//sqliteConnection.Close();
									Console.WriteLine("Successfully inserted " + Conversions.ToString(num) + " row(s) into database");
								}
							}
						}
					}
				}
			}
		}

		// Token: 0x04000008 RID: 8
		private const int USER_DISABLED = 2;
	}
}
