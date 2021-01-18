import requests
import json

logo=r"""
 _             _             _                
(_)           | |           | |               
 _ _ __ ______| | ___   ___ | | ___   _ _ __  
| | '_ \______| |/ _ \ / _ \| |/ / | | | '_ \ 
| | |_) |     | | (_) | (_) |   <| |_| | |_) |
|_| .__/      |_|\___/ \___/|_|\_\\__,_| .__/ 
  | |                                  | |    
  |_|                                  |_|    
                        by Sudano#7479
"""
print(logo)

ip = input("IP: ")

r = requests.get('http://extreme-ip-lookup.com/json/' + ip)
y = json.loads(r.text)

if "fail" in y["status"]:
  print("Ocorreu um erro ao pegar as informações do IP")
  exit()

print("Cidade: " + y["city"])
print("Estado: " + y["region"])
print("País: " + y["country"])
print("Lat: " + y["lat"] + " | Lon: " + y["lon"])
