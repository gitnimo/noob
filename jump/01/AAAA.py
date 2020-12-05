import pandas as pd
p=[1,2,3]
o=[2,3,4]
t=[3,7,5]
s=[4,2,1]
A=pd.Series(p,index=s)
B=pd.Series(o,index=s)
C=pd.Series(t,index=s)

#A.name='dude'
#B.name='good'
#C.name='hello'
O=pd.concat([A,B,C],axis=1)
O.columns=[4,2,3]
print(O)