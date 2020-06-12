import urllib.request
from bs4 import BeautifulSoup
import re
import threading
import time
import winsound
from win10toast import ToastNotifier 

# getting info from jiofi webpage
def scan():
    try:
        page = urllib.request.urlopen('http://jiofi.local.html')
        data=page.read()
        soup=BeautifulSoup(data,'html.parser')
        jiofi=soup.find_all('input')
        return jiofi
    except:
        time.sleep(10)
        scan()

# extract info
def update():
    status={}
    for i in scan():
        try:
            ids = re.findall(r'["][\w\s]+["]',str(i))
            val_begin = re.search(r'value=',str(i)).end()
            value = str(i)[val_begin+1:-3]
            status[ids[0][1:-1]]=value
        except AttributeError:
            pass
    return status



n = ToastNotifier() 
while True:
    time.sleep(30)
    status = update()
    level = status['batterylevel'] 
    if int(level[:-1]) < 30 and status['batterystatus']=='Discharging':
        n.show_toast(" JIOFI Low battery", "Connect charger", duration = 10 )
    if status['batterystatus']=='Fully Charged':
        n.show_toast(" JIO Fully Charged", "Unplug charger", duration = 10 )


