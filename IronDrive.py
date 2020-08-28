# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:54:53 2020

@author: Heriberto
"""

import os
import json

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
        
    #call the python script to send a message
    os.system('C:/ProgramData/Anaconda3/Scripts/activate.bat C:/ProgramData/Anaconda3 && python C:/Send2Gchat/Send2Gchat.py')
