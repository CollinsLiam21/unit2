#Liam Collins
#1/30/18
#adventure.py

print('Earl is running at you with the ball')
challenge = input('Do you challenge him?')

if challenge == 'yes':
    print('Ok you are in a bit of a pickle because Earl is much better at soccer than you')
    run = input('You have one more chance to give up and run away, do you turn the other way and run?')
    if run == 'yes':
        print('Good job! Your ankles were not broken but unfortunately Earl scored on your team and you lost the game')
    elif run == 'no':
        print('You should have run away, Earl broke your ankles and he scored on you. You lose!')
elif challenge == 'no':
    print('Good choice, You win!')
    rethink = input('Unfortunately your team did not so would you like to rethink your decision?')
    if rethink == 'yes':
        print('Ok you are in a bit of a pickle because Earl is much better at soccer than you')
        run = input('You have one more chance to give up and run away, do you turn the other way and run?')
        if run == 'yes':
            print('Good job! Your ankles were not broken but unfortunately Earl scored on your team and you lost the game')
        elif run == 'no':
            print('You should have run away, Earl broke your ankles and he scored on you. You lose!')
    elif rethink == 'no':
        print('Ok you personally do not lose but your team does :(')
