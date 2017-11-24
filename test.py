import requests

print("hallo")

r = requests.get('https://api.github.com/events')
json = r.json()

for e in json:
    print(e)
    print('======================================')
