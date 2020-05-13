import requests

r = requests.get("https://en.wikipedia.org/wiki/HR_6819")
print(r.text)
print(type(r))
print(dir(r))
# print(help(r))