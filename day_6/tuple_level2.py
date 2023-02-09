print('=================one===============')

family_members = ('Idara', 'Joy', 'Afusa', 'Azeez', 'Oluwaseun', 'Oboh', 'Mojisola')
first_sibling, second_sibling, third_sibling, forth_sibling, fifth_sibling, *rest = family_members

print(first_sibling)
print(second_sibling)
print(third_sibling)
print(forth_sibling)
print(fifth_sibling)
print(*rest)

print('=================Two===============')

fruits = ('Agbalumo', 'Orange', 'Mango')
vegetables = ('ugwu', 'Waterleaf', 'Utazi')
animal_products = ('ponmo', 'chicken', 'beef')

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

print('=================Three===============')

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

print('=================Four===============')

some_food = food_stuff_tp[1:5]

print(some_food)

print('=================Five===============')

first_three_food = food_stuff_lt[:3]

print(first_three_food)

print('=================Six===============')

del food_stuff_tp

print('=================Seven===============')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in  nordic_countries)

print('Iceland' in  nordic_countries)


