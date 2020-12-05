import urllib.request as request
import json
src="http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as op:
    data=json.load(op)
plist=(data["data"])
for i in plist:
    print(i)