import requests


class HttpRequests():
    def __init__(self, url, method, data=None, cookies=None):
        self.url = url
        self.data = data
        self.method = method
        self.cookies = cookies

    def send_request(self, type):
        if type == 'json':
            if self.method == 'post':
                res = requests.post(self.url, json=self.data, cookies=self.cookies)
            elif self.method == 'put':
                res = requests.put(self.url, json=self.data, cookies=self.cookies)
            elif self.method == 'delete':
                res = requests.delete(self.url, json=self.data, cookies=self.cookies)
            else:
                res = None
        elif type == 'data':
            if self.method == 'post':
                res = requests.post(self.url, data=self.data, cookies=self.cookies)
            elif self.method == 'put':
                res = requests.put(self.url, data=self.data, cookies=self.cookies)
            elif self.method == 'delete':
                res = requests.delete(self.url, data=self.data, cookies=self.cookies)
            else:
                res = None
        elif type == 'params':
            res = requests.get(self.url, params=self.data, cookies=self.cookies)
        else:
            res = None
            print("数据方式不全，待完善")
        return res
