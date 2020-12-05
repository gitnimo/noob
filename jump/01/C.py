import requests
import re
import bs4
url='https://aisweb.ltu.edu.tw/affair/'

#try:
a=requests.get(url)
 #   a.raise_for_status()
#    print("成功")
#except :
 #   print("失敗")
#if a.status_code==requests.codes.ok:
 #   print("Y")
fn='hero.txt'
with open(fn,'wb') as file:
    for line in a.iter_content(40960):
        size=file.write(line)
        print(size)


import requests
url='https://udesign.udnfunlife.com/mall/cus/cat/Cc1c02.do?dc_cateid_0=B_021_004&dc_cargxuid_0=DU00054330'
A=requests.get(url)
fn='oo.txt'
with open(fn,"wb") as file:
    for i in A.iter_content(40960):
        file.write(i)


