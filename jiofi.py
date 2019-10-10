import urllib.request
import requests 
from bs4 import BeautifulSoup
import winsound
import ctypes 

def scan():
    try:
        page = urllib.request.urlopen('http://jiofi.local.html')
        data=page.read()
        soup=BeautifulSoup(data,'html.parser')
        jiofi=soup.find_all('input')
        jiofi=str(jiofi[0])
        return jiofi
    except:
        ctypes.windll.user32.MessageBoxW(0, "Not connected to jiofi ", "Program Exitting..", 1)
        winsound.Beep(300,1000)
        exit()

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

def fullalert(): 
    ctypes.windll.user32.MessageBoxW(0, "Your JioFi router is fully charged ", "Unplug charger", 1)
    winsound.Beep(100,1000)
    exit()
    
def lowalert():   
    ctypes.windll.user32.MessageBoxW(0, "Your JioFi charge going low ", "plug charger", 1)
    winsound.Beep(100,1000)
    exit()

def warn():
    jiofi=scan()
    s=jiofi.split('\n')[1]
    s=s.split()
    tag=s[1]
    value=s[-1]
    percent=value[s[-1].find('=')+2:-2]
    remaining=int(percent[0:-1])
    if remaining < 20:
        lowalert()
    if remaining == 100:
        fullalert()
    else:
        alert()
    return


        
def help():
    print("use status function without any args to know status")
    print("use battery function without any args to know left percentage")
    print("use alert function without any args to get alert is battery goes below 20%")
    
def alert():
        warn()
        
alert()