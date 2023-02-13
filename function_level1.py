print('=====================One=======================')

def add_two_numbers (first_num, second_num):
    sum = first_num + second_num
    return (sum)
print (add_two_numbers(5, 4))


print('=====================Two=======================')

def area_of_circle(radius):
    pi = 3.142
    area = pi * (radius**2)
    return (area)

print (area_of_circle(4))


print('=====================Three=======================')


def add_all_nums(*nums):
    # initiate the result as zero
    sum_all = 0
    for num in nums:
        # check if num is number
        if isinstance(num, int):
            sum_all += num
        else:
            print(f'{num} is not an integer')
    return sum_all

numbers = [5,7,8,7,3]            
add_all_nums(*numbers)

        
print('=====================Four========================')
        
def celcius_to_fahrenheit(degrees):
    fahrenheit = ((degrees*(9/5)) + 32)
    return fahrenheit

print (celcius_to_fahrenheit(50))


print('=====================Five=======================')

def check_season(month):
    msg1 = 'Spring'
    msg2 = 'Summer'
    msg3 = 'Autumn'
    msg4 = 'Winter'
    
    if month == 'September' or 'October' or 'November':
        message = msg1
    elif  month == 'December' or 'January' or 'February':
         message = msg1
    elif month == "March" or "April" or "May":
        message = msg3
    elif month == "June" or "July" or "May":
        message = msg4
    else:
        message = msg5
    return (message)


print(check_season('october'))


print('=====================Six=======================')

def calculate_slope(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    return (slope)
    
print (calculate_slope(7, 4, 3, 1))


print('=====================Seven=======================')

# Python program to find roots of quadratic equation
import math 
  
  
# function for finding roots
def solve_quadratic_eqn( a, b, c): 
  
    # calculating discriminant using formula
    discriminant = b * b - 4 * a * c 
    sqrt_value = math.sqrt(abs(discriminant)) 
      
    # checking condition for discriminant
    if discriminant > 0: 
        print('The roots are real and different') 
        print((-b + sqrt_value)/(2 * a)) 
        print((-b - sqrt_value)/(2 * a)) 
      
    elif discriminant == 0: 
        print('The roots are real and the same') 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print('The roots are Complex') 
        print(- b / (2 * a), ' + i', sqrt_value) 
        print(- b / (2 * a), ' - i', sqrt_value) 
  
# Driver Program 
a = -3
b = 26
c = 12
  
# If a is 0, then incorrect equation
if a == 0: 
        print('Input correct quadratic equation') 
else:
    solve_quadratic_eqn(a, b, c)


print('=============================Eight===========================')

n = [3,5,7]
for i in range(0, len(n)):
    print (n[i])


def print_list(lst):
    for num in range(0, len(lst)):
        print (print_list(lst))

print('=============================Nine===========================')

def reverse_list(lst):
    for number in reversed(lst):
        print(number)

reverse_list([1, 2, 3, 4, 5])
# [5, 4, 3, 2, 1]

#reverse_list1(["A", "B", "C"])
# ["C", "B", "A"]


print('=============================Ten===========================')


def capitalize_lst(input):
    lst = [x.upper() for x in input]
    return(lst)
    
print(capitalize_lst(['ade', 'tope']))


print('=============================Eleven============================')

def add_item(lst, item ):
        lst.append(item)
        return(lst)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))    

numbers = [2, 3, 7, 9];
print(add_item(numbers, 5)) 

print('=============================Twelve============================')

def remove_item(lst,item):
    lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
    

print('=============================Thirtheen============================')

def sum_of_numbers(num):
    sum_num = 0 
    for number in range(1, num+1):
        sum_num += number
    return (sum_num)
    
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

print('=============================Fourteen============================')

def sum_of_odds(num):
    sum_odds = 0 
    for number in range(1, num+1):
        if number%2 != 0:
            sum_odds += number
    return (sum_odds)
    
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 25
print(sum_of_odds(100)) # 2500

print('=============================Fifteen============================')

def sum_of_even(num):
    sum_evens = 0 
    for number in range(1, num+1):
        if number%2 == 0:
            sum_evens += number
    return (sum_evens)
    
print(sum_of_even(5))  # 6
print(sum_of_even(10)) # 30
print(sum_of_even(100)) # 2550
      
