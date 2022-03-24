#3.1 code
a=19245301
b=4218520
c=271
#a,b,c represent the total cases of COVID-19 in the UK on 2022.3.7,2021.3.7 and 2020.3.7
d=b-c
e=a-b
#d,e shows the cases added in 2020 and 2021
if d>e:
 print("there are more cases in 2020")
else: print("there are more cases in 2021")
# compare d and e, then give an output
f=b/c
g=a/b
#f,g shows the new cases rate in 2020 and 2021
if f>g:
 print("the rate of new cases is greater in 2020")
else: print("the rate of new cases is greater in 2021" )
#a compare of f,g shows which year's rate is greater

#3.2 code
A=input("A is True or False?")
B=input("B is True or False?")
W=A and B
#A,B and W are booleans
print(W)
