import requests

s = input()
response = requests.get(s)
print(response.status_code)
print(response.text)