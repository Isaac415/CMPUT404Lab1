import requests

print(requests.__version__)

x = requests.get('http://google.com')

print(x.status_code)