from django.shortcuts import render
from mydb.models import Student
from django.http import HttpResponse,HttpResponseRedirect

def getContestData(request):
		return render(request, 'contestdata/getContestData.html')
# Create your views here.
