import requests, re, os, time

os.system("pip install requests")
os.system("clear")

target = input(" [!] Masukkan Target ex(https://target.com) = ")
html = requests.get(target).text
links = re.findall('"(https?://.*?)"', html)
for link in links:
  print(" [!] Result => ")
  print(link)