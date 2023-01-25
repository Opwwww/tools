import os as o
import time as t
import sys as opw
from time import sleep as s
from sys import platform
from colorama import Fore
import requests as r
if platform == "win32":
 o("cls")
if platform == "linux" or platform == "linux2":
 o("clear")
if platform == "darwin":
 o("clear")
print(Fore.BLUE + "Type help or credits.")
currentTime = t.ctime()
cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "help":
    print(Fore.LIGHTRED_EX + """
                                 
                                                         Run this on Linux.       * = Root needded(admin)
                                                                      
                                                                    .##.......####.##....##.##.....##.##.....##
                                                                    .##........##..###...##.##.....##..##...##.
                                                                    .##........##..####..##.##.....##...##.##..
                                                                    .##........##..##.##.##.##.....##....###...
                  .                                                 .##........##..##..####.##.....##...##.##..
                                                                    .##........##..##...###.##.....##..##...##.
                                                                    .########.####.##....##..#######..##.....##
   
                    

                                                                    [1] -- Clear Terminal.        [2] -- Display your IP Adress.        
                
                                                                    [3] -- Open text editor.      [4] -- Update system.*

                                                                    [5] -- See hidden files.      [6] -- Run Metasploit Database and Metasploit.*
                                                                                 
                                                                    [7] -- Display history.       [8] -- Run python http.server (port 8000).
                                                                                
                                                                    [9] -- Display path.          [10] -- Scan a Website.

                                                                    [11] -- Restart pc.           [12] -- Shutdown PC. 
                                                                                                  
                                                                    [13] -- Make a Banner.*       [14] -- Nmap a host.

                                                                    [15] -- Ping a host.          [16] -- Go back.

                                                                    [17] -- Exit.   """)
currentTime = t.ctime()
cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "credits":
    print(Fore.BLUE + """
    Well#9999
    https://github.com/londxv/
    """)
if cmd == "1" or cmd == "01":
  o("clear")
  currentTime = t.ctime()
  cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ") 
if cmd == "2" or cmd == "02":
  o("ifconfig")
  currentTime = t.ctime()
  cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ") 
if cmd == "3" or cmd == "03":
    currentTime = t.ctime()
    text = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Name n extension (test.py): ")
    o("nano " + text)
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "4" or cmd == "04":
    o("sudo apt-get update")
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ") 
if cmd == "5" or cmd == "05":
    o("find .")    
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "6" or cmd == "06":
    o("msfdb run")
if cmd == "7" or cmd == "07":
    o("history")
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "8" or cmd == "08":
  o("python -m http.server ") 
if cmd == "9" or cmd == "09":
    o("echo $PATH")
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "10":
  web = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Web: ")
  yeah = r.get(web)
  if yeah.status_code == 404:
    print("Invalid Website. (add http:// )")
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
  else:
    o("whatweb -v -a 3 " + web)
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "11":
    o("reboot")
if cmd == "12":
    o("shutdown -n")
if cmd == "13":
 print("Installing modules.. [+]")
 t.s(1)
 o("suto apt-get install figlet ")
 print("Input something.")
 banner = input("Banner: ")
 o("figlet "+ banner)
 currentTime = t.ctime()
 cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "14":
    host = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> Host: ")
    print(Fore.GREEN + "[+] Scanning...")
    o("nmap -Pn -sV " +host)
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "15":
    ye = input("Host: ")
    o("ping "+ ye)
    currentTime = t.ctime()
    cmd = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if cmd == "16":
    o('cmd /k "python main.py" ')
if cmd == "17":
    opw.exit("Exitting.. ")





 
