import requests

url = "https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg//assets/1401.12eba7b734f4ac060bcc.js"

response = requests.get(url)
data = response.json()
print(data)