"""
Created on Thu Aug 27 15:36:56 2020

@author: Heriberto
"""
import os
import sys
import json

from json import dumps
from json import loads

from datetime import datetime

from httplib2 import Http

def Send2Gchat(message):
    """ # Function to send the message
    # message  is a String""" 
    
    #This part will load the message from IronDrive
    filemessage = os.path.join('c:/Send2Gchat', 'message.json')
    if os.path.exists('c:/Send2Gchat/message.json'):
        with open(filemessage) as json_message:
            datamessage= json.load(json_message)
            for pm in datamessage['message']:
                print('text: ' + pm['text'])
                print('number: ' + pm['value'])
                print('')
            message = pm['text']
        os.remove('c:/Send2Gchat/message.json') 
    
    #JSON CONFIG    
    filepath = os.path.join('c:/Send2Gchat', 'config.json')
    if not os.path.exists('c:/Send2Gchat'):
        os.makedirs('c:/Send2Gchat')

    #This will open json config to upload the url and thread if that exists
    with open(filepath) as json_file:
        data = json.load(json_file)
        for p in data['config']:
            print('url: ' + p['url'])
            print('thread: ' + p['thread'])
            print('')
         
    #Just a time reference
    now = datetime.now() # current date and TimeoutError
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    #Filling the URL, message and thread to POST
    url = p['url']
    bot_message = {
        'text' : current_time + " | "+ message
        }
    bot_message['thread'] = { "name": p['thread'] }
        
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    #Creating the HTTP object
    http_obj = Http()

    #Sending and saving the contents
    response, content = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    # print(response)
    # print(content)
    
    #If the JSON file doens't have any thread, it will fill a new one.
    if p['thread'] == "" : 
        print ("Thread empty!!!")
    
        content_json = loads(content)
        thread_json = content_json['thread']
        
        data = {}
        data['config'] = []
        data['config'].append({
            'url': p['url'],
            'thread': thread_json['name'],        
            'anaconda3': p['anaconda3'],
            'activated.bat': p['activated.bat']
        })
    
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile)
    
        print('Updating new thread: '+thread_json['name'])
        print('')

    return 0

#Function to set the Webhook url | USE THIS FUNCTION ON PYTHON TERMINAL TO GENERATE A NEW CONFIG.JSON
def config():   
    """ # Function to create the connection with Webhook of Google Chat
    # url  is a String"""  
    
    while True:
        urlc = input("WebHook URL from Google Chat: ")
        check = input("This URL is correct (y/n)?\n"+urlc+"\n")
        if check == 'y':
            break
    
    while True:
        anaconda = input("Path of Anaconda3\n(Example: C:/ProgramData/Anaconda3)\n>")
        if os.path.exists(anaconda):
            break
        else:
            print("Path not founded!!!\n")
    
    while True:
        activate = input("PATH of activated.bat from Anaconda3\n(Example: C:/ProgramData/Anaconda3/Scripts/activate.bat):\n>")
        if os.path.exists(activate):
            break
        else:
            print("Path not founded!!!\n")
    
    data = {}
    data['config'] = []
    data['config'].append({
        'url': urlc,
        'thread': "",
        'anaconda3': anaconda,
        'activated.bat': activate,
    })

    filepath = os.path.join('c:/Send2Gchat', 'config.json')
    if not os.path.exists('c:/Send2Gchat'):
        os.makedirs('c:/Send2Gchat')
    
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)

    print('Setting URL: '+urlc)
    print('Anaconda3 PATH: '+anaconda)
    print('activated.bat PATH: '+activate)
    print('')
    
    return 0


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = int(sys.argv[1])
        if arg == 1:
            Send2Gchat("SIMULATION STARTED")
        else:
            Send2Gchat("DONE")
    else:
        Send2Gchat("HELLO WORLD")
    
    
    