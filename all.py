# modul
import os,time

banner = """
       1 -> DOS/Windows
       2 -> Termux/Linux
       3 -> Grup Telegram
       4 -> Grup WhatsApp
"""

os.print(banner.txt)
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
