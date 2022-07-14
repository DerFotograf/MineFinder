import socket
import os
import threading
import concurrent.futures
from os import system, name
import colorama
from colorama import Fore
import time
colorama.init()

print_lock = threading.Lock()

os.system("cls")
time.sleep(1)
os.system(f'title MineFinder V1 / By Fotograf.')
print(f'''{Fore.RED}
  ███▄ ▄███▓  ██▓ ███▄    █  ▓█████   █████  ██▓ ███▄    █ ▓█████▄  ▓█████ ██▀███  
 ▓██▒▀█▀ ██▒▒▓██▒ ██ ▀█   █  ▓█   ▀ ▓██    ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌ ▓█   ▀▓██ ▒ ██▒
 ▓██    ▓██░▒▒██▒▓██  ▀█ ██▒ ▒███   ▒████  ▒▒██▒▓██  ▀█ ██▒░██   █▌ ▒███  ▓██ ░▄█ ▒
 ▒██    ▒██ ░░██░▓██▒  ▐▌██▒ ▒▓█  ▄ ░▓█▒   ░░██░▓██▒  ▐▌██▒░▓█▄   ▌ ▒▓█  ▄▒██▀▀█▄  
▒▒██▒   ░██▒░░██░▒██░   ▓██░▒░▒████▒░▒█░   ░░██░▒██░   ▓██░░▒████▓ ▒░▒████░██▓ ▒██▒
░░ ▒░   ░  ░ ░▓  ░ ▒░   ▒ ▒ ░░░ ▒░ ░ ▒ ░    ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
░░  ░      ░░ ▒ ░░ ░░   ░ ▒░░ ░ ░  ░ ░     ░ ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░ ░    ░▒ ░ ▒ 
 ░      ░   ░ ▒ ░   ░   ░ ░     ░    ░ ░   ░ ▒ ░   ░   ░ ░  ░ ░  ░     ░    ░░   ░ 
░       ░     ░           ░ ░   ░  ░         ░           ░    ░    ░   ░     ░     

''')
time.sleep(2)

ipadr = input(f"{Fore.RED}>> {Fore.BLUE}Introduce la IP o dominio a escanear: {Fore.WHITE}")

def minefinder(ipadr, port):
    mapper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mapper.settimeout(8)
    try:
        mapper.connect((ipadr, port))
        mapper.close()
        with print_lock:
            print(" ")
            print(f"{Fore.GREEN}El puerto{Fore.WHITE}", [port], f"{Fore.GREEN}está abierto.")
            print(" ")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
    for port in range(2000):
        executor.submit(minefinder, ipadr, port + 1)