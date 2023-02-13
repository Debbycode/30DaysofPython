print('=======================One=====================')

sum = 0

for number in range(0, 101):
    sum = sum + number
    print(f'The sum of all number is {sum}')
print()

print('=======================Two=====================')

even_sum = 0
odd_sum = 0

for num in range(0,101):
    if num%2 != 0:
        odd_sum = odd_sum + num
        continue
    if num%2 == 0:
        even_sum = even_sum + num
        print(f'The sum of all odds is {even_sum}. And the sum of all evens is {odd_sum}')

    

