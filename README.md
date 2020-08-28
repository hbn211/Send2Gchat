# Send2Gchat

This script will send the alert to your Google Chat group.

1- Install:
pip install httplib2

2 - To create the config.json, you have to execute at the first time the SeturlGchat with the webhook url from Google Chat.

Tip:

>>> (base) C:\Send2Gchat>python
>>> Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
>>> Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> >>> from Send2Gchat import SeturlGchat
>>> >>> SeturlGchat('URL LINK')
>>> >>> Setting URL: URL LINK
>>>
>>> 0
>>> >>> quit()
>>>
>>> (base) C:\Send2Gchat>

You will observe that the config.json have created with this informations:

{"config": [{"url": "URL LINK", "thread": ""}]}

The thread information will autofill with the first message sent. But if you call again SeturlGchat, this information will be erased.

Tested on Anaconda3s
Python 3.7.7