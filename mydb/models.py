# coding:utf8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User #测试拓展User的profile model属性
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser) #NEW
from django.conf import settings
#学生表，自定义Django中的User Model
'''
class Student(AbstractBaseUser):
	username = models.CharField(length = 50, unque = True)
	student_id = models.CharField(max_length = 50, unique = True)
	student_name = models.CharField(max_length = 50)
	student_teacherid = models.CharField(max_length = 50)
	student_teachername = models.CharField(max_length = 30)
	student_class = models.CharField(max_length = 30)
	studnet_grade = models.CharField(max_length = 30)
	student_point = models.IntegerField()
	student_rank = models.IntegerField()
	student_email = models.EmailFiled(max_length = 100, unique = True)#NEW
	def __unicode__(self):
		return self.student_name
#添加学生的用户操作类
class StudentManage(BaseUserManager):
	def create_student(self, name, email, password = None):
		if not email:
			raise ValueError("Users must have an email address")
	student = self.model(name = name, email = UserManager.normalize_email(email))
	student.set_password(password) #使用User自带的密码加密设置密码
	student.save(using = self._db)
	return student
	
	def create_superuser(self, name, email, password = None):
		
		user = self.create_student(name, email, password)
		user.is_admin = True
		user.save(using = self._db)
		return user
'''
class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, unique = True)
	studentid = models.CharField(max_length = 50, unique = True)
	student_name = models.CharField(max_length = 50)
	student_teacherid = models.CharField(max_length = 50)
	student_teachername = models.CharField(max_length = 30)
	student_class = models.CharField(max_length = 30)
	student_grade = models.CharField(max_length = 30)
	student_point = models.IntegerField()
	student_rank = models.IntegerField()
	def __unicode__(self):
		return self.student_name
class Teacher(models.Model):
	teacher_id = models.IntegerField()
	teacher_password = models.CharField(max_length = 30)
	
class Problem(models.Model):
	e_id = models.IntegerField()
	e_name = models.TextField()
	e_point = models.IntegerField()
	contain = models.TextField()
	output = models.TextField()
	dif = models.IntegerField()
	def __unicode__(self):
		return self.e_name
	
class Problem_Student(models.Model):
	problem = models.ForeignKey(Problem, null = True)
	student = models.ForeignKey(Student, null = True)
	problem_student_code = models.TextField()
	problem_student_review = models.TextField(null = True)
	problem_student_condition = models.TextField()
	problem_student_submittime = models.CharField(max_length = 50, null = True)
	problem_student_spendtime = models.CharField(max_length = 50, null = True)
	problem_student_spendspace = models.CharField(max_length = 50, null =True)
	

class SmallTest(models.Model):
	name = models.CharField(max_length = 30)
	age = models.IntegerField()
	
	
	

# Create your models here.
