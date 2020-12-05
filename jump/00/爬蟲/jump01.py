import urllib.request as req
import json
import csv
ur='https://www.twse.com.tw/exchangeReport/BFT41U?response=json&date=&selectType=&_=1589434864462'
with req.urlopen(ur) as qq:
    ioi=json.load(qq)
    for line in ioi['data']:
        print(line)
fn='jump.csv'
with open (fn,'w',newline='') as file:
    wri=csv.writer(file)
    wri.writerow(ioi['title'])
    wri.writerow(ioi['fields'])
    for line in ioi['data']:
        wri.writerow(line)



    



