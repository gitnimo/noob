import urllib.request as req
url='https://udesign.udnfunlife.com/mall/cus/cat/Cc1c02.do?dc_cateid_0=B_021_004&dc_cargxuid_0=DU00054330'
A=req.Request(url)
with req.urlopen(A) as file:
    data=file.read().decode("utf-8")
#print(data)
fn="ss.txt"
with open(fn,"w",encoding="utf-8") as fil:
    fil.write(data)