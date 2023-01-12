import requests

print(requests.__version__)

x = requests.get('http://google.com')

r = requests.get('https://raw.githubusercontent.com/Isaac415/CMPUT404Lab1/main/lab1.py')

print(r.text)