import pandas as pd
A=[1,2,3]
B=[4,5,6]
C=[7,8,9]
AA=pd.Series(A,index=[3,5,7])
BB=pd.Series(B,index=[3,5,7])
CC=pd.Series(C,index=[3,5,7])
AA.name='147'
BB.name='258'
CC.name='369'
AAA=pd.concat([AA,BB,CC],axis=1)
print(AAA)