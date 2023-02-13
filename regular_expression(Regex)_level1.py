print('====================One===================')

import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\w+', paragraph)
word_frequency = Counter(words)

most_frequent_word = word_frequency.most_common(1)[0][0]
print("The most frequent word is:", most_frequent_word)

print('====================Two===================')

import re

text = "-12, -4, -3 and -1 in the negative direction, 0 at origin,4 and 8 in the positive direction."

numbers = re.findall(r"-?\d+", text)
numbers = [int(x) for x in numbers]

print(numbers)
# Output: [-12, -4, -3, -1, 0, 4, 8]


