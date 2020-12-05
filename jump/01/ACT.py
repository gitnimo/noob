import pandas as pd


course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 1011, 15]
social = [12, 11, 14, 9, 14]
A=pd.DataFrame([chinese,eng,math,nature,social],columns=course,)
total=[A.iloc[i].sum() for i in range(0,5)]
A['total']=total
ave=A.mean()
A.loc['ABC']=ave
A=A.drop(index=['ABC'])
A=A.sort_values(by='total',ascending=False)
A.to_csv("mother.csv")

print(A)



