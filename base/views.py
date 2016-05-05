#coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from mydb.models import Student

import time #延迟执行

CHOICE_CLASS = (("c1","class1"),("c2","class2"),("c3","class3"),("c4","class4"))
CHOICE_GRADE = (("g1","grade1"),("g2","grade2"),("g3","grade3"),("g4","grade4"))
def showBase(request):
	return render(request, 'base/base.html')
class StudentForm(forms.Form):
	username = forms.CharField(label='用户名',max_length = 100)
	password = forms.CharField(label = '密码', widget = forms.
	PasswordInput())
	name = forms.CharField(label = '姓名', max_length = 30)
	teachername = forms.CharField(label = '教师名', max_length = 30)
	theclass = forms.CharField(label = '班级', max_length = 30)
	teacher_id = forms.CharField(label = '教师id', max_length =50)

class LoginForm(forms.Form):
	username = forms.CharField(
	required = True,
	label = u"用户名", 
	max_length = 100,
	error_messages={'required':'请输入用户名'},
	widget = forms.TextInput(
		attrs = {
		'placeholder':u"用户名",
		}
	 ),
	)
	password = forms.CharField(
	required = True,
	label = u"密码",
	error_messages={'required':u'请输入密码'},
	widget = forms.PasswordInput(
		attrs ={
			'placeholder':u"密码",
		}
	 ),
	)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"用户名和密码为必填项")
		else:
			cleaned_data = super(LoginForm,self).clean()
class RegForm(forms.Form):
	username = forms.CharField(
	required = True,
	label = u"用户名", 
	max_length = 100,
	error_messages={'required':'请输入用户名'},
	widget = forms.TextInput(
		attrs = {
			'placeholder':u"用户名",
		}
	 ),
	)
	password = forms.CharField(
	required = True,
	label = u"密码",
	max_length = 50,
	error_messages={'required':u'请输入密码'},
	widget = forms.PasswordInput(
		attrs ={
			'placeholder':u"密码",
		}
	 ),
	)

	student_name = forms.CharField(
	required = True,
	label = u"姓名",
	max_length = 50,
	error_messages={'required':u'请输入姓名'},
	widget = forms.TextInput(
		attrs ={
			'placeholder':u"姓名",
		}
	 ),
	)
	student_id = forms.CharField(
	required = True,
	label = u"id",
	max_length = 50,
	error_messages={'required':u'请输入id'},
	widget = forms.TextInput(
		attrs ={
			'placeholder':u"id",
		}
	 ),
	)
	
	student_grade = forms.ChoiceField(
		choices = CHOICE_GRADE,
		required = True,
		label = u"年级",
		error_messages={'required':u'请选择年级'},
		widget = forms.Select(
			attrs ={
		
		}
	 ),
	)
	student_class = forms.ChoiceField(
	choices = CHOICE_CLASS,
	required = True,
	label = u"班级",
	error_messages={'required':u'请选择班级'},
	widget = forms.Select(
		attrs ={
		}
	 ),
	)
	
	student_email = forms.EmailField(
	required = True,
	label = u"邮箱",
	max_length = 50,
	error_messages={'required':u'请输入邮箱'},
	widget = forms.TextInput(
		attrs ={
			'placeholder':u"邮箱",
		}
	 ),
	)

def regist(request):
	print 'in regist'
	#如果是GET方式的情况
	if request.method =='GET':
		print 'in GET'
		form = RegForm()
		return render_to_response('base/register.html',RequestContext(request,{'form':form,}))
	#如果是以POST方式的情况
	else:
		print 'in POST'
		form = RegForm(request.POST)
		if form.is_valid():
			#获得表单数据
			print 'form is cvalid'
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			student_name = request.POST.get('student_name','')
			student_grade = request.POST.get('student_grade','')
			student_class = request.POST.get('student_class','')
			student_email = request.POST.get('student_email','')
			studentid = request.POST.get('student_id','')
			firstname = student_name[0]
			lastname = student_name[1:]
			#添加到数据库
			print 'add in database'

			usr = User.objects.create_user(username,student_email,password)
			usr.first_name = firstname
			usr.last_name = lastname
			usr.save()
			Student.objects.create(
			user = usr,
			studentid = studentid, 
			student_name = student_name,
			#student_teachername = student_teachername,
			student_class = student_class,
			student_grade = student_grade,
			student_point = 0,
			student_rank = 0,
			#student_teacherid = student_teacherid
			)
			return HttpResponse('regist success <a href = "/login">回到登陆界面</a>')

		else:
			print 'form is not valid'
			form = RegForm()
		return render_to_response('base/register.html',{'form':form},context_instance = RequestContext(request))
def login(request):
	#如果是以get方式获取则重新获取当前页面
	if request.method =='GET':
		form = LoginForm()
		return render_to_response('base/login.html',RequestContext(request,{'form':form,}))
	#如果是以POST方式的情况
	else:
			form = LoginForm(request.POST)
			if form.is_valid():
				#获取表单用户密码
				username = request.POST.get('username','')
				password = request.POST.get('password','')
				#把获取表单的用户名传递给session对象
				#request.session['username'] = username
				#获取的表单数据与数据库进行比较
				#user = Student.objects.filter(student_id__exact = username,student_password__exact = password)
				user = auth.authenticate(username = username, password = password)	
				print Student.objects.get(user = user).student_name
				if user is not None and user.is_active:
					#比较成功跳转到主界面
					#response = HttpResponseRedirect('/getnews')
					#将username写入浏览器cookie，失效时间为3600
					#response.set_cookie('username',username,3600)
					#return response
					auth.login(request,user)
					return render_to_response('thenews/freshnews.html',RequestContext(request))
				else:
					#比较失败，还在login
					return render_to_response('base/login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
			else:
				return render_to_response('base/login.html',RequestContext(request,{'form':form,}))
	#else:
	#	uf = LoginForm()
	#return render_to_response('base/login.html',{'uf':uf},context_instance = RequestContext(request))
	
def index(request):
	username = request.COOKIES.get('username','')
	print 'username is '+username
	student = Student.objects.get(student_id = username)
	return render_to_response('base/index.html',{'username':student[0]})
	
def logout(request):
	response = HttpResponse('logout !!  <a href = "/getnews">回到主页</a>')
	#清理cookie中保存的username
	response.delete_cookie('username')
	auth.logout(request)
	return response
# Create your views here.
