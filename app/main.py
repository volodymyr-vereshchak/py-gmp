import requests

def main():
  # payload = {
  #   "from": "20221129",
  #   "to": "20221130",
  #   "organization": 7,
  #   "offset": 0,
  #   "limit": 10,
  #   "filter": "manufacturerName:RGC PRODUCTION",
  #   "order": "sessionDate:desc,manufacturerName:asc"
  # }
  
  headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2b2xvZHlteXIudmVyZXNoY2hhayIsImV4cCI6MTY2OTkwMzIyNCwicm9sZXMiOlsiUk9MRV9ETC1aUC1BTEwtVVNFUlMiLCJST0xFX0RMLUhPLUdNUC1NRVRST0xPR0lTVFMiLCJST0xFX0RMLUhPLUdNUC1ESVNQQVRDSEVSUyJdfQ.INTg9vfFPTAVmOLm2mtkOIS7im4rb14LXpo4romS0ovnW17JR2BNte6CFIx1-PAP6KgCD-ZbL5Inho4ggwErHQ",
    "Host": "gmp.ent.ukrgas.com.ua",
    "Referer": "https://gmp.ent.ukrgas.com.ua/appliances/all/-2?organization=7&consumerCategory=-2&from=20221129&to=20221130",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
  }
  # response = requests.get("https://gmp.ent.ukrgas.com.ua/api/devices/total-contacted", headers=headers, params=payload)
  # print(response.status_code)
  
  response = requests.get("https://gmp.ent.ukrgas.com.ua", headers=headers)
  print(response.status_code)
  
  
main()
