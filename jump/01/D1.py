import pandas as pd 
import matplotlib.pyplot as plt 
A={'AA':[1,3,6,4,7],
   'BB':[4,5,2,7,5],
   'town':['Tapei','Tainan','Taithoung','Taidi','Teddy']}
B=pd.DataFrame(A,columns=['AA','BB'],index=A['town'])
fig,ax=plt.subplots()
fig.suptitle('City')
ax.set_ylabel('AA')
ax.set_xlabel('BB')

ax2=ax.twinx()
ax2.set_ylabel('TT')
B['AA'].plot(ax=ax2,rot=100)
B['BB'].plot(ax=ax2,style='g-')
ax.legend(loc=1)
ax2.legend(loc=2)
plt.show()