import py_compile
from colorama import Fore
def py_encrypt(file):
    py_compile.compile(file)
    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done encrypt file ..')
