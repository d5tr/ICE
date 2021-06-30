from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512
from hashlib import sha224
from hashlib import sha384
from hashlib import sha3_512
from hashlib import sha3_384
from hashlib import sha3_256
from hashlib import sha3_224
import sys
from colorama import *
def encrypt_attack(you_want, file, the_hash):
    # read file
    file = open(file, 'r')
    xx = file.readlines()

    for files in xx :
        files = str(files).strip()



        if you_want == 1 :

            # encrypt
            attack = md5(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.WHITE}---> ", the_hash)
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

                if the_hash == password :
                    print(files,f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ",the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
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

                    if the_hash == password :
                        print(files, f" ---{Fore.GREEN}GOOD-ATTACK{Fore.GREEN}---> ", the_hash)
                        print('''
                        DONE !!
                        INSTA = D_5TR
                        ''')
                        sys.exit()

                    else:
                        print(f'[{Fore.RED}!{Fore.WHITE}]not this :', files, '-->', password)