from Modules.encrypt import *
from Modules.Descover_type_hash import *
from ban_hash import  *
from Modules.Files_encryptinos import *
from Modules.DEcrypt import *
import math
from colorama import Fore
import os

def ICE():
    os.system('clear')
    ice_banner()
    chose = int(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter number you want : '))


    if chose == 1 :
        os.system('clear')
        encrypt_banner()
        what = int(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter number you want : '))
        if what == 99 :
            ICE()
        elif what == 14 :
            
            Txt = list(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter you want encrypted : '))
            KEy = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter Key : ')) 

            EncrypT().Caesar(Txt, KEy)
        
        elif what == 15 :

            Text = str(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter your text :')).lower()
            EncrypT().Monoalphabetic(Text)

        elif what == 16 :

            txt = str(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter text : '))
            key = str(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter key : '))
            print('\n')
            if len(txt) <= len(key):
                
                # take letter numbers from a - z
                CK = key[:len(txt)]


            else :
                
                # numbers of text / key 
                CL = math.ceil(len(txt) / len(key))

                NK = []
                
                # The number of repetitions
                for Crypt in range(0, CL):

                    for Next in key :

                        NK.append(Next)

                CK = NK[:len(txt)]

            EncrypT().vigenere(txt, CK)

        else:

            EncrypT().encrypt(what)

    elif chose == 2:
        
        os.system('clear')
        encrypt_attack_banner()
        you_want = int(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter number hash you want :' ))
        
        if you_want == 99:
            ICE()

        elif you_want == 11 :

            xt = list(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter Hash : '))
            KEy = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter how many key you want try : '))

            Decrypts(xt).decrypt_Caesar(KEy)

        elif you_want == 12 :

            Text = str(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter your hash :')).lower()
            Decrypts(Text).decrypt_Monoalphabetic()
        

        elif you_want == 13 :

            txt = str(input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter text : '))
            key = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter file keys : ')
            print('\n')

            Key_read = open(key, 'r').readlines()

            for file in Key_read :
                file = str(file).strip()



                if len(txt) <= len(file):
                    
                    # take letter numbers from a - z
                    CK = file[:len(txt)]


                else :
                    
                    # numbers of text / key 
                    CL = math.ceil(len(txt) / len(file))

                    NK = []
                    
                    # The number of repetitions
                    for Crypt in range(0, CL):

                        for Next in file :

                            NK.append(Next)

                    CK = NK[:len(txt)]

                Decrypts('').decrypt_vigenere(txt, CK)
        
        else:
            file_name = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter wordlist for crack : ')
            the_hash = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter hash : ')

            E_A = Decrypts(the_hash)
            E_A.encrypt_attack(you_want, file_name)

    elif chose == 3 :
        
        os.system('clear')
        know_hash_banner()
        
        know_hash()

    elif chose == 4 :
        
        os.system('clear')
        py_encrypt_banner()
        name_file = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name python file : ')
        
        E_py = Files_Encryptions(name_file)
        E_py.py_encrypt()

    elif chose == 5 :
        
        os.system('clear')
        pdf_encrypt_banner()
        file_name = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name file PDF to encrypt : ')
        password_file = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter password for file : ')
        
        E_PDF = Files_Encryptions(file_name)
        E_PDF.pdf_encrypt(password_file)

    elif chose == 6 :
        os.system('clear')
        Decrypt_without_list_banner()
        
        the_hash = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter hash : ')

        D_W_L = Decrypts(the_hash)
        D_W_L.Decrypt_without_list()

    elif chose == 7 :
        os.system('bash encryption/Exe.sh')

    elif chose == 99:
        print(f'\nGood bye ...')
        exit()

    else:
        print(Fore.RED+'Error : The number you chose is not available')
        exit()

ICE()
