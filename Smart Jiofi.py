#!/usr/bin/env python
# coding: utf-8

# In[30]:


import urllib.request
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import re
import threading
import time
import winsound

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

# alert function
def alert():
    status = update()
    level = status['batterylevel']
    if int(level[:-1]) < 30 and status['batterystatus']=='Discharging':
        return 'low'
    if int(level[:-1]) > 95 and status['batterystatus']=='Discharging':
        return 'high'
    else:
        pass

# warn user about battery level
def warn():
    while True:
        alert()
        time.sleep(10)

#t = threading.Thread(target=warn,args=())
#t.start()

# GUI to show status
layout = [  [sg.Text('Device Status', font=('Helvetica', 15),size=(20, 2), justification='center')],
            [sg.Text(size=(30, 10), font=('Helvetica', 10), justification='center', key='-OUTPUT-')],
            [sg.T(' ' * 5), sg.Button('freeze', focus=True), sg.Quit()]]

window = sg.Window('Status board', layout)

timer_running, counter = True, 0

while True:                                
    event, values = window.read(timeout=10) 
    if event in (None, 'Quit'):             
        break
    elif event == 'freeze':
        timer_running = not timer_running
    if timer_running:
        try:
            status = update()
            level = status['batterylevel'] # Alert user to connect or disconnect charger to JIOFI
            if int(level[:-1]) < 30 and status['batterystatus']=='Discharging':
                winsound.Beep(500,1000)
                sg.Popup("Low battery")
            if status['batterystatus']=='Fully Charged':
                winsound.Beep(500,1000)
                sg.Popup("Battery level high")
            bat_status = 'Battery-Status:'+status['batterystatus']
            bat_status = bat_status +'\n'+'Battery-level:'+status['batterylevel']
            bat_status = bat_status +'\n'+'signal strength:'+status['signalstrength']
            bat_status = bat_status +'\n'+'Upload DataRate:'+status['ulCurrentDataRate']
            bat_status = bat_status +'\n'+'Download DataRate:'+status['dlCurrentDataRate']
            bat_status = bat_status +'\n'+'Connection Time:'+status['ConnectionTime']
            bat_status = bat_status +'\n'+'Connection Status:'+status['connectedStatus']
            bat_status = bat_status +'\n'+'No of Users :'+status['noOfClient']
            window['-OUTPUT-'].update(bat_status)
        except:
            pass
        counter += 1
window.close()


# In[ ]:




