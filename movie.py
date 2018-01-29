#Liam Collins
#1/29/18
#movie.py

age = int(input('Enter your age: '))

if age >= 18:
    print('You can watch R rated movies')
elif age >= 13:
    print('You can watch PG-13 movies')
elif age >= 7:
    print('You can watch PG movies')
elif age >= 0:
    print('You can watch G movies')
else:
    print('No movies for you!, your not even alive yet')
