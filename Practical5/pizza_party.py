#start at the first cut
n=1
p=0
#finish cutting?
while p<64:

#False
#calulate the slices
 p=0.5*(n**2+n+2)
#print the total slices
 print("the number of cut is:",n,"the number of pizza slices is:",p)
#have a more cut
 n+=1
#repeat
print('after',n-1,'cuts,the number of pizza slices can be 64')
#True
#finish
