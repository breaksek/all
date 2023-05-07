# Termux/Linux
import os,time

header = """
======================================================
|     _                    _             _           |
|    | |                  | |           | |          |
|    | |__  _ __ ___  __ _| | _____  ___| | __       |
|    | '_ \| '__/ _ \/ _` | |/ / __|/ _ \ |/ /       |
|    | |_) | | |  __/ (_| |   <\__ \  __/   <        |
|    |_.__/|_|  \___|\__,_|_|\_\___/\___|_|\_\ v1.0  |
|                                                    |
|                                                    |
======================================================"""

author = """
<=================={ Author }=========================>
<==                 BREAKSEK                        ==>
<==       Github : github.com/breaksek/all          ==>
<==         Tiktok : tiktok.com/@breaksek           ==>
<==           Telegram : t.me/breaksek              ==>
<=====================================================>
"""

banner = """       SELAMAT DATANG DI TOOLS BY BREAKSEK
          
          1 => Generator Password
          2 => Cek Ip Domain
          3 => Crack Facebook
          4 => Crack Instagram
          5 => Spam Sms
          6 => Spam Telepon
          7 => Spam Whatsapp
"""

os.system("clear")
print(header)
print(author)
print(banner)
pilih = int(input("Pilih fitur ~> "))

if(pilih == 1):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 2):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 3):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 4):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 5):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 6):
    time.sleep(5)
    print("Maintenance !")
elif(pilih == 7):
    time.sleep(5)
    print("Maintenance !")
else :
    print("Udah dibilang jangan cari yang nggak ada")
    time.sleep(3)
    os.system("python termux.py")
