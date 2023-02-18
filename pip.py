print('============================One================================')

import requests
import re
from collections import Counter

# retrieve text from URL
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text

# count word occurrences
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)

# print the 10 most frequent words
for word, count in word_counts.most_common(10):
    print(word, count)


print('===========================Two==============================')


import requests
import numpy as np
from collections import Counter

# retrieve cat breed data from API
response = requests.get('https://api.thecatapi.com/v1/breeds')
data = response.json()

# extract weight and lifespan data
weights = []
lifespans = []
for breed in data:
    if breed['weight']['metric']:
        weight = float(breed['weight']['metric'].split()[0])
        weights.append(weight)
    if breed['life_span']:
        lifespan = float(breed['life_span'].split()[0])
        lifespans.append(lifespan)

# calculate statistics on weight and lifespan
weight_min = min(weights)
weight_max = max(weights)
weight_mean = np.mean(weights)
weight_median = np.median(weights)
weight_std = np.std(weights)

lifespan_min = min(lifespans)
lifespan_max = max(lifespans)
lifespan_mean = np.mean(lifespans)
lifespan_median = np.median(lifespans)
lifespan_std = np.std(lifespans)

# create frequency table of country and breed
country_breed_counts = Counter()
for breed in data:
    if breed['origin']:
        country = breed['origin'].strip().lower()
    else:
        country = 'unknown'
    breed_name = breed['name'].strip().lower()
    country_breed_counts[(country, breed_name)] += 1

# print the results
print("Weight statistics:")
print(f"  Min: {weight_min:.2f} kg")
print(f"  Max: {weight_max:.2f} kg")
print(f"  Mean: {weight_mean:.2f} kg")
print(f"  Median: {weight_median:.2f} kg")
print(f"  Standard deviation: {weight_std:.2f} kg")

print("Lifespan statistics:")
print(f"  Min: {lifespan_min:.1f} years")
print(f"  Max: {lifespan_max:.1f} years")
print(f"  Mean: {lifespan_mean:.1f} years")
print(f"  Median: {lifespan_median:.1f} years")
print(f"  Standard deviation: {lifespan_std:.1f} years")

print("Country/breed frequency table:")
for (country, breed), count in country_breed_counts.most_common():
    print(f"  {country.capitalize()}: {breed.capitalize()} - {count}")




print('======================Four=========================')


import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
data = response.json()

# sort countries by descending order of area and get the top 10
largest_countries = sorted(data, key=lambda x: x['area'], reverse=True)[:10]

# print the names of the largest countries
for country in largest_countries:
    print(country['name'])




import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
data = response.json()

languages = {}

# count the number of countries that speak each language
for country in data:
    for language in country['languages']:
        if language['name'] in languages:
            languages[language['name']] += 1
        else:
            languages[language['name']] = 1

# sort languages by descending order of number of countries and get the top 10
most_spoken_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]

# print the names of the most spoken languages
for language, count in most_spoken_languages:
    print(language)



import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
data = response.json()

languages = set()

# add all unique language names to the set
for country in data:
    for language in country['languages']:
        languages.add(language['name'])

# print the number of languages
print(len(languages))


print('======================Four=========================')


import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

datasets_table = soup.find_all('table')[5]

for row in datasets_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    dataset_name = columns[0].text.strip()
    dataset_url = "https://archive.ics.uci.edu/ml/" + columns[0].find('a')['href']
    print(dataset_name, dataset_url)




