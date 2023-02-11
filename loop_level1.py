print('=========================One============================')

for number in range(11):
    print (number)
else:
    print('Loop stopped!')

print('--------------------')

number = 0
while number < 11:
    print(number)
    number += 1

    

    
print('=========================Two============================')

for number in range(10,0,-1):
    print (number)
else:
    print('Loop Stopped!')
    
print('--------------------')

number = 10         
while number > 0:
    print(number)
    number -= 1

print('=========================Three============================')

height = 7
for row in range(1, height+ 1):
    print(" " * (row - height) + "#" * row)

print('=========================Four============================')

n= 8

for x in range(n):
    for y in range(n):
        print('#', end =' ')
    print()


print('=========================Five============================')

for x in range(11):
        print(f'{x} x {x} = {x*x}')



print('=========================Six============================')


framework = ['Python', 'Numpy','Pandas','Django', 'Flask']

for program in framework:
    print(program)

print('=========================Seven============================')

for number in range(0, 100):
    if number%2 == 0:
        print(number, end= ' ')
        #number+=1

print('=========================Eight============================')

for number in range(0, 100):
    if number%2 !=0:
        print(number, end = ' ')
        #number+=1



        
