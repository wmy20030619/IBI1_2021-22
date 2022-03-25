
#input new students' scores
marks=input("please input your scores")
#change the input into integers
a = marks.split(' ')
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
print(sorted(b))
#calclate the mean
import numpy as np
A=np.mean(b)
#judge whether the mean is above 60
if A>=60:
    print("the average is over 60,pass")
else: print("the average is below 60,fail")
#print the plot
import matplotlib.pyplot as plt
plt.boxplot(b)
plt.show()