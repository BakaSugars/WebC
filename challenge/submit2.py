#coding:utf-8
import re,urllib,urllib2,cookielib
from bs4 import BeautifulSoup
def login():
	#模拟登录 
	cj = cookielib.CookieJar() 
	#用户名和密码 
	post_data = urllib.urlencode({'username': 'asjw789456123', 'userpass': '2515436', 'login': 'Sign In'}) 
	#登录路径 
	path = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
	opener.addheaders = [('User-agent', 'Opera/9.23')] 
	urllib2.install_opener(opener) 
	req = urllib2.Request(path, post_data) 
	conn = urllib2.urlopen(req)
def submit(problemid,code):
	usercode ={
			'check':0,
			'problemid':problemid,
			'language':2,
			'usercode':code,
		}
	req2 = urllib2.Request('http://acm.hdu.edu.cn/submit.php?action=submit', urllib.urlencode(usercode)) 
	#查看表单提交后返回内容 
	conn2 = urllib2.urlopen(req2)
	#获取提交信息
	req3 = urllib2.Request('http://acm.hdu.edu.cn/status.php?user=asjw789456123')
	htmll =  urllib2.urlopen(req3).read()
	soup = BeautifulSoup(htmll,'html.parser',from_encoding='utf-8')
	contain_nodes = soup.find_all('td',height= '22px')
	submit_id_node = contain_nodes[0]
	print submit_id_node.get_text()
	submit_time_node = submit_id_node.next_sibling
	print submit_time_node.get_text()
	result_node = submit_time_node.next_sibling
	print result_node.get_text()
	spendtime_node = result_node.next_sibling.next_sibling
	print spendtime_node.get_text()
	spendspace_node = spendtime_node.next_sibling
	print spendspace_node.get_text()
	result = {
	'id':submit_id_node.get_text(),
	'submittime':submit_time_node.get_text(),
	'result':result_node.get_text(),
	'spendtime':spendtime_node.get_text(),
	'spendspace':spendspace_node.get_text(),
	}
	return result