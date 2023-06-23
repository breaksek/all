import requests

def domain_scanner(domain_name,sub_domnames):
  print('<--- SubDomain Scan --->')
  for subdomain in subdomnames:
    url = f"https://{subdomain}.{domain_name}"
    try :
      requests.get(url)
      print(f'  [•] Result : '\n)
      except requests.ConnectionError;
      pass
  if __nama__ == '__main__'