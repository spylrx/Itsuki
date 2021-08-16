# Itsuki es una tool hecha en python | github.com/spylrx
import random
from random import *
from random import randrange, choice
from string import ascii_letters, digits
from threading import Thread as thr
from itertools import cycle
from datetime import date
from colorama import Fore
from time import sleep
import os
import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)
import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)

os.system("title Spylrx...")

print(f"""
{Fore.RED}
destroy
                                       {Fore.WHITE}         Espera porfavor...
""")
print(f"{Fore.RED}")

import base64, pyperclip

os.system("title Itsuki token tool | github.com/spylrx")
os.system("cls")
print(f"""{Fore.RED}


                   ██╗████████╗███████╗██╗   ██╗██╗  ██╗██╗
                   ██║╚══██╔══╝██╔════╝██║   ██║██║ ██╔╝██║
                   ██║   ██║   ███████╗██║   ██║█████╔╝ ██║
                   ██║   ██║   ╚════██║██║   ██║██╔═██╗ ██║
                   ██║   ██║   ███████║╚██████╔╝██║  ██╗██║
                   ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
               {Fore.YELLOW}  <+> https://github.com/spylrx
""")
id = input(Fore.RED+"[$] I˜Sk" + Fore.WHITE+"@" + Fore.RED+"Spylrx" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.RED+"ID :" + Fore.WHITE+" ")

try:
    check = int(id)
    print('')
    print(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] ID valida.')
    data = f'{id}'
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print('')
    print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] {encodedStr}')
    print('')
    copy = input(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] Quieres copiar el token en el portapapeles? (y/n){Fore.WHITE} ')

    if copy == "y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] Text Copiado !')

    if copy == "Y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] Text Copiado !')

    else:
        print('')
        print(f'{Fore.RED} [{Fore.YELLOW}+{Fore.BLUE}] Presiona enter para salir')
        input()

except ValueError:
    print('')
    print(f'{Fore.WHITE} [{Fore.RED}+{Fore.WHITE}] Id invalida')
    print('')
    print(f'{Fore.WHITE} [{Fore.RED}+{Fore.WHITE}] Presiona enter para salir')
    input()
             