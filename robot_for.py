import random
import requests
import urllib.parse
import urllib.request
from PIL import Image
import os
import random
from time import time,strftime, localtime
import time as t
qid=str(16454455)#问卷ID
rnqian=str(2063096382)#问卷序列号
for z in range(4):
	times=str(int(time()))#打开问卷时间戳
	t.sleep(10)
	timee=str(int(time()))#提交问卷时间戳
	t.sleep(3)
	timec=str(int(time() * 1000))#服务器响应时间戳
	rnhou=str(random.randint(10000000,99999999))#答案序列号
	header = {
	    'Host': 'sojump.com',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.3397.1012 Safari/537.36 EXT/9139f0308ece11e7b499gqpxeb2237921fdb/2.1',    
		'Cookie':'UM_distinctid=15e37f4faa976-0aa5531ef3840e-5d6c0014-100200-15e37f4faaa29b; .ASPXANONYMOUS=enuYfdpY0wEkAAAAY2VkNmUyNWQtNWFkZC00MzEyLWE0NmUtYTJjNTMyY2FhODFhz2ObKZ1zCtOQVmcPSomgwzb5dWQ1;SojumpABX_251=1; jac'+qid+'='+rnhou+'; CNZZDATA4478442=cnzz_eid%3D1240851277-'+times+'-%26ntime%3D'+timee,	
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Referer': 'https://sojump.com/jq/'+qid+'.aspx',
	    'Content-Length': '48',#提交信息长度
	    'X-Forwarded-For': '8.8.8.8',
	    'Connection': 'keep-alive',
	    'Pragma': 'no-cache',
	    'Cache-Control': 'no-cache'
	}
	thedata = {'submitdata': '1$'+str(random.randint(1,5))+'}2$'+str(random.randint(1,10))+'}3$'+str(random.randint(1,3))+'}4$'+str(random.randint(1,4))+'}5$1<'+str(random.randint(1,9))+',2<'+str(random.randint(1,5))+',3<'+str(random.randint(1,5))+',4<'+str(random.randint(1,5))+',5<'+str(random.randint(1,5))+',6<'+str(random.randint(1,5))+',7<'+str(random.randint(1,5))+',8<'+str(random.randint(1,5))+',9<'+str(random.randint(1,5))+'}6$'+str(random.randint(1,3))+'}7$'+str(random.randint(1,7))+'}8$'+str(random.randint(1,3))+'|'+str(random.randint(3,6))+'|'+str(random.randint(7,9))+'}9$'+str(random.randint(1,4))+'|'+str(random.randint(5,7))+'}10$'+str(random.randint(1,3))+'}11$'+str(random.randint(1,4))+'}12$1<1,2<4,3<6,4<3,5<8,6<3,7<6,8<5}13$'+str(random.randint(1,4))+'|'+str(random.randint(5,7))+'}14$2|5}15$'+str(random.randint(1,2))+'}16$'+str(random.randint(1,2))+'}17$'+str(random.randint(1,2))+'}18$'+str(random.randint(1,2))+'}19$'+str(random.randint(1,2))+'}20$'+str(random.randint(1,4))+'}21$'+str(random.randint(1,3))}
	#问卷答案
	url1='https://sojump.com/handler/processjq.ashx?submittype=1&curID='+qid+'&t='+timec+'&starttime='+(str(strftime("%Y/%m/%d%H:%M:%S", localtime())).replace('/','%2F')).replace(':','%3A')+'&rn='+rnqian+'.'+rnhou+'&sd='+('https://sojump.com/'.replace('/','%2F')).replace(':','%3A')
        #改rn
	r = requests.post(url1, headers = header,data = thedata)
	print(r.text)
	t.sleep(2000)
