# create a class and a function
class staff:
    def function(self,a,b,c,d):
        count = 0
        for i in a:
            count += 1
        for i in range(count):
            print('The full name is:',a[i]+b[i],',the location is:',c[i],',the role is:',d[i])
        return
# input the name location and role
a = input('Please enter the first name as a list')
b = input('Please enter the last name as a list')
c = input('Please enter the location as a list')
d = input('Please enter the role as a list')

use = staff()
use.function(a,b,c,d)
# an example:
# a = [Sam,Steve]
# b = [Wang,Robert]
# c = [China,Japan]
# d = [leadership,faculty]