#Set
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('====================One========================')
""
age_set = set(age)

print('Age list converted to Set: ', age_set)

print(len(age))
print(len(age_set))
print(f'Length of age list {len(age)} is bigger than its set {len(age_set)}')

print('====================Two========================')

print('''String are any text enclosed in a single, double ot triple quotes. Examples of strings: '123', 'word', 'a long sentence' etc.''')

print('''List is ordered and mutable data type that holds a different data in a square bracket. Example of list: [2, 6.8, 2, 'String', False, 6.8]''')

print('''Tuple is ordered unchangable data structure that contains related data or pair of data enclosed in  a bracket(). Example of tuple: (length, breadth, height).''')

print('''Set are unorderd,unchangeable and unindexed data structure that holds unique values enclosed in a curly bracket. Example of set: {65, 21, 34,10}''')


print('====================Three========================')

sentence = 'I am a teacher and I love to inspire and teach people.'

get_unique_word = set (sentence.split())
print('Unique words: ', get_unique_word)

print('The number of unique of words is: ', len(get_unique_word))tuple

