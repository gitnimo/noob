from urllib import request,error   #抓取抓取網頁錯誤
eurl='https://draaq.de/tw200202/1.html'
try:
    A=request.urlopen(eurl)
except error.HTTPError as r:
    print("錯誤原因",r.code,r.reason,r.headers)
except error.URLError as e:
    print("錯誤原因:::",e.reason)
else:
    print("成功")
url='https://dramaq.de/tw200202/1.html'
try:
    B=request.Request(url)
except error.URLError as g:
    print("失敗",g.reason)
else:
    print('OK')    