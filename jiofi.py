
# coding: utf-8

# In[37]:

import urllib.request
import requests 
from bs4 import BeautifulSoup
import winsound
import time

page = urllib.request.urlopen('http://jiofi.local.html')
data=page.read()
soup=BeautifulSoup(data,'html.parser')
jiofi=soup.find_all('input')
jiofi=str(jiofi[0])

def status():
    for k in range(11):
        s=jiofi.split('\n')[k]
        s=s.split()
        tag=s[1]
        value=s[-1]
        print(tag[s[1].find('=')+2:-1],"--->",value[s[-1].find('=')+2:-2])
        return

def battery():
    s=jiofi.split('\n')[1]
    s=s.split()
    tag=s[1]
    value=s[-1]
    percent=value[s[-1].find('=')+2:-2]
    remaining=int(percent[0:-1])
    print("left ",percent)  
    return

def warn():
    s=jiofi.split('\n')[1]
    s=s.split()
    tag=s[1]
    value=s[-1]
    percent=value[s[-1].find('=')+2:-2]
    remaining=int(percent[0:-1])
    if remaining < 50:
        winsound.Beep(300,1000)
    return

        
def help():
    print("use status function without any args to know status")
    print("use battery function without any args to know left percentage")
    print("use alert function without any args to get alert is battery goes below 30%")
    
def alert():
    while 1:
        warn()
        time.sleep(1)


# In[38]:



