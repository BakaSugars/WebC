#coding=utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django import forms
from mydb.models import Student
from mydb.models import Problem
from mydb.models import Problem_Student
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import Queue
from challenge.submit2 import login,submit
#@login_required(redirect_field_name='base/login.html',login_url='login/')
taskq = Queue.Queue()
class AnswerForm(forms.Form):
	code = forms.CharField(
	required = True,
	label = u"代码框", 
	max_length = 10000,
	error_messages={'required':'请输入你的代码'},
	widget = forms.TextInput(
		attrs = {
		'placeholder':u"请将代码填写在此",
		}
	 ),
	)
@login_required
def getChallenge(request):
		problems = Problem.objects.all()
		print problems[0].id
		key = range(1,11)
		return render(request, 'challenge/getChallenge.html',{'problems': problems,'key':key})
@login_required	
def showProblem(request):
		code = request.POST.get('coding','')
		print "code is loading"	
		id = int(request.GET['id'])
		student = Student.objects.get(user = request.user)
		problem = Problem.objects.get(e_id = id)
		PS = Problem_Student.objects.filter(student = student,problem =problem)
		print len(PS)
		if len(code)<=0:
			if len(PS)==0:
				condition='no submit'
				spendtime = 'none'
				spendspace = 'none'
				submittime = 'none'
			else :
				condition=PS[0].problem_student_condition
				spendtime = PS[0].problem_student_spendtime
				spendspace = PS[0].problem_student_spendspace
				submittime = PS[0].problem_student_submittime
			print "coding at least 50byte"
		else:
			if len(PS) == 0:
				nwps=Problem_Student.objects.create(
				student = student,
				problem = problem,
				problem_student_code = code,
				problem_student_condition = 'submitted',
				)
				taskq.put(nwps.id)
				print taskq.qsize()
			else :
				PS[0].problem_student_code = code
				PS[0].save()
				taskq.put(PS[0].id)
				print taskq.qsize()
			login()
			while(taskq.qsize()!=0):
				psid = taskq.get()
				ps = Problem_Student.objects.get(id = psid)
				problemid = Problem.objects.get(id=ps.problem_id).e_id
				print problemid
				result = submit(problemid,ps.problem_student_code)
				ps.problem_student_submittime = result['submittime']
				ps.problem_student_condition = result['result']
				ps.problem_student_spendtime = result['spendtime']
				ps.problem_student_spendspace = result['spendspace']
				ps.save();
			condition = PS[0].problem_student_condition
			spendtime = PS[0].problem_student_spendtime
			spendspace = PS[0].problem_student_spendspace
			submittime = PS[0].problem_student_submittime
		
		
		
		colors = {'no submit':'blue','submit':'yellow','Accepted':'green','Compilation Error':'red','Wrong Answer':'pink','Memory Limit Exceeded':'gray','Time Limit Exceeded':'black'}
		color = colors[condition]
		return render(request, 'challenge/showProblem.html',{'problem': problem,'condition':condition,'color':color,'spendtime':spendtime,'spendspace':spendspace,'submittime':submittime})

# Create your views here.
