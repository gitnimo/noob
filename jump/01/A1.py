import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用來正常顯示中文字元
plt.rcParams['axes.unicode_minus'] = False      # 用來正常顯示正負號
#print(matplotlib.matplotlib_fname())

x = np.linspace(1,4,100)
y = x**x
plt.plot(x,y, '+',label='y=x**x函式影象',color='black')
 
plt.xlabel('這是x座標')
plt.ylabel('這是y座標')
plt.title('這是y=x**x的函式影象')
plt.legend()
plt.show()