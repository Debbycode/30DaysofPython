import json
from operator import itemgetter

# load countries data from countries_data.py
with open('countries_data.py') as f:
    countries_data = json.load(f)

# sort countries by name
sorted_countries_by_name = sorted(countries_data, key=itemgetter('name'))

# sort countries by capital
sorted_countries_by_capital = sorted(countries_data, key=itemgetter('capital'))

# sort countries by population
sorted_countries_by_population = sorted(countries_data, key=itemgetter('population'), reverse=True)

# sort out the ten most spoken languages by location
languages = []
for country in countries_data:
    for language in country['languages']:
        languages.append(language)

language_frequency = {}
for language in languages:
    if language in language_frequency:
        language_frequency[language] += 1
    else:
        language_frequency[language] = 1

sorted_languages = sorted(language_frequency.items(), key=itemgetter(1), reverse=True)
ten_most_spoken_languages = [language[0] for language in sorted_languages[:10]]
print(ten_most_spoken_languages)
 
# sort out the ten most populated countries
ten_most_populated_countries = sorted_countries_by_population[:10]
print(ten_most_populated_countries)
