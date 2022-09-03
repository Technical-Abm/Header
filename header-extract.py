# -*- coding: utf-8 -*-

import os
import time
import requests
from datetime import datetime
import platform

AUTHOR = "Technical Abm"
GITHUB = "https://github.com/Technical-Abm"
FACEBOOK = "https://www.facebook.com/techabm"

from datetime import datetime
now = datetime.now()
b = requests.get('https://api.ipify.org').text.strip()
ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}).json()['country_name'].lower()
Your_aarch = platform.uname()[4]
Today_time = now.strftime('%H:%M:%S')
Today_date = now.strftime('%Y/%m/%d')

DEVICE = """
        d8888b.  .d8b.  d888888b  .d8b.
        88  `8D d8' `8b `~~88~~' d8' `8b
        88   88 88ooo88    88    88ooo88
        88   88 88~~~88    88    88~~~88
        88  .8D 88   88    88    88   88
        Y8888D' YP   YP    YP    YP   YP
---------------------------------------------------
 (~) Auhtor : {}
 (~) Github : {}
 (~) FB Page: {}
---------------------------------------------------
        (~) Device Aarch: {}
        (~) Your Region : {}
        (~) Today Time  : {}
        (~) Today Date  : {}
---------------------------------------------------
""".format(AUTHOR,GITHUB,FACEBOOK,Your_aarch,ips,Today_time,Today_date)

class colors(object):
    def __init__(self):
        self.colorma = {
            "white" : "\033[1;97m",
            "red" : "\033[1;91m",
            "none": "\033[1;0m"
        }

class dev(object):
    def __init__(self):
        os.system("cls")
        print(DEVICE)
        print(colors().colorma["none"],"[1] Get header from website domains",colors().colorma["none"])
        print()
        self.null = input(" [!] Select an option :- ")
        if "1" in self.null:
            os.system("cls")
            print(DEVICE)
            print()
            print(colors().colorma["yellow"],"\t Enter any domains name to get website api headers ",colors().colorma["none"])
            time.sleep(1)
            self.domains = input(" Enter domains name :- ")
            self.result = requests.get("https://api.hackertarget.com/httpheaders/?q="+self.domains).text
            print()
            print("\t  Domains website headers ")
            print()
            print(" {} ".format(self.result))
            time.sleep(3)
            exit()
        else:
            print(colors().colorma["red"],"Please select an valid option",colors().colorma["none"])

dev()
