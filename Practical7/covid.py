import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import data
os.chdir("/Users/86150/PycharmProjects/Practical7")
covid_data = pd.read_csv("full_data.csv")
# store data of Afghanistan in check1
check1 = []
for i in range(len(covid_data)):
    country = covid_data.loc[i,"location"]
    if country == "Afghanistan":
        marker1 = True
    else: marker1 = False
    check1.append(marker1)
print(covid_data.loc[check1,"total_cases"])
# store data of China in check2
check2 = []
for i in range(len(covid_data)):
    country = covid_data.loc[i,"location"]
    if country ==  "China":
        marker2 = True
    else: marker2 = False
    check2.append(marker2)
new_cases = covid_data.loc[check2,"new_cases"]
new_deaths = covid_data.loc[check2,"new_deaths"]
date = covid_data.loc[check2,'date']
# the mean of new cases and new deaths
print('the mean of the new cases in China equals',np.mean(new_cases))
print('the mean of the new deaths in China equals',np.mean(new_deaths))
# boxplot of new cases
plt.boxplot(new_cases,labels = ['new_cases'])
plt.title('new cases in China')
plt.ylabel('cases')
plt.show()
# boxplot of new deaths
plt.boxplot(new_deaths,labels = ['new_deaths'])
plt.title('new deaths in China')
plt.ylabel('cases')
plt.show()
# new cases over time
plt.plot(date,new_cases,'r+')
plt.title('new cases over time in China')
plt.ylabel('cases')
plt.xlabel('time')
plt.show()
# new deaths over time
plt.plot(date,new_deaths,'g+')
plt.title('new deaths over time in China')
plt.ylabel('cases')
plt.xlabel('time')
plt.show()

# additional question
# store data of Australia in check3
check3 = []
for i in range(len(covid_data)):
    country = covid_data.loc[i,"location"]
    if country ==  "Australia":
        marker3 = True
    else: marker3 = False
    check3.append(marker3)
new_cases = covid_data.loc[check3,"new_cases"]
total_cases = covid_data.loc[check3,"total_cases"]
# new cases over time in Australia
plt.plot(date,new_cases,'b+')
plt.title('new cases over time in Australia')
plt.ylabel('cases')
plt.xlabel('time')
plt.show()
# total cases over time in Australia
plt.plot(date,total_cases,'r+')
plt.title('total cases over time in Australia')
plt.ylabel('cases')
plt.xlabel('time')
plt.show()