def cal(x,y):
    x = int(x)
    y = int(y)
# check whether money and price meet the requirement
    while (x<0 or y<=0):
        print('Please enter the right amount of money and price')
        x = input('money(should be >=0) = ')
        y = input('price(should be >0) = ')
        x = int(x)
        y = int(y)
# do the calculation
    count = 0
    while x>0:
        x -= y
        if x>=0:
            count += 1
    print('You can afford to buy'+count+'chocolate bars')
    return
# input money and price
x = input('money(should be >=0) = ')
y = input('price(should be >0) = ')
cal(x,y)