from django.shortcuts import render
from mydb.models import Student
from django.http import HttpResponse,HttpResponseRedirect

	
def getHomework(request):
		return render(request,'getcontest/getHomework.html')
	
def getNewProblem(request):
		return render(request, 'getcontest/getNewProblem.html')
def getImprove(request):
		return render(request, 'getcontest/getImprove.html')
def getRankImprove(request):
		return render(request, 'getcontest/getRankImprove.html')
	

# Create your views here.
