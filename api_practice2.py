import requests

url = "https://jsonplaceholder.typicode.com/users/"
params = input("ユーザーID")

res = requests.get(url, params=params)

print(res.url)
print(res.text)