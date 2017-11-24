import requests

print("hallo")

r = requests.get('https://api.github.com/events')
json = r.json()

print(json[2])
