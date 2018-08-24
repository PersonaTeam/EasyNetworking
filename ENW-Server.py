# Advanced Wireless Network Creator ( LAN Wireless Network ) 
# Code By Mohammad Abbasi
# Available on Windows Platforms ( xp - 7 - 10 )"""
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
This Application Is For The Server Computer 


Usage : ENW-Server.py [-h] [-n] [-p] [-u] [-s]

Options :                    
     -h         Help For How To Be Joined To Network
     -n         Network Name
     -p         Network Password
     -u         User Accounts Name
     -s         Stop Network \n  
                    
     ForExample: ENW-Server.py  -n mohammad -p 1234 -u User \n 
                    
                             ^_^ 

     # Advanced Wireless Network Creator ( LAN Wireless Network ) 
     # Code By Mohammad Abbasi
     # Available on Windows Platforms ( xp - 7 - 10 )""")


    Choice_Color()
    os.system("cls")
    if sys.argv[1] == "-h" :
        Choice_Color()
        print (" Playing Tutoial Video  :) ")
        os.system("Help.wmv")
        sys.exit()
    elif sys.argv[1] == '-s' :
        os.system(" netsh wlan stop hostednetwork")
        time.sleep (2)
        print (" [+] Please Wait To Turn Off The Firewall \n ")
        firewall = os.system("""netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=no""")
        time.sleep (2)
        print (" [+] Please Wait To Turn Off The Network Discovery \n ")
        os.system ("""netsh advfirewall firewall set rule group="Network Discovery" new enable=no""")
        os.system ("cls")
        print(" [+] Network Is Off GodBye ^_^  \n ")
        time.sleep (2)
        print ("\n [*] Thank You For Using EasyNetworking ")
        time.sleep (2)
        print ("\n [*] Follow Me In GitHub & Telegram  .")
        time.sleep (2)
        print ("""\n
             [*] https://t.me/Avestar
             [*] https://t.me/PersonaDigitalSecurityTM
             [*] https://github.com/PersonaTeam """)
       
        sys.exit()

    try :
        if sys.argv[1] != "-n" :
            print (" Wrong Comment ! ")
            time.sleep (2)
            os.system ("cls")
            Help()
            sys.exit()
        else :
            sys.argv [2]
        if sys.argv[3] != "-p" :
            print (" Wrong Comment ! ")
            time.sleep (2)
            os.system ("cls")
            Help()
            sys.exit()

        else :
            sys.argv [4]
            passw = sys.argv[4]
        if sys.argv [5] != "-u" :
            Help()
            sys.exit()
        else :
            sys.argv [6]
    except IndexError :
        print ()
    if len (passw)>= 8:
        os.system(" netsh wlan set hostednetwork mode=allow ssid={} key={}".format(sys.argv[2],sys.argv[4]))
        os.system(" netsh wlan start hostednetwork ")
        print (" Please Add Password For Account (Password can not be seen, but set) \n ")
        os.system(" net user {} *".format(sys.argv[6]))
        time.sleep (2)
        print (" [+] Please Wait To Turn On The Firewall ")
        firewall = os.system("""netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=yes""")
        time.sleep (2)
        print (" [+] Please Wait To Turn On The Network Discovery ")
        os.system ("""netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes""")
        os.system ("cls")
        time.sleep (2)
        print(" [+] Wireless Network Was Activated With Name {} (Share File And Enjoy To Use)".format(sys.argv[2]))
        time.sleep (2)
        print ("\n [*] Thank You For Using EasyNetworking ")
        time.sleep (2)
        print ("\n [*] Follow Me In GitHub & Telegram .")
        time.sleep (2)
        print ("""\n
             [*] https://t.me/Avestar
             [*] https://t.me/PersonaDigitalSecurityTM
             [*] https://github.com/PersonaTeam """)
        
    else :
        print(" ----> Error , Password should be 8 to 63 characters")

except IndexError :
    Help()



