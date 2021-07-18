import requests
import os
from colorama import Fore


def Decrypt_without_list():

    message = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter your hash : ')

    url = 'https://hashes.com/en/decrypt/hash'

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

    Data = {
        "csrf_token":"e4dae28067482799c72d62e8fbab820f",
        "hashes":f"{message}",
        "knn":"64",
        "submitted":"true",
    }

    Req = requests.post(url, headers=Header, data=Data).text

    if 'Found:' in Req :


        with open('Hash.txt', 'a') as X0 :
            X0.write(Req+'\n')


        with open('Hash.txt', 'r') as Fx :
            for line in Fx :
                if message in line :
                    Remove1 = line.replace('<pre class="mb-0 border-success text-success"><div class="py-1">', '')
                    Remove2 = Remove1.replace('</div></pre>', '')
                    print(f'\n[{Fore.GREEN}+{Fore.WHITE}] Found : '+ Remove2)
                    os.system('rm Hash.txt')

    else:
        print(f'\n[{Fore.RED}!!{Fore.WHITE}] Can"t know hash ! ..')