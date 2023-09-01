import multiprocessing
import requests

def downloadfile(url,name):
    response = requests.get(url)
    path = r"C:\Users\BHAVESH\OneDrive\Desktop\python 100\MutilProcessing\picture"
    open(f"{path}/{name}.jpg", "wb").write(response.content)

url = "https://stock.adobe.com/search/images"
for i in range(6):
    downloadfile(url,i)

