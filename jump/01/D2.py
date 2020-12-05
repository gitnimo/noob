import pandas as pd
import matplotlib.pyplot as plt
A={'AA':[1,3,6,4,7],
   'BB':[4,5,2,7,5],
   'town':['Tapei','Tainan','Taithoung','Taidi','Teddy']}
B=pd.DataFrame(A,columns=['AA','BB'],index=A['town'])
B.plot(title='nimo',kind='bar')
plt.xlabel('ss')
plt.ylabel('s')
plt.show()

