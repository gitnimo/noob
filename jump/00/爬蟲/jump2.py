import urllib.request as req
url="https://www.ikea.com.tw/zh/products/beds/double-beds?&&page=3"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
ioi=root.find_all("div",class_="itemDetails")
for itemDetails in ioi:
    if itemDetails.span :
       print(itemDetails.span.string)



#titles=root.find_all("div",class_="itemDetails")
#for itemDetails in titles:
#    if itemDetails.span !=None:
 #       print(itemDetails.span.string)  
