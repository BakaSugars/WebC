<?php
$con = mysql_connect("localhost","shujingwei","123456");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("test", $con);

mysql_query("UPDATE student SET id='1024' WHERE name='jay' ");


mysql_close($con);
?>