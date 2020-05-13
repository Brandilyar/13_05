import requests
from bs4 import BeautifulSoup
import re
import os

path_now = os.getcwd()
URL = input("Введите URL, который выхотите спасрсить: \n")
name_folder = input("Введите название папки: \n")
os.mkdir(name_folder)
page=requests.get(URL.strip())

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
results = soup.find_all('img', src = re.compile('\/[a-z]+\/\d+\/\d+\.jpg'))
print(results)

# our_arr = []
print(type(results))
print(len(results))

for i in range(len(results)):
    link = results[i]['src']
    print(link)
    img_data = requests.get("https://www.combook.ru" + link)
    print(img_data.content)
    with open(name_folder+"/"+str(i)+".jpg", "wb") as handler:
        handler.write(img_data.content)








