print('=====================One==================')

print('No\tScore\tGrades ')
print('1.\t80-100\tA')
print('2.\t70-89\tB')
print('3.\t60-69\tC')
print('4.\t50-59\tC')
print('5.\t0-49\tD')

score = int(input('Enter your test score: ' ))

#if 78 <= grade <= 89:
          
if 80 <= score <= 100:
    print('Grade: A')
elif 70 <= score <= 89:
    print('Grade: B')
elif 60 <= score <= 69:
    print('Grade: C')
elif 50 <= score <=59:
    print('Grade: D')
else:
    print('Grade: F')


print('=====================Two==================')

print('No\tSeasons')
print('1.\tAutumn')
print('2.\tWinter')
print('3.\tSpring')
print('4.\tSummer')

month = input('please enter any month of the year: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn!')

elif month == 'December' or  month == 'January' or month == 'February':
    print('The season is Winter!')

elif month == 'March' or  month == 'April' or month == 'May':
    print('The season is Spring!')

elif month == 'June' or  month == 'July' or month == 'August':
    print('The season is Winter!')


print('=====================Three==================')

fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in fruits:
    fruit_input = input('Enter name of fruit: ')
    if fruit_input not in fruits:
        fruits.append(fruit_input)
        print(fruits)
    else:
        print('The fruit already exist in the list!')
