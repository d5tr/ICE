import random
from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512
from hashlib import sha224
from hashlib import sha384
from hashlib import sha3_224
from hashlib import sha3_256
from hashlib import sha3_384
from hashlib import sha3_512
from hashlib import shake_128
from hashlib import shake_256
from colorama import Fore

def encrypt(ch0s):

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

        x = input('[?] Enter you want to hash :')
        # encrypt
        y = md5(x.encode()).hexdigest()
        print("-----------------------")
        print(y)
        print("-----------------------")



    ##############################################
    elif ch0s == 3:
        x2 = input('[?] Enter you want to hash :')
        y2 = sha1(x2.encode()).hexdigest()
        print('-----------------------')
        print(y2)
        print('-----------------------')
    ###############################################
    elif ch0s == 4:
        x3 = input('[?] Enter you want to hash :')
        y3 = sha256(x3.encode()).hexdigest()
        print("-----------------------")
        print(y3)
        print('-----------------------')
    ###############################################
    elif ch0s == 5:
        x4 = input('[?] Enter you want to hash :')
        y4 = sha512(x4.encode()).hexdigest()
        print("-----------------------")
        print(y4)
        print('-----------------------')
    ###############################################
    elif ch0s == 6:
        x5 = input('[?] Enter you want to hash :')
        y5 = sha224(x5.encode()).hexdigest()
        print("-----------------------")
        print(y5)
        print('-----------------------')
    ###############################################
    elif ch0s == 7:
        x6 = input('[?] Enter you want to hash :')
        y6 = sha384(x6.encode()).hexdigest()
        print("-----------------------")
        print(y6)
        print('-----------------------')
    ###############################################
    elif ch0s == 8:
        x7 = input('[?] Enter you want to hash :')
        y7 = sha3_224(x7.encode()).hexdigest()
        print("-----------------------")
        print(y7)
        print('-----------------------')
    ##############################################
    elif ch0s == 9:
        x8 = input('[?] Enter you want to hash :')
        y8 = sha3_256(x8.encode()).hexdigest()
        print("-----------------------")
        print(y8)
        print('-----------------------')
    #############################################
    elif ch0s == 10:
        x9 = input('[?] Enter you want to hash :')
        y9 = sha3_384(x9.encode()).hexdigest()
        print("-----------------------")
        print(y9)
        print('-----------------------')
    ############################################
    elif ch0s == 11:
        x10 = input('[?] Enter you want to hash :')
        y10 = sha3_512(x10.encode()).hexdigest()
        print("-----------------------")
        print(y10)
        print('-----------------------')
    ###########################################
    elif ch0s == 12:
        x11 = input('[?] Enter you want to hash :')
        y11 = shake_128(x11.encode()).hexdigest()
        print("-----------------------")
        print(y11)
        print('-----------------------')
    ###########################################
    elif ch0s == 13:
        x12 = input('[?] Enter you want to hash :')
        y12 = shake_256(x12.encode()).hexdigest()
        print("-----------------------")
        print(y12)
        print('-----------------------')
    ###########################################