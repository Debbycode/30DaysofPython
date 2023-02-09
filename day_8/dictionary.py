print('===================One==================')

dog = {}

print('===================Two==================')

dog = {'Name': 'Slego', 'Colour': 'White', 'Breed': 'German', 'legs': 'Four', 'age': '7'}
print(dog)

print('===================Three==================')

student = {'first Name': 'Mariam', 'Last Name': 'Adeoye', 'Gender': 'Female',
           'Age': '525', 'Marital Status': 'Married',
           'Skills': ['Python', 'Project Management, Microsoft Office Suite],
                      'Country': 'Nigeria', 'City': 'FCT Abuja',
                      'Address': '22, Somewhere in Abuja, Nigeria'}

print(student)
print('===================Four==================')

print(len(student))

print('===================Five==================')

print(student['skill'])

print(type(student['skills']))

print('===================Six==================')
           
other_skills = ('Microsoft Office Suite', 'Project Management')
student['skills'].append(other_skills)
print(student)

print('===================Seven==================')

print(student.keys())

print('===================Eight==================')

print(student.values())

print('===================Nine==================')

print(student.items())

print('===================Ten==================')

del student['address']
#student.popitem()
print(student)


print('===================Eleven==================')

del dog



