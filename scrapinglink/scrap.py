import requests, re, os, time

try:
  pip install requests
  
target = input(" [!] Masukkan Target = ")
html = requests.get(target).text
akhir = re.findall('"https?://.*?)"', html)
for link in akhir:
  print(" [!] Result = " + link)