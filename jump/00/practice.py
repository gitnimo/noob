#import pandas as pd
#data=pd.Series([5,2,1,-5,9,8411],index=["a","sa","s","asse","ss","f"])
#print(data)

import pandas as pd
data=pd.DataFrame({
    "name":["nimo","bob","opt"],
    "ioi":["sPOf","asoid","saprmf"],
},index=["a","b","c",])
#print(data)
#print("------------------")
#print(data.iloc[2],sep="\n")
#print(data.loc["c"],sep="\n")
#print(data.shape)
#print(data.index)
print(data["name"],sep="\n")
iooi=data["name"]
print("把name全部轉大寫",iooi.str.upper(),sep="\n")
data["jump"]=[5500,500,90]
data["cp"]=data["jump"]
print(data)
