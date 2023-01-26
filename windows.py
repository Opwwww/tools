from os import system as s
import requests as r
from colorama import Fore
from sys import platform
import requests
import time as t
import sys as opw
if platform == "linux" or platform == "linux2":
  s("clear")
elif platform == "win32":
  s("cls")
elif platform == "darwin":
  s("clear")
print(Fore.CYAN + "Type Help to see all the commands.")
while True:
 currentTime = t.ctime()
 yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "help":
    print(Fore.LIGHTBLUE_EX + """
            
      
            '##:::::'##:'####:'##::: ##:'########:::'#######::'##:::::'##::'######::
             ##:'##: ##:. ##:: ###:: ##: ##.... ##:'##.... ##: ##:'##: ##:'##... ##:
             ##: ##: ##:: ##:: ####: ##: ##:::: ##: ##:::: ##: ##: ##: ##: ##:::..::
             ##: ##: ##:: ##:: ## ## ##: ##:::: ##: ##:::: ##: ##: ##: ##:. ######::
             ##: ##: ##:: ##:: ##. ####: ##:::: ##: ##:::: ##: ##: ##: ##::..... ##:
             ##: ##: ##:: ##:: ##:. ###: ##:::: ##: ##:::: ##: ##: ##: ##:'##::: ##:
            . ###. ###::'####: ##::. ##: ########::. #######::. ###. ###::. ######::
             :...::...:::....::..::::..::........::::.......::::...::...::::......:::

         
         [1] -- Display network information.        [2] -- System Information.

         [3] -- Display private history.            [4] -- Tree

         [5] -- Check if a website is running.      [6] -- Stop windows defender.
 
         [7] -- Windows defender Status.            [8] -- Discord Webhook Checker.

         [9] -- Display Drivers of the Pc.          [10] -- Ping a Host.

         [11] -- Make  a Folder.                    [12] --Delete a folder.

         [13] -- Go back.                           [14] -- Restart.
                                                                                                 
         [15] -- Exit                    
        
""")
  if yes == "credits":
   Made By Opw
    
   Discord = "opw#7777"

   Github = "github.com/Opwwww  
 currentTime = t.ctime()
 yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "1" or yes == "01":
    s("ipconfig")
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "2" or yes == "02":
  s("systeminfo")
  currentTime = t.ctime()
  yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "3" or yes == "03":
    s("ipconfig /displaydns")
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "4" or yes == "04":
    s("tree")
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "5" or yes == "05":
    currentTime = t.ctime()
    request = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Website: ")
    r.get(request)
    if r.status_codes == "404":
        print(Fore.RED+"[-] Website is down.")
    else:
         print(Fore.GREEN+"[+] Website is working.")
 if yes == "6" or yes == "06":
    print("You need admin for this^")
    s("sc stop windefend")
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "7" or yes == "07":
    s("sc query windefend")
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "8" or yes == "08":
    webhook = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Webhook: ")
    yeah = r.get(webhook)
    if yeah.status_code == 404:
        print("Invalid Webhook.")
    else:
     print("Valid Webhook.")
 if yes == "9" or yes == "09":
    currentTime = t.ctime()
    s("sc query type=driver")
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "10":
    currentTime = t.ctime()
    host = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Host: ")
    s("ping"+host)
 if yes == "11":
    currentTime = t.ctime()
    print("Input the path, example: c:/users/{name}/downloads/folderexample")
    folder = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Name of the folder: ")
    s('mkdir ' + folder)    
    currentTime = t.ctime()
    yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
 if yes == "12":
    currentTime = t.ctime()
    fold = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Name of the folder: ")
    s("del " + fold)
    currentTime = t.ctime()
    fold = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Name of the folder: ")
 if yes == "13":
    s('cmd /k "python main.py" ')
 if yes == "14":
    s('cmd /k "python windows.py" ')
 if yes == "15":
    opw.exit("Exitting...")
 else:
    while True:
     print(Fore.RED+ "[-] Invalid option.")
     t.sleep(2)
     s("cls")
     yes = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")


    



