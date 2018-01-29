#Liam Collins
#1/29/18
#unitConverter.py

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')

num = int(input('Choose a number: '))

if num == 1:
    kilom = float(input('Enter number of kilometers: '))
    mile = kilom*.621371
    print(kilom, 'kilometers is', mile, 'miles')
elif num == 2:
    kilog = float(input('Enter number of kilograms: '))
    pounds = kilog*2.20462
    print(kilog, 'kilograms is', pounds, 'pounds')
elif num == 3:
    liter = float(input('Enter number of liters: '))
    gal = liter*0.264172
    print(liter, 'liters is', gal, 'gallons')
