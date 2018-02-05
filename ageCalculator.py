#Liam Collins
#2/2/18
#ageCalculator.py

from datetime import date

year = int(input('Enter year you were born: '))
month = int(input('Enter the month you were born in: '))
day = int(input('Enter the day you were born on: '))
age = date.today().year-year
age2 = date.today().year-year-1

if month < date.today().month:
    print(age)
elif month == date.today().month and day < date.today().day:
    print(age)
elif month == date.today().month and day > date.today().day:
    print(age2)
elif month > date.today().month:
    print(age2)
else:
    print('Happy Birthday! You are now', age, 'years old!')
