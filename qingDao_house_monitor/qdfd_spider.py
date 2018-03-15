#! /usr/bin/python

import os
import sys
import time;
import requests
from bs4 import BeautifulSoup
#import xlrd
import csv,codecs
import random
from faker import Faker
from faker import Factory

fake = Factory.create()

reload(sys)
sys.setdefaultencoding('utf-8')

qd_url='http://www.qdfd.com.cn/qdweb/realweb/indexnew.jsp'

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Host':'www.qdfd.com.cn',
    'Pragma':'no-cache',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
#
#'User-Agent': fake.user_agent()

proxy_ips = [
'192.168.145.128',
'192.168.15.128',
'192.168.145.18',
'192.168.145.28'
] 

def random_proxies():
    ip_index = random.randint(0, len(proxy_ips)-1)
    res = { 'http': proxy_ips[ip_index] }
    return res

def parseTable(bsoup,in_data,file,time):
    new_h = bsoup.find('div',class_=in_data)
    
    #print("test:")
    #print(new_h)
    type = new_h.find('div',class_='con2ls mg2 xi18 bai cen')
    writer.writerow("")
    writer.writerow([type.text,localtime])
    
    colum = 5
    i = 0
    recoder = []
    for d in new_h.find_all('td'):
        recoder.append(d.text)
        i += 1
        if(i == 5 ):
            i = 0
            #print(line)
            writer.writerow(recoder)
            recoder=[]


if __name__ == '__main__':

    localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
   
    f = codecs.open('./today-'+localtime+'.csv', 'wb', 'utf_8_sig')  
    writer = csv.writer(f)
    
    res = requests.get(qd_url,headers=headers,timeout=5)
   # print(res.content)
    try:
        print (res.status_code)
    except res.exceptions.HTTPError as e:
        print( "Error: " + str(e))
	exit()

    soup = BeautifulSoup(res.content, 'html.parser')
    #title = soup.find('span', attrs={'class': 'vol-title'})
    #print(soup.prettify())
    
    parseTable(soup,"con2l f",f,localtime)
    
    parseTable(soup,"con2l r",f,localtime)




