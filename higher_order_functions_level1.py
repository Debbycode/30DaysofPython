
print('======================One=======================')
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
sum = reduce(add, numbers)
# sum is now 10


print('=====================Two==========================')

print('''A higher-order function is a function that takes another function as an argument or returns a function as its result. Higher-order functions are an important part of functional programming and they allow you to create more abstract, reusable code.

A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.

A decorator is a special type of function that takes another function as input, extends the behavior of the input function, and returns the input function with the extended behavior. In Python, decorators are applied to functions or classes using the @ symbol. Decorators are often used to add extra functionality to functions or classes, such as timing a function or limiting the number of times a function can be called.''')


print('=====================Three==========================')

#call function

def call(func, *args, **kwargs):
    return func(*args, **kwargs)   #The call function is a theoretical example and is not a built-in function in Python.


#call function before map:

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled_numbers = list(map(call, [double] * len(numbers), numbers))
# doubled_numbers is now [2, 4, 6, 8]


#call function before filter:

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4]
even_numbers = list(filter(call, [is_even] * len(numbers), numbers))
# even_numbers is now [2, 4]

#call function before reduce:

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
sum = reduce(call, [add] * (len(numbers) - 1), numbers)
# sum is now 10

print('=====================Four==========================')


countries = ['Nigeria', 'China', 'Malawi', 'Ethopia']
for country in countries:
    print(country)

# Output:
# Nigeria
# China
# Malawi
# Ethopia


print('=====================Five==========================')

names = ['Adeboye', 'Tijani', 'Eze', 'Fejiro']
for name in names:
    print(name)


print('=====================Six==========================')

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5

