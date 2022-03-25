#tinydict is the dictionary
tinydict={30:1.03,35:1.07,40:1.11,45:1.17,50:1.23,55:1.32,60:1.42,65:1.55,70:1.72,75:1.94}
print(tinydict[int(input("please input your desired age"))])
print(tinydict)
#print the column
import numpy as np
import matplotlib.pyplot as plt
N=10
risk=(1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)
ind=np.arange(N)
width=0.35
pl=plt.bar(ind,risk,width,yerr=0.01)
plt.ylabel('relative risk')
plt.title('relative CHD risk of different parental ages')
plt.xticks(ind,('30','35','40','45','50','55','60','65','70','75'))
plt.yticks(np.arange(1,2,0.1))
plt.show()