from colorama import Fore
def know_hash():
    your = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter your hash :')
    x = 0

    for xx in your:
        x = x + 1

    if x == 32:
        print(your)
        print('----------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] MD5')
        print('----------')
    ##########################
    if x == 40:
        print(your)
        print('------------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA1')
        print('------------')
    #########################
    if x == 64:
        print(your)
        print('----------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA256')
        print(f'[{Fore.GREEN}+{Fore.WHITE}]SHA3_256')
        print('-----------')
    #########################
    if x == 128:
        print(your)
        print('-----------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA512')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA3_512')
        print('-----------')
    #######################
    if x == 56:
        print(your)
        print('------------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA224')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA3_224')
        print('------------')
    #######################
    if x == 96:
        print(your)
        print('-----------')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA384')
        print(f'[{Fore.GREEN}+{Fore.WHITE}] SHA3_384')
        print('-----------')
