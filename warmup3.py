#Liam Collins
#1/31/18
#warmup3.py

num = int(input('Enter an integer: '))

if num%2==0 and num%3 !=0:
    print('Number is only divisible by 2')
elif num%3==0 and num%2 !=0:
    print('Number is only divisble by 3')
elif num%2==0 and num%3==0:
    print('Number is divisible by 2 and 3')
else:
    print('Number is divisible by neighter')
