import subprocess as sp
import colorama
from colorama import Fore, Back, Style
import time
import netifaces
colorama.init(autoreset = True)

def macchanger():
    
    sp.call("clear", shell=True)
    sp.call("figlet mac changer", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    sp.call("figlet Coded By", shell=True)
    sp.call("figlet DarknetWolf", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    print(" \n")
    print("Do you want to change your MAC to a random address or you would like to specify your own MAC? (Self/Random)")
    print(" \n")
    print(Fore.GREEN + Back.BLACK + "Reply with 'Random' or 'Self' to lock your decision: \n")



    user=input()
    if (user == 'random') or (user == 'Random'):
        print(" \n")
        print(Fore.WHITE + Back.RED + "Your Available Interfaces: ")
        print(" \n")
        print(netifaces.interfaces())
        print(" \n")
        iface=input("Please enter your Interface name according to your available interfaces: ")
        print(" \n")
        
        print(Fore.RED + Back.WHITE + "[+] Changing your MAC to a Random Address:")
        sp.call("macchanger -r" + " " + iface, shell=True)
        print(" \n")
        print(Fore.GREEN + "[+] Showing your Current MAC address status:")
        sp.call("macchanger --show" + " " + iface, shell=True)
        print(" \n")
    elif (user == 'Self') or (user == 'self'):
        print(" \n")
        print(Back.CYAN + Style.NORMAL + Fore.RED + "please enter the new mac: \n")
        new_mac = input()
        print(" \n")
        print(Back.RED + Fore.WHITE + "Your Available Interfaces are: ")
        print(" \n")
        print(netifaces.interfaces())
        print(" \n")
        interface=input("Please enter your Interface name according to your available interfaces: \n")
        print(" \n")
        print(Fore.GREEN + "[+] Your current MAC address status:")
        time.sleep(1)
        sp.call("macchanger --show wlan0", shell=True)
        print(" \n")
        print(Fore.GREEN + "[+] Taking your NetworkManager Down:")
        time.sleep(2)

        print(" \n")
        sp.call("ifconfig wlan0 down", shell=True)
        print(Fore.GREEN + "[+] Changing your MAC address:")
        sp.call("macchanger -m " + new_mac + " " + interface, shell=True)
        print("\n")
        print(Fore.WHITE + Back.RED + "Please Note: MAC addresses are changed based on the Availability of the MAC in the Library. \n")
        print(Fore.WHITE + Back.RED + "Sometimes, you may not see the MAC which is is given by you while choosing the 'SELF' option. \n")



        sp.call("ifconfig wlan0 up", shell=True)

        print(Fore.GREEN + "[+] Showing your Current MAC address:")
        sp.call("macchanger --show" + " " + interface, shell=True)
        print(" \n")
    else:
        print(Fore.RED + Back.YELLOW + Style.NORMAL + "INVALID INPUT YOU FUCKING IDIOT.")
        time.sleep(2)
        sp.call("clear", shell=True)
        sp.call("figlet IDIOTS EVERYWHERE", shell=True)

macchanger()

flag = 0
while (flag == 0):
    print("Do you want to change your MAC address again?")
    secondtime=input()
    if (secondtime=='Yes') or (secondtime=='yes') or (secondtime=='YES') or (secondtime=='y'):
        macchanger()
    elif (secondtime=='No') or (secondtime=='no') or (secondtime=='NO') or (secondtime=='n'):
        sp.call("figlet THANKS FOR USING", shell=True)
        time.sleep(1)
        sp.call("clear", shell=True)
        sp.call("figlet BYE", shell=True)
        break
    else:
        print("Again, Invalid input.")
