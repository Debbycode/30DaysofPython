print('=================One================')
empty_list = []
print(empty_list)


print('=================Two================')
list_item = ['Nigeria','213.4', 'Democratic',['Christainity','Islam', 'Traditional'], 'Africa']


print('=================Three================')

print(len(list_item))


print('=================Four================')

print(list_item[0])
print(list_item[3])
print(list_item[2])


print('=================Five=================')

mixed_data_types = ['Deborah', '', '165', 'engaged', 'FCT Abuja']

print(mixed_data_types)



print('=================Six=================')


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

fb, ggle, mcft, aple, ibm, orcle, azn = it_companies



print('=================Seven================')

print(fb)
print(ggle)
print(mcft)
print(aple)
print(ibm)
print(orcle)
print(azn)


print('=================Eight=================')

print('Number of Companies: ', len(it_companies))


print('=================Nine=================')

print('First IT Company: ', it_companies[0])
print('Middle IT Company: ', it_companies[3])
print('Last IT Company: ', it_companies[-1])

print('=================Ten=================')

it_companies[0] = 'SalesForce'
print('Updated IT Company List: ', it_companies)

print('=================Eleven=================')

it_companies.append('Petals Consult')
print('Additional IT Company: ', it_companies)

print('=================Twelve=================')

it_companies.insert(3,'Accenture')
print(it_companies)

print('=================Thirteen=================')

print(it_companies[3].upper())


print('=================Fourteen==================')

print(' #'.join(it_companies))

print('=================Fifteen==================')

does_exist = 'Salesforce' in it_companies
print(does_exist)

print('=================Sixteen==================')

print(it_companies.sort())

print('=================Seventeen=================')

reverse_list = it_companies.reverse()

print(reverse_list)

print('=================Eighteen==================')

print(it_companies[:3])

print('=================Nineteen==================')

print(it_companies[-3:])

print('=================Twenty==================')

print(it_companies[1:4])

print('=================Twenty One==================')

it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.remove('Facebook')
print(it_companies)

print('=================Twenty Two==================')

it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.remove('Apple')
print(it_companies)

print('=================Twenty Three==================')

it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.remove('Amazon')
print(it_companies)

print('=================Twenty Four==================')
it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

print('=================Twenty Five==================')

del it_companies


print('=================Twenty Six==================')

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

frameworks = front_end + back_end

print(frameworks)

print('=================Twenty Seven==================')

full_stack = frameworks.copy()

additions = ['Python', 'SQL']
full_stack.e(4, additions)

print(full_stack)


















