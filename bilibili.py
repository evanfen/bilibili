# _*_ coding:utf-8_*_
import json
import requests
import re
import sys
import datatime
import time
def datetime_to_timestamp_in_milliseconds(d):
    current_milli_time=lamba:int(round(time.time()*1000)) #lamba是将函数进行缩小化
    return current_milli_time()


reload(sys)
sys.setfaultencoding("utf-8 ")#进行编码
urls=[]
head={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/873981/',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',}
    #url请求时浏览器给予的信息，进行伪装
    time1=time.time() #返回时间，不过返回的却是秒数

    for i in range(873981,873982):
        url='http://space.bilibili.com/ajax/member/GetInfo?mid='+str(i)
        urls.append(url)#urls为之前定义的列表
        #将要爬取的地址存储在列表中

proxies={
    #'http':'120,198.231.87:84,
    #"https":'http://219.133.31.120:8888'} #代理
    }

def getsource():
    payload={
    '_':datetime_to_timestamp_in_milliseconds(datetime.datetime.now())，
    'mid':url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=','')
        }
print payload
jscontent=requests.post("http://space.bilibili.com/ajax/member/GetInfo",headers=head,data=payload).content

print(jscontent)
time2=time.time()
jsDict=json.loads(jscontent)
if jsDict=json.loads(jscontent)
if jsDict['status']==True:
    jsDate=jsDict['Data']
    mid=jsData['mid']
    name=jsData['name']
    sex=jsData['sex']
    face=jsData['face']
    coins=jsData['coins']
    regtime=jsData['regtime']
    js