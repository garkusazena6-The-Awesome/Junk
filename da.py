"""
import urllib.request
"""
from bs4 import BeautifulSoup
import requests
"""
opener = urllib.request.build_opener()
response = opener.open("https://www.python.org/")
print(response.read())
responce1 = requests.get("https://www.python.org/")
print(responce1.text)
"""
"""
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for element in response_parse:
    if element.startswith("$"):
        print(element)
"""
"""
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    list_1 = soup.find_all("div",{"class":"sc-fa25c04c-0 eAphWs"})
    res = list_1[1].find("span")
    print(res.text)
"""
url = "https://sinoptik.ua/"
response = requests.get(url)
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.find_all("p",{"class":"R1ENpvZz"})
    for i in temp:
        print(i.text)
