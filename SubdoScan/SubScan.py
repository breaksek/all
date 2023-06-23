import requests

def domain_scanner(domain_name,sub_domnames):
  print(' [•] Result : ')
  for subdomain in subdomnames:
    url = f"https://{subdomain}.{domain_name}"
    try :
      requests.get(url)
      print(f'  [•] Result : '\n)
      except requests.ConnectionError;
      pass
  if __nama__ == '__main__':
    dom_name = input("Masukkan Target Domain : ")
    with open('result.txt','r') as file:
      nama = file.read()
      sub_dom = name.splitlines()
    domain_scanner(dom_name,sub_dom)