import requests
from bs4 import BeautifulSoup

payload = {'text':"ozon", 'lr':"159"}

r = requests.get("https://yandex.ru/search/", params=payload)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
with open("result.txt", "a") as file:
    for link in soup.find_all("a"):
        file.write(link.get("href")+'\n')