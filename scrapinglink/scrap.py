import requests, r

os.system("pip install requests")
os.system("clear")

url = input(" [!] Masukkan Target = ")
html = requests.get(url).text
links = re.findall('"(https?://.*?)"', html)
for link in links:
  print(link)