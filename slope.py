#Liam Collins
#1/17/18
#slope.py - Calculating slope and equation of line

x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))

if x1 != x2:
    m = (y2-y1)/(x2-x1)
    print('slope =', m)
    b = y1-m*x1
    print('Equation of line: Y =', m,'x +', b)

elif x1 == x2:
    print('slope is undefined, line is vertical')


