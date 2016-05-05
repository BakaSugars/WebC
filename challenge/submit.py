#! /usr/bin/env python
#coding:utf-8
 
import sys
import re
import urllib2
import urllib
import httplib
import cookielib
from bs4 import BeautifulSoup
import xlrd
from xlutils.copy import copy
import requests
## 这段代码是用于解决中文报错的问题  


reload(sys)  
sys.setdefaultencoding("utf8")  
loginurl = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
logindomain = 'http://acm.hdu.edu.cn/'
excel_problem_info = xlrd.open_workbook("D:\Data\problem_information.xls")
print excel_problem_info
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}

class Login(object):
     
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''

 
        self.cj = cookielib.LWPCookieJar()            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)    
     
    def setLoginInfo(self,username,password,domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain
 
    def login(self):
        '''登录网站'''
        loginparams = {'userpass':self.pwd,'username':self.name,'login':'Sign In' }  
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)  
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read() 
        
def getProblemInformation(problem_number):
    req = urllib2.Request('http://acm.hdu.edu.cn/showproblem.php?pid=%d'%problem_number,headers=headers)      
    problem = urllib2.urlopen(req)
    return problem.read()
def addProblemInfo(problem_id):
    rb = xlrd.open_workbook('D:\\Data\problem_information.xls')
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    HTML = getProblemInformation(problem_id)
    soup = BeautifulSoup(HTML,'html.parser',from_encoding='utf-8')
    
    e_id = problem_id
    e_name = soup.find('h1',style='color:#1A5CC8').get_text()
    dif = 1+(problem_id-1000)/200
    e_point = dif*10
    contain_tnodes = soup.find_all('div',class_='panel_title')
    contain_nodes = soup.find_all('div',class_ = 'panel_content')
    contain = contain_tnodes[0].get_text()+'\n'+contain_nodes[0].get_text()+'\n'+contain_tnodes[1].get_text()+'\n'+contain_nodes[1].get_text()+'\n'+contain_tnodes[2].get_text()+'\n'+contain_nodes[2].get_text()+'\n'+contain_tnodes[3].get_text()+'\n'+contain_nodes[3].get_text()
    output = contain_nodes[4].get_text()
    
    ws.write(e_id-999, 0, e_id)
    ws.write(e_id-999, 1, e_name)
    ws.write(e_id-999, 2, e_point)
    ws.write(e_id-999, 3, contain)
    ws.write(e_id-999, 4, output) 
    ws.write(e_id-999, 5, dif)
    wb.save('D:\\Data\problem_information.xls')

def getSubmit(problemid,code):
	userlogin = Login()
	username = 'asjw789456123'
	password = '2515436'
	domain = logindomain
	userlogin.setLoginInfo(username,password,domain)

	req = urllib2.Request('http://acm.hdu.edu.cn/submit.php?pid=%d'%problemid,headers=headers)      
	usercode = urllib.urlencode({
		'username':'asjw789456123',
		'password':'2515436',
		'check':0,
		'problemid':str(problemid),
		'language':2,
		'usercode':code,
	})
	
	r = requests.post("http://acm.hdu.edu.cn/submit.php?action=submit",data=usercode)
	userlogin.login()
	s = requests.session()
	r = s.post("http://acm.hdu.edu.cn/submit.php?action=submit",data=usercode)
	'''
	conn = httplib.HTTPConnection("acm.hdu.edu.cn")
	conn.request(method = 'POST', url = "/submit.php?action=submit",headers = headers)
	response = conn.getresponse()
	if response.status == 302:
		print "提交成功"
	else :
		print "发布失败"
	'''
if __name__ == '__main__': 
    getSubmit(1001,"#include<stdio.h>#include<iostream>using namespace std;int a ,b;int main(int argv, char *argc[]){while(cin>>a>>b){cout<<a+b<<endl;}}")