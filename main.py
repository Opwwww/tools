from os import system as s
from time import sleep as sl
from colorama import Fore
from sys import platform
import time as t
if platform == "linux" or platform == "linux2":
  s("clear")
elif platform == "win32":
  s("cls")
elif platform == "darwin":
  s("clear")
print(Fore.RED+"""                        
                          ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ############################## 
              #                             #    ########   #""")
print(Fore.GREEN+"                  ####   ##  ")    
print(Fore.RED+"""                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##        
                      ##     ##   ##     ##        """)
sl(1)
print(Fore.CYAN + "Type help to see the information." )
currentTime = t.ctime()
help = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if help == "help":
  print(Fore.RED +"""

  [1] --  [Credits]                        [2] -- [Restart]
  
  [3] --  [Windows tools]                  [4] -- [Linux tools.] 

  [5] --  [Discord Webhook Spammer.]       [6] -- [Credit Card Generator.]
 
  """)
  currentTime = t.ctime()
  help = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
if help == "1"or help == "01":
  print(Fore.BLUE + """
  Well#9999
  https://github.com/londxv/
  """)
if help == "2" or help == "02":
  print(Fore.GREEN + "[+]")
  s('cmd /k "python main.py"')
if help == "3" or help == "03":
  print(Fore.GREEN + "[+]")
  s('cmd /k "python windows.py"')
if help == "04" or help == "4":
  print(Fore.GREEN + "[+]")
  s('cmd /k "python main.py" ')
if help == "5" or help == "05":
  print(Fore.GREEN + "[+]")
  s('cmd /k "python spammer.py" ')
if help == "6" or help == "06":
     print(Fore.GREEN + "[+]")
     s('cmd /k "python generator.py" ')
else:
    print(Fore.RED+ "[-] Invalid option.")
    t.sleep(1)
    s("cls")
    currentTime = t.ctime()
    gen = input(Fore.CYAN + "[" + currentTime.split(" ")[3]  + "]" + " >>> ")
