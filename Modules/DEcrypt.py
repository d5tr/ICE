import requests
import os
from hashlib import *
import sys
from colorama import *

class Decrypts :
    
    def __init__(self, Hash):
        self.Hash = Hash


    
    def encrypt_attack(self, you_want, file):
        # read file
        file = open(file, 'r')
        xx = file.readlines()

        for files in xx :
            files = str(files).strip()



            if you_want == 1 :

                # encrypt
                attack = md5(files.encode()).hexdigest()
                password = attack

                if self.Hash == password :
                    print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.WHITE}---> ", self.Hash)
                    print('''
                    DONE !!
                    INSTA = D_5TR
                    ''')
                    sys.exit()

                else:
                    print(f'[{Fore.RED}!{Fore.WHITE}]not this :',files,'-->',password)

            if  you_want == 2:

                    attack = sha1(files.encode()).hexdigest()
                    password = attack

                    if self.Hash == password :
                        print(files,f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                        print('''
                        DONE !!
                        INSTA = D_5TR
                        ''')
                        sys.exit()

                    else:
                        print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 3:


                        attack = sha256(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 4:

                        attack = sha512(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 5:

                        attack = sha224(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 6:

                        attack = sha384(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:

                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 7:

                        attack = sha3_512(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 8:

                        attack = sha3_384(files.encode()).hexdigest()
                        password = attack

                        if self == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 9:

                        attack = sha3_256(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

            if you_want == 10:

                        attack = sha3_224(files.encode()).hexdigest()
                        password = attack

                        if self.Hash == password :
                            print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", self.Hash)
                            print('''
                            DONE !!
                            INSTA = D_5TR
                            ''')
                            sys.exit()

                        else:
                            print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)

    
    def Decrypt_without_list(self):
        
        # url web to decrypt hash 
        url = 'https://hashes.com/en/decrypt/hash'
        
        # headers 
        Header = {
            'Host': 'hashes.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '105',
            'Origin': 'https://hashes.com',
            'Connection': 'keep-alive',
            'Referer': 'https://hashes.com/en/decrypt/hash',
            'Cookie': 'csrf_cookie=e4dae28067482799c72d62e8fbab820f',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # data
        Data = {
            "csrf_token":"e4dae28067482799c72d62e8fbab820f",
            "hashes":f"{self.Hash}",
            "knn":"64",
            "submitted":"true",
        }
        
        # send request
        Req = requests.post(url, headers=Header, data=Data).text

        if 'Found:' in Req :


            with open('Hash.txt', 'a') as X0 :
                X0.write(Req+'\n')


            with open('Hash.txt', 'r') as Fx :
                for line in Fx :
                    if self.Hash in line :
                        Remove1 = line.replace('<pre class="mb-0 border-success text-success"><div class="py-1">', '')
                        Remove2 = Remove1.replace('</div></pre>', '')
                        print(f'\n[{Fore.GREEN}+{Fore.WHITE}] Found : '+ Remove2)
                        os.system('rm Hash.txt')

        else:
            print(f'\n[{Fore.RED}!!{Fore.WHITE}] Can"t know hash ! ..')

    def decrypt_Caesar(self, key):
        
        print(f'\n{Fore.RED}-----------Result----------{Fore.WHITE}\n')
        
        Text = list(self.Hash)
        KEYS = 0
        for Trying in range(key):
            
            Clist = []
            for crypt in Text:
                
                # letter order from 1 to 26
                Order = ord(crypt)
                # Encrypt
                encrypt = chr(Order-KEYS)
                # add to list
                Clist.append(encrypt)
                
            # converting to str
            converting = ''.join(Clist)
            print(f'> {Fore.GREEN}{converting}{Fore.WHITE}')

            KEYS = KEYS+1

    def decrypt_Monoalphabetic(self):

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

        CI = []

        for encrypT in self.Hash:
            # set nummber for letters in Text
            LN = Keys.index(encrypT)
            # switch KN => Keys
            NK = letters[LN]
            # return NL in CI
            CI.append(NK)

        # converting to str
        ET = ''.join(CI)
        print(f'\n Result {Fore.CYAN}==>{Fore.WHITE} ', ET)

    def decrypt_vigenere(self, txt, key):

        CL = []

        for (letter, kex) in zip (txt, key):
            
            # to see rank of letter
            TP = ord(letter)
            # to see rank of number 
            KP = ord(kex)

            NL = chr(TP - KP)

            CL.append(NL)

        end = ''.join(CL)

        print(f'\n Result {Fore.CYAN}==>{Fore.WHITE} ', end)


