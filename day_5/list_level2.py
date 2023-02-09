ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(=================Sort, Minimum, Maximum========================)

print('Sorted ages: ', ages.sort())

min_age = (min(ages)
print('Minimum Number: ', min_age)
           
max_age =(max(ages))
print('Maximum Number: ', max_age)

print(=================Append Minimum & Maximum Ages================)

ages.append(min_age)
print('Updated ages including minimum number: ', ages)
           
ages.append(max_age)
print('Updated ages including maximum number: ', ages)

print(=================Median========================)

num_ages = len(ages)
ages.sort()

median1 = ages[n//2]
median2 = ages[n//2 -1 ]
median = (median1 + median2)/2
           
print('Median is: ', median)

print(=================Average========================)

num_ages = len(ages)
sum_ages = sum(ages)
           
average_age = sum_ages)/num_ages
print('Average age is: ', average_age)

print(=================Range=======================)

age_range = max_age - min_age

print('Maximum and minimum range is: ', age_range)


print(=================Absolute Age========================)
def maximum(x, y):
    
    return ((x + y + abs(x - y)) / 2)

def minimum(x,y):
    
    return ((x + y - abs(x - y)) / 2)



print(=================One========================)

import requests

countries = https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py

country_list = requests.get(countries)

print(country_list)

print(=================Two========================)

half_length = len(country_list)//2

first_half, second_half = country_list[:half_length], country_list[half_length:]

print(f'{first_half=}')



print(=================Three========================)

3. countries = ['China', 'Russia','USA','Finland','Sweden','Norway','Denmark']

CHN, RSA, US = countries

print(CHN)
print(RSA)
print(US)           

           
