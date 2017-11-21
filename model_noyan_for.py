import random
import requests
import urllib.parse
import urllib.request
from PIL import Image
import os
from time import time,strftime, localtime
import time as t
#下面值需要抓包更改
qid=str(16326759)#问卷ID
rnqian=str(3726693844)#问卷序列号
Length=str(48)#提交信息长度
for i in range(100):
	times=str(int(time()))
	t.sleep(10)
	timee=str(int(time()))
	t.sleep(3)
	timec=str(int(time() * 1000))
	rnhou=str(random.randint(10000000,99999999))
	header = {
    'Host': 'www.wjx.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 EXT/6d8a2f10c62d11e7gqpxa53987ed19aa47e3/2.4',    
	'Cookie':'.ASPXANONYMOUS=Se6Dlf-S0wEkAAAAMzEyZGYyZmUtYzBmYi00YWM3LWIyMTEtMTEzZWI0YzkzMmZhi6xL6iHoMTghIlPoznFqbYuLd1s1; SojumpSurvey=0102FF37CFE8842AD508FEFFD7E06FA62AD508000670002D00740065007300740000012F00FFE1A618AA5E20B4A360A7B782CD703DF66141E2F1; lllogcook=1; LastCheckUpdateDate=1; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1510570468; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1510570517; jac'+qid+'='+rnhou+'; CNZZDATA4478442=cnzz_eid%3D1240851277-'+times+'-%26ntime%3D'+timee,	
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Forwarded-For': str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255)),
    'Referer': 'https://www.wjx.cn/jq/'+qid+'.aspx',
    'Content-Length': Length,
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
	}
	thedata = {'submitdata': '1$1}2$3}3$1}4$1}5$4'}#******提交答案，需要改******
	url1='https://www.wjx.cn/handler/processjq.ashx?submittype=1&curID='+qid+'&t='+timec+'&starttime='+(str(strftime("%Y/%m/%d%H:%M:%S", localtime())).replace('/','%2F')).replace(':','%3A')+'&rn='+rnqian+'.'+rnhou+'&sd=http%3a%2f%2fwww.wjx.cn%2f'
	#改rn
	r = requests.post(url1, headers = header,data = thedata,allow_redirects=False)
	print(url1)
	print(r.text)
	t.sleep(100)
