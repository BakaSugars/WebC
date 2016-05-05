"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from thenews import views as thenews_views
from base import views as base_views
from getcontest import views as contest_views
from challenge import views as challenge_views
from contestdata import views as contestdata_views
from links import views as links_views
from users import urls #for users
import settings
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', thenews_views.getFreshNews, name='getFreshNews'),
	url(r'^login', base_views.login, name = 'login'),
	url(r'^regist', base_views.regist, name = 'regist'),
	url(r'^index', base_views.index, name = 'index'),
	url(r'^logout', base_views.logout, name = 'logout'),
	url(r'^getnews/$', thenews_views.getFreshNews),
	url(r'^getnews-freshnews', thenews_views.getFreshNews, name = 'getFreshNews' ),
	url(r'^getnews-freshproblem', thenews_views.getFreshProblem, name = 'getFreshProblem' ),
	url(r'^getnews-freshcontest', thenews_views.getFreshContest, name = 'getFreshContest' ),
	url(r'^getnews-freshrank', thenews_views.getFreshRank, name = 'getFreshRank' ),
	url(r'^getcontest/$',contest_views.getHomework),
	url(r'^getcontest-getHomework', contest_views.getHomework, name = 'getHomework'),
	url(r'^getcontest-getNewProblem', contest_views.getNewProblem, name = 'getNewProblem'),
	url(r'^getcontest-getImprove', contest_views.getImprove, name = 'getImprove'),
	url(r'^getcontest-getRankImprove', contest_views.getRankImprove, name = 'getRankImprove'),
	url(r'^getchallenge', challenge_views.getChallenge, name = 'getChanllenge'),
	url(r'^getcontestdata' , contestdata_views.getContestData, name = 'getContestData'),
	url(r'^getlink/$', links_views.getLinks, name = 'getLinks'),
	url(r'^problem/$',challenge_views.showProblem, name = 'showProblem'),
	#url(r'^accounts/', include('users.urls')),
	url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }), 	
]

