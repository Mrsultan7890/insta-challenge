import requests 

response = requests.get("https://api.ipify.org")

print("public ip:", response.text)




