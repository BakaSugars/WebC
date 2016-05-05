from django.shortcuts import render

def getLinks(request):
	return render(request, 'links/getLinks.html')
# Create your views here.
