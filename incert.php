<?php
$con = mysql_connect("localhost","shujingwei","123456");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("test", $con);

mysql_query("INSERT INTO student (name, id) 
VALUES ('jay', 1003)");

mysql_query("INSERT INTO student (name, id) 
VALUES ('alice', 1004)");

mysql_close($con);
?>