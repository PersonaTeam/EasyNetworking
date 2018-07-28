# This Program Use For Create ( LAN Wireless Network ) 
# This Program Write By Mohammad Abbasi
# This Program Tested On ( Win xp - Win 7 - Win 10 )""")
import sys,os,random

def Choice_Color () :
    rand =  "Color a ","Color b","Color c","Color d","Color f "
    rand_Choice_Color = random.choice (rand)
    os.system(rand_Choice_Color)
try :
    def Help () :
        print ("""
                    Usage : EasyNetworking.exe  [-n] [-p] [-u] [-s]
                    -h                Help For How To Be Joined To Network
                    -n                Network Name
                    -p                Network Password
                    -u                User Accounts Name
                    -s                Stop Network \n  
                    
                    ForExampel: EasyNetworking.exe  -n mohamamd -p 1234 -u User \n 
                    
                                            ^_^ 
                    # This Program Use For Create ( LAN Wireless Network ) 
                    # This Program Write By Mohammad Abbasi
                    # This Program Tested On ( Win xp - Win 7 - Win 10 )""")


    Choice_Color()
    os.system("cls")
    if sys.argv[1] == "-h" :
        Choice_Color()
        print (" Play Help Film :) ")
        Dir = os.getcwd()
        os.system(r"Untitled_0001.wmv")
        sys.exit()
    elif sys.argv[1] == '-s' :
        os.system(" netsh wlan stop hostednetwork")
        print(" [+] Done Network Off GodBye ^_^  \n ")
        sys.exit()

    try :
        if sys.argv[1] != "-n" :
            Help()
            sys.exit()
        else :
            sys.argv [2]
        if sys.argv[3] != "-p" :
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
        print ("Plz Add Password For Account (Password can not be seen, but set) \n ")
        os.system(" net user {} *".format(sys.argv[6]))
        os.system(" netsh advfirewall firewall set rule group={} new profile=private".format("File and Printer Sharing "))
        print(" [+] Wireless Network Was Activated With Name {} (Share File And Enjoy To Use)".format(sys.argv[2]))
    else :
        print(" ----> Error , Password should be 8 to 63 characters")

except IndexError :
    Help()



