import requests

url = "https://price-analytics.p.rapidapi.com/search-by-term"

payload = {
	"source": "amazon",
	"country": "uk",
	"values": "Fire HD 8"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "API KEY",
	"X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
j = response.json()
ji = j["job_id"]
ji = "648450d6a3d544237b97a2ce"
print(ji)
url = "https://price-analytics.p.rapidapi.com/poll-job/" + ji

import time
import datetime

status = "working"
while status == "working":
    response = requests.get(url, headers=headers)
    j = response.json()
    status = j["status"]
    print(status)
    x = datetime.datetime.now()
    print(x)
    time.sleep(2)

r = j["results"][0] # dict_keys(['updated_at', 'query', 'content', 'success'])
c = r["content"]    # dict_keys(['offers', 'offers_count'])
o = c["offers"]     # dict_keys(['price', 'is_prime', 'is_bestseller', 'is_amazon_choice', 'review_count', 'review_rating', 'image', 'link', 'asin', 'name'])
#print(f"results", r.keys())
#print(f"content", c.keys())
#print(f"offers", o[0].keys())

for i in o:
    print(f'{i["price"]} {i["name"]}')
