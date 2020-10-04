# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:54:53 2020

@author: Heriberto
"""

import os
import json
import threading

def status(message):
    
    #This place where the message will be storaged
    filepath = os.path.join('c:/Send2Gchat', 'message.json')
    if not os.path.exists('c:/Send2Gchat'):
        os.makedirs('c:/Send2Gchat')
        
    data = {}
    data['message'] = []

    data['message'].append({
        'text': message,
        'value': '0',
            })
    
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)
    

    filepath = os.path.join('c:/Send2Gchat', 'config.json')
    if not os.path.exists('c:/Send2Gchat'):
        os.makedirs('c:/Send2Gchat')

    #This will open json config to upload the url and thread if that exists
    with open(filepath) as json_file:
        data = json.load(json_file)
        for p in data['config']:
            print('')
            
    #call the python script to send a message
    command = p['activated.bat'] + ' ' + p['anaconda3'] + ' && python C:/Send2Gchat/Send2Gchat.py'
    os.system(command)


def callcheck():   
    filepath = os.path.join('c:/Send2Gchat', 'config.json')
    if not os.path.exists('c:/Send2Gchat'):
        os.makedirs('c:/Send2Gchat')
    
    #This will open json config to upload the url and thread if that exists
    with open(filepath) as json_file:
        data = json.load(json_file)
        for p in data['config']:
            print('')
    
    command = p['activated.bat'] + ' ' + p['anaconda3'] + ' && python C:/Send2Gchat/checkprocess.py'
    os.system(command)
    
def enableHFSSmonitor():
    t = threading.Timer(1,callcheck)
    t.start()