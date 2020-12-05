import urllib.request as req
url='https://tw.op.gg/champion/statistics'
a=req.Request(url)                       #a=req.urlopen(url)
with req.urlopen(a) as file:             #print(a.read().decode("utf-8"))
    data=file.read().decode("utf-8")
fn='opgg.txt'
with open(fn,"w",encoding="utf-8") as fil:
    fil.write(data)