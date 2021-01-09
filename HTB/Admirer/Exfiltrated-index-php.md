# Exfiltrated index.php

```text
MariaDB [admirerdata]> SELECT * FROM data;
+-----------------------------------------------------------------------------------------+
| text                                                                                    |
+-----------------------------------------------------------------------------------------+
| <!DOCTYPE HTML>                                                                         |
| <!--                                                                                    |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| -->                                                                                     |
| <html>                                                                                  |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                         $servername = "localhost";                                      |
|                         $username = "waldo";                                            |
|                         $password = "&<h5b~yK3F#{PaPB&dA}{H>";                          |
|                         $dbname = "admirerdb";                                          |
|                                                                                         |
|                         // Create connection                                            |
|                         $conn = new mysqli($servername, $username, $password, $dbname); |
|                         // Check connection                                             |
|                         if ($conn->connect_error) {                                     |
|                             die("Connection failed: " . $conn->connect_error);          |
|                         }                                                               |
|                                                                                         |
|                         $sql = "SELECT * FROM items";                                   |
|                         $result = $conn->query($sql);                                   |
|                                                                                         |
|                         if ($result->num_rows > 0) {                                    |
|                             // output data of each row                                  |
|                             while($row = $result->fetch_assoc()) {                      |
|                                 echo "<article class='thumb'>
";                        |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                             }                                                           |
|                         } else {                                                        |
|                             echo "0 results";                                           |
|                         }                                                               |
|                         $conn->close();                                                 |
|                     ?>                                                                  |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| </html>                                                                                 |
+-----------------------------------------------------------------------------------------+
123 rows in set (0.000 sec)
```

