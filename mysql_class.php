<?php
  class
   Mysql(
       private
       $host;//��ַ
       private
       $root;//�û���
       private
       $password;//����
       private
       $database;//���ݿ���
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
      $this->connect();//����������ͬʱ�������ݿ�
      }//���캯��
      function
      connect(){
      $this->conn
      =mysql_connect($this->host,$this->root,$this->password) or die("DB 
      Connect Error!".mysql_error());
      mysql_select_db($this->database,$this->conn);
      mysql_query("set name utf8");
      }//�������ݿ����
      function
       dbClose(){
       mysql_close($this->conn);
       	}	       	
			function
			 query($sql){		
			 return
			 mysql_query($sql);
			}//��װ����			        		
			function
			 myArray($result){
			 return
			 mysql_fetch_array($result);
			}//��װ����				
			function
			 rows($result){
			 return
			 mysql_num_rows($result);
			}//��װ����		
      function
		  select($tableName,$condition){
		  return
		 $this->query("SELECT
		 * FROM $tableName $condition");
      }//���ݲ��Һ���
     function
     insert($tableName,$fields,$value){
     $this->query("INSERT
     INTO $tableName $fields VALUES$value");
     echo "sucess";
     }//���ݲ��뺯��
     function
 			update($tableName,$change,$condition){
    	$this->query("UPDATE
 			$tableName SET $change $condition");
     }//�����޸ĺ���
     function
     delete($tableName,$condition){
     $this->query("DELETE
     FROM $tableName $condition");
		 }//����ɾ������
     }//����Mysql��
     $db
     =new Mysql("localhost_3306","shujingwei","123456","test");//ʵ��������
     >
      