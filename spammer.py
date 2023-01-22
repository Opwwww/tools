#Webhook spammer yes
#made by opw 
import requests as r
import time as t
from colorama import Fore
from os import system as sys
from time import sleep as s
currentTime = t.ctime()
sys("cls")
print(Fore.GREEN+"""

 :::::::: :::::::::    :::    ::::    :::: ::::    :::: :::::::::::::::::::  
:+:    :+::+:    :+: :+: :+:  +:+:+: :+:+:++:+:+: :+:+:+:+:       :+:    :+: 
+:+       +:+    +:++:+   +:+ +:+ +:+:+ +:++:+ +:+:+ +:++:+       +:+    +:+ 
+#++:++#+++#++:++#++#++:++#++:+#+  +:+  +#++#+  +:+  +#++#++:++#  +#++:++#:  
       +#++#+      +#+     +#++#+       +#++#+       +#++#+       +#+    +#+ 
#+#    #+##+#      #+#     #+##+#       #+##+#       #+##+#       #+#    #+# 
 ######## ###      ###     ######       ######       ################    ### 
""")
print(Fore.GREEN + "Loading webhook spammer [*]")
s(1)
#Webhook
print(Fore.RED + "Input webhook")
currentTime = t.ctime()
webhook = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
webhook_check = r.get(webhook)
if webhook_check.status_code == 404:
    print(Fore.RED + "Invalid webhook,try again")
    currentTime = t.ctime()
    input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
else:
    print(Fore.GREEN + "Working webhook")
#username of the webhook
currentTime = t.ctime()
print(Fore.RED + "Input username of the webhook.")
user = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
#Avatar of the webhook (url)
currentTime = t.ctime()
print(Fore.RED + "Input the webhook avatar (url)")
avatar = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
#Message to send
currentTime = t.ctime()
print(Fore.CYAN + "Message: ")
message = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
currentTime = t.ctime()
print(Fore.CYAN + "Do you want to see webhook url,username,avatar? (y/n)")
answer = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if answer == "yes" or answer == "y" or answer == "ye":
    print("Webhook: "+ webhook)
    print("Username: " + user)
    print("Avatar URL: " + avatar)
    print("Message: " + message)
    s(1)
    print(Fore.GREEN + "[*} Spamming webhook..")
if answer == "n" or answer == "no":
    print(Fore.GREEN + "[*} Spamming webhook..")
#Headers (Ignore this)
headers = {"Content-Type": "application/json"}
data = {
  "content": message,
  "username": user,
  "avatar_url": avatar
}
#Spam
while True:
 spammer = r.post(webhook,headers=headers,json=data)
