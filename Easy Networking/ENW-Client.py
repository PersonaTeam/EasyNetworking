# Advanced Wireless Network Creator ( LAN Wireless Network ) 
# Coded By Mohammad Abbasi
# Available on Windows Platforms ( xp - 7 - 10 )
# The program written with Python 3.6

import random
import sys
import os
import time
def Choice_Color () :
    rand =  "Color a ","Color b","Color c","Color d","Color f "
    rand_Choice_Color = random.choice (rand)
    os.system(rand_Choice_Color)


try :
    def Help () :
        print ("""
This Application Is For The Client Computers 


Usage : ENW-Client.py [-h] [--start] [--stop] 

Options :                    
     -h         About Start Or Stop 
     --start    Enable Network Settings
     --stop     Disabel Network Settings 
                    
     Example (Start): ENW-Client.py --Start \n
     Example (Stop) : ENW-Client.py --Stop 
                    
                             ^_^ 

     # Advanced Wireless Network Creator ( LAN Wireless Network ) 
     # Coded By Mohammad Abbasi
     # Available on Windows Platforms ( xp - 7 - 10 )""")


    Choice_Color()
    os.system("cls")
    if sys.argv[1] == "-h" :
            Help ()


    elif sys.argv[1] == "--start" :            
        print (" [+] Please Wait To Turn On The Firewall \n ")
        firewall = os.system("""netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=yes""")
        time.sleep (2)
        print (" [+] Please Wait To Turn On The Network Discovery \n ")
        os.system ("""netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes""")
        os.system ("cls")
        time.sleep (2)
        print ("\n [*] Thank You For Using EasyNetworking ")
        time.sleep (2)
        print ("\n [*] Follow Us In GitHub & Telegram  .")
        time.sleep (2)
        print (""" \n
             [*] https://t.me/Avestar
             [*] https://t.me/PersonaDigitalSecurityTM
             [*] https://github.com/PersonaTeam """)
        
               
    elif sys.argv[1] == "--stop" :
               time.sleep (2)
               print (" [+] Please Wait To Turn Off The Firewall \n ")
               firewall = os.system("""netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=no""")
               time.sleep (2)
               print (" [+] Please Wait To Turn Off The Network Discovery \n ")
               os.system ("""netsh advfirewall firewall set rule group="Network Discovery" new enable=no""")
               os.system ("cls")
               time.sleep (2)
               print ("\n [*] Thank You For Using EasyNetworking ")
               time.sleep (2)
               print ("\n [*] Follow Us In GitHub & Telegram.")
               time.sleep (2)
               print (""" \n
             [*] https://t.me/Avestar
             [*] https://t.me/PersonaDigitalSecurityTM
             [*] https://github.com/PersonaTeam """)
        
    elif sys.argv[1] != "--stop" or sys.argv[1] != "--start" or sys.argv[1] != "-h" :
        print (" Wrong Syntax ! ")
        time.sleep (2)
        os.system ("cls")
        Help ()          
               
except IndexError :
               Help ()
