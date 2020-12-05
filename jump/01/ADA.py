import pandas as pd 
U=[7,4,4]
I=[6,3,4]
O=[1,8,6]
p=['Name','Same','Date']
A=pd.Series(U,index=p)
AA=pd.Series(I,index=p)
AAA=pd.Series(O,index=p)
A.name='M'
AA.name='L'
AAA.name='T'
AAAA=pd.concat([A,AA,AAA],axis=1)
print(AAAA['Name'])