import requests, re, os, time

os.system("pip install requests")
os.system("clear")

url = input(" [!] Masukkan Target ex(https://target.com) = ")
html = requests.get(url).text
links = re.findall('"(https?://.*?)"', html)
for link in links:
  print(link)