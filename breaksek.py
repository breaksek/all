# modul
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

banner = """
       1 -> DOS/Windows
       2 -> Termux/Linux
       3 -> Grup Telegram
       4 -> Grup WhatsApp
"""

print(header)
print(author)
print(banner)
pilihOS = int(input("Pilih --> "))

if(pilihOS == 1):
    print("Sabar ya oom masih proses")
    time.sleep(3)
    os.system("python termux.py")
elif(pilihOS == 2):
    print("Sabar ya oom masih proses")
    time.sleep(3)
    os.system("python dos.py")
elif(pilihOS == 3):
    print("Sabar ya oom masih proses")
    time.sleep(3)
    os.system("xdg-open t.me/")
elif(pilihOS == 4):
    print("Sabar ya oom masih proses")
    time.sleep(3)
    os.system("xdg-open chat.whatsapp.com/E35EpFW6PrR8c*Sg7stTN1")
else :
    print("Jangan cari yang gak ada !")
    time.sleep(3)
    os.system("python breaksek.py")
