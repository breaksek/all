import os, time, random
from banner import *

# coloring
class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
ga = colors()

# source
kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "1234567890"
simbol = "@#$_&-+()/*':;!?"

# question
kombinasi = ga.blue+""" [?] Kombinasi :"""+ga.end+"""\n     1. huruf kecil + besar + angka + simbol\n     2. huruf kecil + besar + angka\n     3. huruf kecil + angka\n     4. huruf besar + angka"""

# program
os.system("clear")
print(bann)
digit = int(input(" [!] Digit ex(8)= "))
print(kombinasi)
kombo = int(input(" [!] Kombinasi = "))
if kombo == 1:
   kombin = kecil + besar + angka + simbol
elif kombo == 2:
   kombin = kecil + besar + angka
elif kombo == 3:
   kombin = kecil + angka
elif kombo == 4:
   kombin = besar + angka
else :
   print(ga.red+"     [!] Udah dibilang pilih yang ada aja"+ga.end)
   time.sleep(5)
   os.system("python generate.py")

hasil = "".join (random.sample(kombin,digit))
hasil1 = "".join (random.sample(kombin,digit))
hasil2 = "".join (random.sample(kombin,digit))
hasil3 = "".join (random.sample(kombin,digit))
hasil4 = "".join (random.sample(kombin,digit))
hasil5 = "".join (random.sample(kombin,digit))

print(ga.green + " [!] Result = " + ga.end + hasil)
print("              " + hasil1)
print("              " + hasil2)
print("              " + hasil3)
print("              " + hasil4)
print("              " + hasil5)
exit()