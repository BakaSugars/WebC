<?php
$con = mysql_connect("localhost","shujingwei","123456");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("test", $con);

mysql_query("DELETE FROM student WHERE name='alice'");


mysql_close($con);
?>