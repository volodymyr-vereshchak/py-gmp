import requests

def main():  
  payload = {
    "from": "20221129",
    "to": "20221130",
    "organization": 7,
    "offset": 0,
    "limit": 1,
    "filter": "manufacturerName:RGC PRODUCTION",
    "order": "sessionDate:desc,manufacturerName:asc"
  }
  
  headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2b2xvZHlteXIudmVyZXNoY2hhayIsImV4cCI6MTY2OTkwMzIyNCwicm9sZXMiOlsiUk9MRV9ETC1aUC1BTEwtVVNFUlMiLCJST0xFX0RMLUhPLUdNUC1NRVRST0xPR0lTVFMiLCJST0xFX0RMLUhPLUdNUC1ESVNQQVRDSEVSUyJdfQ.INTg9vfFPTAVmOLm2mtkOIS7im4rb14LXpo4romS0ovnW17JR2BNte6CFIx1-PAP6KgCD-ZbL5Inho4ggwErHQ",
  }
  response = requests.get("https://gmp.ent.ukrgas.com.ua/api/devices/total-contacted", headers=headers, params=payload)
  limit = response.json()["totalElements"]
  payload["limit"] = limit
  response = requests.get("https://gmp.ent.ukrgas.com.ua/api/devices/total-contacted", headers=headers, params=payload)
  data = response.json()
  for i in data["content"]:
    print(i["serialNumber"])
  # print(response.json())
  
  # response = requests.get("https://gmp.ent.ukrgas.com.ua", headers=headers)
  # print(response.status_code)
  
  
main()
