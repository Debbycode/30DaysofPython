print('========================Four========================')

import re

with open('email_exchange_big.txt', 'r') as file:
    contents = file.read().splitlines()
    email_addresses = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', contents)

print(email_addresses)


print('========================Five========================')

import re
from collections import Counter

def find_most_common_words(input_text, num_words):
    # read input text from file, if given
    if input_text.endswith('.txt'):
        with open(input_text, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = input_text
    
    # split text into words and remove non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())
    
    # count word frequencies and return top num_words most common words
    word_counts = Counter(words)
    return word_counts.most_common(num_words)

print(find_most_common_words('sample.txt', 5))


print('========================Six========================')

import re
from collections import Counter

def find_most_common_words(input_file, num_words=10):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # split text into words and remove non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())

    # count word frequencies and return top num_words most common words
    word_counts = Counter(words)
    return word_counts.most_common(num_words)


# Obama's speech
obama_most_common = find_most_common_words('obama.txt', 10)
print('Obama:', obama_most_common)

# Michelle's speech
michelle_most_common = find_most_common_words('michelle.txt', 10)
print('Michelle:', michelle_most_common)

# Trump's speech
trump_most_common = find_most_common_words('trump.txt', 10)
print('Trump:', trump_most_common)

# Melania's speech
melania_most_common = find_most_common_words('melania.txt', 10)
print('Melania:', melania_most_common)


print('========================Seven========================')

import re
import string
from collections import Counter

# load stop words from file
def load_stop_words(file_path):
    with open(file_path, 'r') as f:
        stop_words = [line.strip() for line in f]
    return stop_words

# clean text by removing punctuation and converting to lowercase
def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text

# remove stop words from text
def remove_stop_words(text, stop_words):
    words = re.findall(r'\b\w+\b', text)
    return ' '.join([word for word in words if word not in stop_words])

# compute similarity between two texts using cosine similarity
def check_text_similarity(text1, text2):
    # convert text to bag-of-words representation
    text1_words = re.findall(r'\b\w+\b', text1)
    text2_words = re.findall(r'\b\w+\b', text2)
    text1_word_counts = Counter(text1_words)
    text2_word_counts = Counter(text2_words)

    # compute dot product
    dot_product = 0
    for word, count in text1_word_counts.items():
        if word in text2_word_counts:
            dot_product += count * text2_word_counts[word]

    # compute magnitudes
    text1_mag = sum(count ** 2 for count in text1_word_counts.values()) ** 0.5
    text2_mag = sum(count ** 2 for count in text2_word_counts.values()) ** 0.5

    # compute cosine similarity
    if text1_mag != 0 and text2_mag != 0:
        cosine_similarity = dot_product / (text1_mag * text2_mag)
    else:
        cosine_similarity = 0.0

    return cosine_similarity

# main program
if __name__ == '__main__':
    # load stop words
    stop_words = load_stop_words('data/stopwords.txt')

    # read Michelle's speech
    with open('data/michelle.txt', 'r', encoding='utf-8') as f:
        michelle_text = f.read()

    # read Melania's speech
    with open('data/melania.txt', 'r', encoding='utf-8') as f:
        melania_text = f.read()

    # clean and remove stop words from text
    michelle_cleaned = remove_stop_words(clean_text(michelle_text), stop_words)
    melania_cleaned = remove_stop_words(clean_text(melania_text), stop_words)

    # compute similarity between texts
    similarity = check_text_similarity(michelle_cleaned, melania_cleaned)

    # print result
    print('Similarity between Michelle and Melania:', similarity)


print('========================Eight========================')


import re
from collections import Counter

# read file and count word occurrences
with open('romeo_and_juliet.txt', 'r') as f:
    text = f.read()
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)

# print the 10 most repeated words
for word, count in word_counts.most_common(10):
    print(word, count)


print('========================Nine========================')  

import csv

# define keywords to search for
python_keywords = ['python', 'Python']
javascript_keywords = ['javascript', 'Javascript', 'JavaScript']
java_keywords = ['java']

# initialize line counts
python_count = 0
javascript_count = 0
java_not_javascript_count = 0

# read file and count lines containing keywords
with open('hacker_news.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # check for Python keywords
        if any(keyword in row[1] for keyword in python_keywords):
            python_count += 1
        # check for JavaScript keywords
        if any(keyword in row[1] for keyword in javascript_keywords):
            javascript_count += 1
        # check for Java but not JavaScript
        if all(keyword in row[1] for keyword in java_keywords) and not any(keyword in row[1] for keyword in javascript_keywords):
            java_not_javascript_count += 1

# print the results
print(f"Number of lines containing 'python' or 'Python': {python_count}")
print(f"Number of lines containing 'javascript', 'Javascript', or 'JavaScript': {javascript_count}")
print(f"Number of lines containing 'java' but not 'javascript': {java_not_javascript_count}")
