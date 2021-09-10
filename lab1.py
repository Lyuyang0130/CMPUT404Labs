import requests

print(requests.__version__)
url_for_g = requests.get('http://google.com/')
print(url_for_g)

url = 'https://raw.githubusercontent.com/Lyuyang0130/CMPUT404Labs/main/lab1.py'


f = requests.get(url)
print(f.text)