import requests, re

url = input(" [!] Masukkan Target = ")
html = requests.get(url).text
links = re.findall('"(https?://.*?)"', html)
for link in links:
  print(link)