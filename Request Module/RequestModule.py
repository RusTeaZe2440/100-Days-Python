import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.google.com")

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())
# Explore more on documentation
