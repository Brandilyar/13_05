import requests
from bs4 import BeautifulSoup
import os


region_kod = input("Введите код региона: ")
text_search = input("Введите текст поиска: ")

payload = {'text':text_search, 'lr':region_kod}

r = requests.get("https://yandex.ru/search/", params=payload)

soup = BeautifulSoup(r.text, 'html.parser')


with open("result.txt", "a") as file:
    for link in soup.find_all("a"):
        if link.get('href').startswith('https://'):
            file.write(link.get("href")+'\n')