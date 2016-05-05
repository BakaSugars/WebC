from django.shortcuts import render
def getNews(request):
	print 'get in news'
	return render(request, 'thenews/thenews.html')
	
def getFreshNews(request):
	print 'get in fresh news'
	return render(request, 'thenews/freshnews.html')
	
def getFreshProblem(request):
	print 'get in freshproblem'
	return render(request, 'thenews/freshproblem.html')
	
def getFreshContest(request):
	print 'get in contest'
	return render(request, 'thenews/freshcontest.html')
	
def getFreshRank(request):
	print 'get in rank'
	return render(request, 'thenews/freshrank.html')
# Create your views here.
