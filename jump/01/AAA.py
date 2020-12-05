import requests
url='http://www.httpbin.org/post'
fromdata={'gender':'M','page':'1'}
r=requests.post(url,data=fromdata)
print(r.url)
print('*'*70)
print(r.text)