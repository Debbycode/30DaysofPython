# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print('================One====================')

print(len(it_companies))

print('================Two====================')

new_company = 'Twitter'

it_companies.add(new_company)

print(it_companies)

print('================Three====================')

other_it_companies = {'Linkedin', 'Youtube', 'Salesforce'}

it_companies.update(other_it_companies)

print(it_companies)


print('================Four====================')

it_companies.remove('Youtube')

print(it_companies)

print('================Five====================')


it_companies.remove('Facebook')

print(it_companies)


it_companies.discard('Youtube')

print(it_companies) #dicard and remove methods performs the same function of ermoving element in a set

