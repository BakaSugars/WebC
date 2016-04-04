<?php
  class
   Mysql(
       private
       $host;//地址
       private
       $root;//用户名
       private
       $password;//密码
       private
       $database;//数据库名
       function 
       __construct($host,$root,$password,$database){
      $this->host
      =$host;
      $this->root
      =$root;
      $this->password
      =$password;
      $this->database
      =$database;
      $this->connect();//构造类对象的同时连接数据库
      }//构造函数
      function
      connect(){
      $this->conn
      =mysql_connect($this->host,$this->root,$this->password) or die("DB 
      Connect Error!".mysql_error());
      mysql_select_db($this->database,$this->conn);
      mysql_query("set name utf8");
      }//连接数据库操作
      function
       dbClose(){
       mysql_close($this->conn);
       	}	       	
			function
			 query($sql){		
			 return
			 mysql_query($sql);
			}//封装函数			        		
			function
			 myArray($result){
			 return
			 mysql_fetch_array($result);
			}//封装函数				
			function
			 rows($result){
			 return
			 mysql_num_rows($result);
			}//封装函数		
      function
		  select($tableName,$condition){
		  return
		 $this->query("SELECT
		 * FROM $tableName $condition");
      }//数据查找函数
     function
     insert($tableName,$fields,$value){
     $this->query("INSERT
     INTO $tableName $fields VALUES$value");
     echo "sucess";
     }//数据插入函数
     function
 			update($tableName,$change,$condition){
    	$this->query("UPDATE
 			$tableName SET $change $condition");
     }//数据修改函数
     function
     delete($tableName,$condition){
     $this->query("DELETE
     FROM $tableName $condition");
		 }//数据删除函数
     }//创建Mysql类
     $db
     =new Mysql("localhost_3306","shujingwei","123456","test");//实例化操作
     >
      