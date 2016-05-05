from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hellow(request):
	context      = {}
	context['hello'] = 'Hellow World'
	return render(request, 'hello.html',context)
	#return HttpResponse("Hello world")