print('=========================One=====================')

def filter_negative_and_zero(input_list):
    filtered_list = [num for num in input_list if num <= 0]
    return filtered_list

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_negative_and_zero(numbers)


print('=========================Two=====================')

def flatten_list(input_list):
    flat_list = [item for sublist in input_list for subsublist in sublist for item in subsublist]
    return flat_list

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list(list_of_lists)


print('=========================Three=====================')

def create_tuple_list(n):
    tuple_list = [(i, i**2) for i in range(n)]
    return tuple_list


create_tuple_list(7)


print('=========================Four=====================')

def flatten_list(input_list):
    flat_list = [item for sublist in input_list for item in sublist]
    return flat_list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_list(countries)


print('=========================Five=====================')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [{'country': country.upper(), 'city': city.upper()} for [country, city] in countries]

print(result)

print('=========================Six=====================')

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')]]

result = [" ".join(name) for [name] in names]

print(result)


print('=========================Seven=====================')

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)



