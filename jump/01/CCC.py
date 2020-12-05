import urllib.request as r
url='http://img.udnfunlife.com/image/product/DS004909/APPROVED/DU00054330/20191129130042979_300.jpg?t=20191231141406'
#A=r.Request(url)
#with r.urlopen(A) as file:
#    print(file.version,file.geturl(),file.status)
#for i in file.getheaders():
 #   print(i)
fn='sss.jpg'
r.urlretrieve(url,fn)