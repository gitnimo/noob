import pandas as pd
R=range(2000,2003)
bee=pd.Series([1,2,3],index=R)
bee1=pd.Series([50,40,60],index=R)
bee2=pd.Series([80,45,70],index=R)

bee.name='1324'
bee1.name='641324'
bee2.name='137424'
numm1=pd.concat([bee,bee1,bee2],axis=1)
print(numm1)
#P={'H':['A','B','C'],'G':['1','2','']}
#U=pd.Series(P)
# H    [A, B, C]
#G     [1, 2, ]
#dtype: object
#U=pd.DataFrame(P)
#print(U)