#Liam Collins
#1/29/18
#gradeCalculator.py

grade = round(float(input('Enter your percentage grade: ')))

if grade>=90:
    print('You earned an A')
elif grade>=80:
    print('You earned a B')
elif grade>=70:
    print('You earned a C')
elif grade>=60:
    print('You earned a D')
else:
    print('You earned an NC, try harder!')

