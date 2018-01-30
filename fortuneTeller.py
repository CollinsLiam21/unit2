#Liam Collins
#1/30/18
#fortuneTeller.py

color = input('Pick red or blue: ')
num = int(input('Pick number from 1-4: '))

if color=='red' and num==1:
    print('You will be megged by Christo')
elif color=='red' and num==2:
    print('You will be megged by Earl')
elif color=='red' and num==3:
    print('You will be megged by Liam')
elif color=='red' and num==4:
    print('You will be megged by Aiden')
elif color=='blue' and num==1:
    print('You will meg Dillon')
elif color=='blue' and num==2:
    print('You will meg Christo')
elif color=='blue' and num==3:
    print('You will meg Dillon twice')
elif color=='blue' and num==4:
    print('You will meg Christo three times')
else:
    print('ERROR, fix num or color')