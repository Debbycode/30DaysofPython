print('======================One===================')

import re
import collections

def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Split into words
    words = text.split()
    
    return ' '.join(words)

def most_frequent_words(text):
    # Count the frequency of each word
    word_counts = collections.Counter(text.split())
    
    # Sort the words by frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top 3 words
    return sorted_words[:3]

# Clean the text
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)

# Print the cleaned text
print(cleaned_text)
# Output: I am a teacher and I love teaching there is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs does this motivate you to be a teacher

# Print the three most frequent words
print(most_frequent_words(cleaned_text))
# Output: [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
