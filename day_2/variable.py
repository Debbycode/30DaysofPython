# Day 2: 30 Days of python programming

print ("===================LEVEL 1===========================")

# Declaring Variables in Python

first_name = 'Deborah'
print("First name: ", first_name)
last_name = 'Ajah'
print("Last name: ", last_name)
full_name = 'Deborah Ajah'
print("Full name: ", full_name)
country = 'Nigeria'
print("Country: ", country)
city = 'Federal Capital Territory'
print("City: ", city)
age = '969'
print("Age: ", age)
year = '199X'
print("year: ", year)
is_married = 'engaged'
print("marital Status: ", is_married)
is_true = 'No'
print("married?: ", is_true)
is_light = 'False'
print("Are you light complexion? ", is_light)
hobbies = ['reseach', 'reading', 'coding', 'sports', 'music']
print("Hobbies are: ", hobbies)


print ("===================LEVEL 2===========================")
       

#1. Checking data type of variables

print("First name data type: ", type(first_name))
print("Last name data type: ", type(last_name))
print("Full_name data type: ", type(full_name))
print("Country data type: ", type(country))
print("City data type: ", type(city))
print("Age data type: ", type(age))
print("Year data type: ", type(year))
print("is_married data type: ", type(is_married))
print("is_true data type: ", type(is_true))
print("is_light data type: ", type(is_light))
print("Hobbies data type: ", type(hobbies))

#2. Printing the length of  first name

print('First name length:', len(first_name))

#3. Comparing lenght of first name and last name


print("Is the length of firt name equal to the lenght of last name?:", len(first_name) == len(last_name))

#4. Declaring multiple variables in one line

num_one = 5
num_two = 4

#i. 
total = num_one + num_two
print(f"{num_one} + {num_two} = {total}")

#ii.
diff = num_one - num_two
print(f"{num_one} - {num_two} = {diff}")

#iii.
product = num_two * num_one
print(f"{num_two} * {num_one} = {product}")
      
#iv.
division = num_one/num_two
print(f"{num_one} / {num_two} = {division}")
      
#v.
remainder = num_two % num_one
print(f"{num_two} % {num_one} = {remainder}")
      
#vi.
exp = num_one**num_two
print(f"{num_one} ** {num_two} = {exp}")
      
#vii.
floor_division = num_one//num_two
print(f"{num_one} // {num_two} = {floor_division}")

#5. Calculating the area and circumference of a Circle

pie = 3.142
r = 30

#i.

area_of_circle = pie * r**2
print(f"The area of a circle is {area_of_circle}")

#ii.
circum_of_circle = 2 * pie * r
print(f"The circumference of a circle is {circum_of_circle}")

#iii.
radius = int(input("Please enter the radius your cicle: "))

area_of_circle2 = pie * radius**2
print(f"Thank you!. The area of your circle with {radius} is {area_of_circle}")

#6.
user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")
user_country = input("Please which country are from? ")
user_age = input("Kindly let us know how old you are? ")

print("Your first name is: ",user_first_name)
print("Your last name is: ",user_last_name)
print("Your nationality is: ",user_country)
print(f"You entered {user_age}. You are {user_age} years old!")

print(f"Thank you!. Your name is {user_first_name} {user_last_name}, and you are {user_age} years old!") 
   

#7.
help('keywords')





