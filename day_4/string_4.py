print("=================One=================")

string = "Thirty", "Days", "Daya", "of"
ssingle_string = "Thrity days of Python"

Sentence = "Thirty" + ' ' + "Days" + ' ' + "Of" + ' ' + "Python" +  ' ' + "Thirty days of Python"

print(Sentence)


print("=================Two=================")

string = "Coding" + ' ' + "For" + ' ' + "All" + ' ' + "Coding For All"

print(string)


print("=================Three=================")

company = "Coding For All"


print("=================Four=================")

print(company)


print("=================Five=================")

print(len(company))

print("=================Six=================")

print (company.upper())


print("=================Seven=================")

print (company.lower())

print("=================Eight=================")

print(company.capitalize())
print(company.title())
print(company.swapcase())

print("=================Nine=================")

print(company[:5])

print("=================Ten=================")

print(company.find('Coding'))

print("=================Eleven=================")

print(company.replace('Coding', 'Python'))

print("=================Twelve=================")

print(company.replace('Python for Everyone', 'Python for All'))


print("=================Thirteen=================")

print(company.split())

print("=================Fourteen=================")

social_media = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(social_media.split(','))


print("=================Fifteen=================")

print(company[0])


print("=================Sixteen=================")

print(company[-1])

print("=================Seventeen=================")

print(company[10])

print("=================Eigteen===================")

word = 'Python For Everyone'
pfe = word[0:20:11] 
print(pfe)


print("=================Nineteen===================")

cfa = company[0:20:11] 
print(cfa)

print("=================Twenty===================")

print(company.find('c'))

print("=================Twenty One===================")

print(company.find('F'))

print("=================Twenty Two===================")

print(company.rfind('l'))


print("=================Twenty Three===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(sentence.index(sub_string))


print("=================Twenty Four===================")

statement = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(statement.rindex(sub_string))

print("=================Twenty Five===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'
print(sentence[31:54])

print("=================Twenty Six===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
print(sentence.find(word))

print("=================Twenty Seven===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'
print(sentence[31:54])

print("=================Twenty Eight===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.startswith("Coding"))


print("=================Twenty Nine===================")

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.endswith("Coding"))

print("=================Thirty===================")

sentence = '   Coding For All      ' 
print(sentence.endswith("Coding"))

print("=================Thirty One===================")

variable1 = '30DaysOfPython' 
print(variable1.isidentifier())

variable2 = 'thirty_days_of_python'
print(variable2.isidentifier())

print("=================Thirty Two===================")

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
updated_list = ' #'.join(python_libraries)
print(updated_list)                       

print("=================Thirty Three===================")

sentence = 'I am enjoying this challenge.I just wonder what is next.'                    
print('I am enjoying this challenge.\nI just wonder what is next.')

print("=================Thirty Four==================")

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')                       
                       
print("=================Thirty Five==================")

radius = 10
area = 3.14 * radius ** 2

print('The area of a circle with radius {} is {:.2f} meters square'.format(radius, area))


print("=================Thirty Six==================")
x = 8
y = 6
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')
print(f'{x} % {y} = {x%y}')
print(f'{x} // {y} = {x//y}')
print(f'{x} ** {y} = {x**y}')      


      
