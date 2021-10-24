import random
from hashlib import *
from colorama import Fore

class EncrypT :

    
    def vigenere(self, txt, key):


        CL = []

        for (letter, kex) in zip (txt, key):
            
            # to see rank of letter
            TP = ord(letter)
            # to see rank of number 
            KP = ord(kex)

            NL = chr(TP + KP)

            CL.append(NL)

        end = ''.join(CL)

        print(f'\n Encrypted {Fore.CYAN}==>{Fore.WHITE} ',end)


    def Caesar(self, txt, key):

            
        # save encrypt
        Clist = []

        for crypt in txt:
            # letter order from 1 to 26
            Order = ord(crypt)
            # Encrypt
            encrypt = chr(Order+key)
            # add to list
            Clist.append(encrypt)
        # converting to str
        converting = ''.join(Clist)

        print(f'\n Encrypted {Fore.CYAN}==>{Fore.WHITE} ',converting)

    def Monoalphabetic(self, txt):

        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'h', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z'
        ]
        
        Keys = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
            's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 
            'v', 'b', 'n', 'm'
        ]

        #Text = str(input('[+] Enter text : ')).lower()

        CI = []

        for encrypT in txt:
            # set nummber for letters in Text
            KN = letters.index(encrypT)
            # switch KN => Keys
            NL = Keys[KN]
            # return NL in CI
            CI.append(NL)

        # converting to str
        ET = ''.join(CI)
        print(f'\n Encrypted {Fore.CYAN}==>{Fore.WHITE} ', ET)


    def encrypt(self, ch0s):

        if ch0s == 2:
            lowen = 'qwertyuiopasdfghjklzxcvbnm'
            uppen = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            numbers = '1234567890'
            symbols = '[]{+*/-_@$'

            all = lowen + uppen + numbers + symbols
            length = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter number length hash : '))
            passwond = "".join(random.sample(all, length))
            print('------------------------')
            print(passwond)
            print('------------------------')



        ###################################################
        elif ch0s == 1:

            x = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            # encrypt
            y = md5(x.encode()).hexdigest()
            print("-----------------------")
            print(y)
            print("-----------------------")



        ##############################################
        elif ch0s == 3:
            x2 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y2 = sha1(x2.encode()).hexdigest()
            print('-----------------------')
            print(y2)
            print('-----------------------')
        ###############################################
        elif ch0s == 4:
            x3 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y3 = sha256(x3.encode()).hexdigest()
            print("-----------------------")
            print(y3)
            print('-----------------------')
        ###############################################
        elif ch0s == 5:
            x4 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y4 = sha512(x4.encode()).hexdigest()
            print("-----------------------")
            print(y4)
            print('-----------------------')
        ###############################################
        elif ch0s == 6:
            x5 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y5 = sha224(x5.encode()).hexdigest()
            print("-----------------------")
            print(y5)
            print('-----------------------')
        ###############################################
        elif ch0s == 7:
            x6 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y6 = sha384(x6.encode()).hexdigest()
            print("-----------------------")
            print(y6)
            print('-----------------------')
        ###############################################
        elif ch0s == 8:
            x7 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y7 = sha3_224(x7.encode()).hexdigest()
            print("-----------------------")
            print(y7)
            print('-----------------------')
        ##############################################
        elif ch0s == 9:
            x8 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y8 = sha3_256(x8.encode()).hexdigest()
            print("-----------------------")
            print(y8)
            print('-----------------------')
        #############################################
        elif ch0s == 10:
            x9 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y9 = sha3_384(x9.encode()).hexdigest()
            print("-----------------------")
            print(y9)
            print('-----------------------')
        ############################################
        elif ch0s == 11:
            x10 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y10 = sha3_512(x10.encode()).hexdigest()
            print("-----------------------")
            print(y10)
            print('-----------------------')
        ###########################################
        elif ch0s == 12:
            x11 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y11 = shake_128(x11.encode()).hexdigest()
            print("-----------------------")
            print(y11)
            print('-----------------------')
        ###########################################
        elif ch0s == 13:
            x12 = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter you want to hash :')
            y12 = shake_256(x12.encode()).hexdigest()
            print("-----------------------")
            print(y12)
            print('-----------------------')
        ###########################################