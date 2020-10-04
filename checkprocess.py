# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:55:30 2020

@author: Heriberto
"""
# import psutil
import time

import ctypes

import sys
sys.path.append(r'C:/Send2Gchat')
import IronDrive

# def checkprocess():
#     st = "no"
#     # time.sleep(60)
#     for p in psutil.process_iter(attrs=['pid', 'name']):
#         if p.info['name'] == "ansysedt.exe":
#             st = "yes"
#             break
#             #print("yes", (p.info['name']))
#     return st


def checkwindow():
    st = "no"
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
     
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
     
    # for p in titles:
    #     print(p)
    
    substring_in_list = any('ANSYS Electronics Desktop' in string for string in titles)
    if substring_in_list == True:
        st = "yes"
        
    return st

print("Monitoring ANSYS HFSS!!!")
while(1):
    st = checkwindow()
    if st == "no":
        break
    time.sleep(300)#5min = 300
IronDrive.status("HFSS was closed!!!")
print("HFSS was closed!!!")





 
