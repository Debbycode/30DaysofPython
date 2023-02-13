print('========================One==============================')

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return (False)
        else:
            return (True)
    
print(is_prime(5))
print(is_prime(12))

print('========================Two==============================')

def is_unique(lst):
    
    if (len(set(lst)) == len(lst)):
        print('All element are unique')
    else:
        print('All element are not unique')
my_list = ['Mon','Tue','Wed']            
is_unique(my_list)


print('========================Three==============================')

def is_same(lst):
    if(len(set(lst))==1):
        print ('All elements in list are same.')
    else:
        print ('All elements in list are not the same.')
  
my_list = ['z','z','z','z', 'y']
is_same(my_list)


print('========================Four==============================')

def is_valid_python_var(name):
    if string.isidentifier():
        print(f'"{name}" is a valid Identifier')
    else:
        print(f'"{name}" is NOT a valid Identifier')
 

string = "-Search"
is_valid_python_var(string)
 
string = "123"
is_valid_python_var(string)
 
string = "_abc12"
is_valid_python_var(string)


print('========================Five================================')
import json
from collections import Counter

with open('countries_data.py')  as f:
    data = json.load(f)

def most_spoken_languages(n):
    languages = [country['languages'] for country in data]
    language_list = [language for sublist in languages for language in sublist]
    counter = Counter(language_list)
    most_spoken_langauge =  counter.most_common(10)
    return(most_spoken_langauge)


print(most_spoken_languages(10))

print('========================Six==================================')

import json
from collections import Counter

with open('countries_data.py')  as f:
    data = json.load(f)

    
def most_populated_countries(n):
    countries_by_population = sorted(data,key=lambda x: x["population"], reverse = True)
    most_populated_countries = countries_by_population[:10]
    return (most_populated_countries)

print(most_populated_countries(10))






