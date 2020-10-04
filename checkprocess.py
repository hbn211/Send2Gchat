# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:55:30 2020

@author: Heriberto
"""
import psutil,time

import sys
sys.path.append(r'C:/Send2Gchat')
import IronDrive

def check():
    st = "no"
    # time.sleep(60)
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if p.info['name'] == "ansysedt.exe":
            st = "yes"
            break
            #print("yes", (p.info['name']))
    return st

print("Monitoring ANSYS HFSS!!!")
while(1):
    st = check()
    if st == "no":
        break
    time.sleep(300)#5min
IronDrive.status("HFSS was closed!!!")
print("HFSS was closed!!!")