import requests
from tools.http_request import HttpRequests
s = requests.session()
data1 = {"action": "signin", "username": "byhy", "password": "111111"}
data2 = {"action": "listbypage", "pagenum": 1, "pagesize": 5, "keywords": "", "_": "1593621930739"}

s.post("http://127.0.0.1/api/sign", json=data1)
# res = s.get("http://127.0.0.1/api/account?action=listbypage&pagenum=1&pagesize=5&keywords=&_=1593621930739")
res = s.get("http://127.0.0.1/api/account", params=data2)
print(res.url)
print(res.text)
