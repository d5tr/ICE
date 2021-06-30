from encrption.encrypt import *
from encrption.Decrypt import *
from encrption.Descover_type_hash import *
from ban_hash import  *
from encrption.py_encrypt import *
from encrption.pdf_encrypt import *
from colorama import Fore
import os

def ICE():
    os.system('clear')
    ice_banner()
    chose = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number you want :'))


    if chose == 1:
        os.system('clear')
        encrypt_banner()
        what = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number you want :'))
        if what == 99 :
            ICE()
        encrypt(what)

    elif chose == 2:
        os.system('clear')
        encrypt_attack_banner()
        you_want = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number hash you want :'))
        if you_want == 99:
            ICE()
        file_name = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter wordlist for crack :')
        the_hash = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter hash :')

        encrypt_attack(you_want, file_name, the_hash)

    elif chose == 3 :
        os.system('clear')
        know_hash_banner()
        know_hash()

    elif chose == 4 :
        os.system('clear')
        py_encrypt_banner()
        name_file = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name python file :')
        py_encrypt(name_file)
    elif chose == 5 :
        os.system('clear')
        pdf_encrypt_banner()
        file_name = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name file to encrypt :')
        password_file = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter password for file : ')
        pdf_encrypt(file_name, password_file)

    elif chose == 99:
        print(f'\nGood bye ...')
        exit()

    else:
        print(Fore.RED+'Error : The number you chose is not available')
        exit()

ICE()
