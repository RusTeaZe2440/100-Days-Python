import requests
import json


ask = input("Search for latest news here:\n")
url = (f"https://newsapi.org/v2/everything?q=tesla&from=2023-02-28&sortBy=publishedAt&apiKey=59cd075d87924235b6cd2b7e8d1d9234")
res = requests.get(url)
news = json.loads(res.text)

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print("****************")