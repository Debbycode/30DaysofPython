print('=====================One==================')

import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return (shuffled_list)

lst = ['bread', 'eggs', 'sardine', 'vegetble']
print(shuffle_list(lst))


print('=====================Two==================')

import random

def random_unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(random_unique_numbers())
