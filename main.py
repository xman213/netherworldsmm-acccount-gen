import requests
import json
import random
import string
import pystyle
import threading
import user_agent
from pystyle import *
import os

os.system('title netherworldsmm.com account gen (made by xman) github.com/xman213')
open("accs.txt", "a").write('Format is username:password \n\n')
def gen():
    while True:
        f = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=3))
        headers = {
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "Accept-Encoding": 'gzip, deflate, br',
            "Accept-Language": 'en-US,en;q=0.9',
            "Cache-Control": 'max-age=0',
            "Connection": 'keep-alive',
            "Content-Length": '381',
            "Content-Type": 'application/x-www-form-urlencoded',
            "Cookie": 'PHPSESSID=lgkc8bphm92rvgqlpkk4eh83uh; _csrf=4a5a1dee066826ba99064d8892a47b1ba382e550f971a673c5dc6ea503bdd643a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Ua9dFiwOCCcdmEZdde6ZoXUyrR2D462S%22%3B%7D',
            "Referer": 'https://netherworldsmm.com/signup',
            "User-Agent": user_agent.generate_user_agent(),
        }
        user = f"xman{f}"
        password = "xman#1111"
        data = {
            'RegistrationForm[login]': user,
            'RegistrationForm[email]': f'xman{f}@xman.com',
            'RegistrationForm[first_name]': 'xman',
            'RegistrationForm[last_name]': 'cman',
            'RegistrationForm[password]': password,
            'RegistrationForm[password_again]': password,
            'RegistrationForm[termsofservice]': '1',
            '_csrf': 'hiqz8AOc4sS4KO6m-O0mKMc3eJKg10XXB5208JSjh-bTS4qURfWVi_trjcKVqHxMo1JOyM-PEK51z4a0oJW1tQ=='
        }


        open("accs.txt", "a").write(user+f':{password}\n')
        r = requests.post('https://netherworldsmm.com/signup', headers=headers, data=data)

        if r.status_code == 200 or 302:
            print(Colorate.Horizontal(Colors.blue_to_red, 'account made!'))
        else:
            print(Colorate.Horizontal(Colors.blue_to_red,'account not made!'))
            
threads = input(Colorate.Horizontal(Colors.blue_to_red,'threads: '))
if threading.active_count() < int(threads):
        threading.Thread(target=gen).start()         
