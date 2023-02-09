print('=====================One==================')

age = int(input("Please enter your age: "))

if age >= 18:
    print('You are old enough to learn to drive.')

else:
    print(f'You need {18-age} more years to learn to drive.')


print('=====================Two==================')

my_age = 40
your_age = int(input("Please enter your age: "))

if my_age > your_age:
    if (my_age-your_age) == 1:
        print(f'I am {my_age-your_age} year older than you')
    elif my_age == your_age:
        print('Wow! We are the same age.')
    else: 
        print(f'I am {my_age-your_age} years older than you')
        
if my_age < your_age:
    if (your_age-my_age) == 1:
        print(f'You are {your_age - my_age} year older than me')
    elif your_age == my_age:
        print('Wow! We are the same age.')
    else: 
        print(f'You are {your_age-my_age} years older than me')


print('=====================One==================')

num_1 = int(input('Please enter a first number: '))
num_2 = int(input('Please enter a second number: '))

if num_1 > num_2:
    print(f'{num_1} is greater than {num_2}')
elif num_1 < num_2:
    print(f'{num_1} is smaller than {num_2}')
else:
    print(f'{num_1} is equal to {num_2}')
            
            

            
