import matplotlib.pyplot as plt
highL=['26','34','26','15','20','14','32','26','30','32','27','25','27','30']
plt.plot(highL)
plt.title("weather Report",fontsize=24)
plt.xlabel('',fontsize=14)
plt.ylabel('high',fontsize=14)
plt.tick_params(axis='both',labelsize=12,color='black')
plt.show()
