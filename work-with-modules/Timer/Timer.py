from pyfiglet import figlet_format
from colorama import Fore ,init
init()
from time import sleep
import datetime
import os
while True:
    Times = datetime.datetime.now().strftime('%H : %M : %S')
    print(Fore.BLUE+(figlet_format(Times)))
    sleep(1)
    os.system('clear || cls')
print('hello')
