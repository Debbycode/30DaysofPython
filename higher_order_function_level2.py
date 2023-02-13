print('==========================One===========================')

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola']
uppercase_countries = list(map(lambda x: x.upper(), countries))
print(uppercase_countries)



print('==========================Two============================')

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)
# Output: [1, 4, 9, 16, 25]


print('==========================Three============================')

names = ['john', 'jane', 'doe']

uppercase_names = list(map(lambda x: x.upper(), names))

print(uppercase_names)

print('==========================Four============================')


countries = ['Afghanistan', 'Albania', 'Algeria', 'Iceland', 'Ireland']

land_countries = list(filter(lambda x: 'land' in x, countries))

print(land_countries)


print('==========================Five============================')

countries = ['Albania', 'Bahrain', 'India', 'Norway', 'Sweden']

six_char_countries = list(filter(lambda x: len(x) == 6, countries))

print(six_char_countries)


print('==========================Six============================')

countries = ['Albania', 'Bahrain', 'India', 'Norway', 'Sweden']

six_plus_char_countries = list(filter(lambda x: len(x) >= 6, countries))

print(six_plus_char_countries)


print('==========================Seven============================')

countries = ['Egypt', 'England', 'Eritrea', 'Ethiopia', 'France']

e_countries = list(filter(lambda x: x[0] == 'E', countries))

print(e_countries)


print('==========================Eight============================')

from functools import reduce

countries = [{'name': 'Denmark', 'population': 5729000, 'capital': 'Copenhagen'},
             {'name': 'Norway', 'population': 5368000, 'capital': 'Oslo'},
             {'name': 'Iceland', 'population': 341243, 'capital': 'Reykjavik'}]

result = reduce(lambda x, y: x + y['population'],
                filter(lambda x: x['name'][0] == 'I',
                       map(lambda x: x, countries)))
print(result)



print('==========================Nine============================')


def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

my_list = ['apple', 1, 'banana', 2, 'cherry', 3]
print(get_string_lists(my_list))



print('==========================Ten============================')

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

print('==========================Eleven============================')

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

result = reduce(lambda x, y: x + ', ' + y, countries) + ' are north European countries'

print(result)

print('==========================Twelve============================')

def categorize_countries(countries, pattern):
    return list(filter(lambda x: pattern in x, countries))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
land_countries = categorize_countries(countries, 'land')

print(land_countries)


print('==========================Thirteen============================')

from collections import defaultdict

def count_countries_by_letter(countries):
    result = defaultdict(int)
    for country in countries:
        first_letter = country[0]
        result[first_letter] += 1
    return dict(result)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
result = count_countries_by_letter(countries)

print(result)

print('==========================Foureen============================')

def get_first_ten_countries(countries):
    return countries[:10]

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Latvia', 'Lithuania', 'Russia', 'Poland', 'Germany']
first_ten_countries = get_first_ten_countries(countries)

print(first_ten_countries)

print('==========================Fifteen============================')

def get_last_ten_countries(countries):
    return countries[-10:]

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Latvia', 'Lithuania', 'Russia', 'Poland', 'Germany', 'France', 'Italy', 'Spain', 'United Kingdom', 'Greece', 'Portugal', 'Ireland', 'Netherlands']
last_ten_countries = get_last_ten_countries(countries)

print(last_ten_countries)































