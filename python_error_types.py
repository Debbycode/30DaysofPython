print('===================SyntaxError=========================')

print('---------------------Example 1--------------------')

>>> print 'My name is Deborah'


print('----------------------Solution-------------------------')

print ('My name is Deborah')

print('===================NameError=========================')


print('--------------------Example 2---------------------')

additon = num1 + num2
print(addition)

print('----------------------Solution-------------------------')

num1 = 4
num2 = 2

additon = num1 + num2
print(addition)
                      
print('===================IndexError=========================')

print('-------------------Example 3----------------------')

my_skills = ['Python', 'Ms Office Suite', 'Power BI', 'SQL']
my_skills[5]

print('----------------------Solution-------------------------')

my_skills = ['Python', 'Ms Office Suite', 'Power BI', 'SQL']
my_skills[0]

print('===================ModuleErrorNotFound=========================')

print('---------------------Example 4--------------------')

import maths

print('----------------------Solution-------------------------')

import math


print('===================AttributeError=========================')

print('---------------------Example 4--------------------')

import math

math.sqroot(2)
#AttributeError: module 'math' has no attribute 'sqroot'

print('----------------------Solution-------------------------')

import math

math.sqrt(2)
#1.4142135623730951

print('===================KeyError=========================')

print('---------------------Example 5--------------------')

user = {'name':'Asab', 'age':250, 'country':'Finland'}
user['naem']
#KeyError: 'naem'

print('----------------------Solution-------------------------')

user = {'name':'Asab', 'age':250, 'country':'Finland'}
user['name']
#'Asab'


print('===================TypeError=========================')

print('---------------------Example 6--------------------')

num1 = 3
num2 = '6'
sum_num = num1+num2
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

print('----------------------Solution-------------------------')
num1 = 3
num2 = 6
sum_num = num1+num2
#8


print('===================ImportError=========================')

print('---------------------Example 7--------------------')

from math import squareroots

#ImportError: cannot import name 'squareroots' from 'math'
#(/Users/mac/opt/anaconda3/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so)

print('----------------------Solution-------------------------')

from math import sqrt














