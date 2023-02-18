print('============================One=======================')

def count_text_line (txt_file):
    with  open(txt_file, 'r') as file:
        lines = len(file.readlines())
        print('Total number of lines:' , lines)

def count_text_words (txt_file):
    with  open(txt_file, 'r') as file:
        words = file.read().split()
        print(type(words))
        print('Total number of words is:', words)

#Driver code

#a)
txt_file = 'obama_speech.txt'

#b)
txt_file = 'michelle_obama_speech.txt'

#c)
txt_file = 'donald_obama_speech.txt'

#d)
txt_file = 'melina_trump_speech.txt'


print('============================Two=========================')

def most_spoken_languages (filename,n):
    with open(filename) as f:
        data = json.load(f)


    languages = {}

    for countries in data:
        for language in country['languages']:
            if language in languages:
                languages[language] += country['population']

            else:
                languages[language] = country['population']
    most_spoken_languages = sorted(languages.items(), key=lambda x:x[1], reverse=True)[:n]

    return [language[0] for language in most_spoken_languages]

                


print(most_spoken_languages(filename='./data/countries_data.json', n=10))



print('============================Three=========================')

def most_populated_countries (filename,n):
    with open(filename) as f:
        data = json.load(f)


    countries = []

    for countries_data in data:
        name = country_data['name']
        population = country_data['population']
        countries.append((name,population))

    sorted_countries = sorted(countries, key=lambda x: x[1], reverse = True)
    top_countries = [country[0] for country in sorted_countries[:n]]

    return top_countries


print(most_populated_countries(filename='./data/countries_data.json', n=10))





      


      






    
    
