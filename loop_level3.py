print('=====================One=======================')
from country import countries

def filter_country(country):
    if "land" not in country:
        return True
    return False

country_no_land = filter(filter_country,countries)
print(list(country_no_land))


print('=====================Two=======================')

fruit = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruit)-1,-1,-1):
    print(fruit[i])


print('=====================Three========================')

from countries_data import data

lang = {}

for language in languages:
    if language in lang:
        lang[language]+=1
    else:
        lang[language] =1
print(lang)

sorted_lang = sorted(lang.items(), key = lambda x:x[1], reverse=True)
print(sorted_lang)

for i in range(10):
    print(sorted_lang[i])
sorted_lang[:10]
