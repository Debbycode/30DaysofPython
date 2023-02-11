print('===========================One=======================')

import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id

print(random_user_id())


print('===========================Two=======================')

def user_id_gen_by_user():
    
    import random
    import string
  
    num_of_chars = int(input("Enter the number of characters in the user ID: "))
    num_of_id = int(input("Enter the number of IDs to be generated: "))
  
    user_id = []
    for i in range(num_of_id):
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))
        user_id.append(id)
  
    return user_id

print(user_id_gen_by_user())

print('===========================Three=======================')

def rgb_color_gen():
    import random

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    print(f'rgb({red},{green},{blue})')


rgb_color_gen()





