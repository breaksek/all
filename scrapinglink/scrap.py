import requests, re, os, time

os.system("pip install requests")
os.clear()

target = input(" [!] Masukkan Target = ")
html = requests.get(target).text
links = re.findall('"https?://.*?)"', html)
for link in links:
  print(" [!] Result = " + link)