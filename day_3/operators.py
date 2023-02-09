print("===================one===================")
age = 100
print(f"I am {age} years old.")

print("===================Two===================")

height = 165.5
print(f"My height is height = {height}cm.")

print("===================Three===================")

complex_num = 3+5j
#print(f"{complex_num} is a complex number.")
print(f"complex_num = {complex_num} is a complex number.")

print("===================Four===================")

base_input = int(input("please enter the triangle base: "))
height_input = int(input("please enter the triangle height: "))

area_triangle = 0.5 * base_input * height_input

print(f"The area of a triangle of base: {base_input}m and height: {height_input}m is {area_triangle}m^2")

print("===================Five===================")

side_a = int(input("please enter value or side a: "))
side_b = int(input("please enter value or side b: "))
side_c = int(input("please enter value or side c: "))
 
perimeter_triangle = side_a + side_b + side_c

print(f"The perimeter of a triangle of side a: {side_a}m, side b: {side_b}m and side c: {side_c} is {perimeter_triangle}m")

print("===================Six===================")

lenght_rect = int(input("Please enter lenght value: "))
width_rect = int(input("Please enter width value: "))

area = lenght_rect * width_rect
perimeter = 2 * (lenght_rect + width_rect)

print(f"The area and perimeter of rectangle with lenght: {lenght_rect}m and width: {width_rect}m is {area}m^2, {perimeter}m.")

print("===================Seven===================")

pi = 3.14
radius = float(input("Please enter radius value: "))

area_circle = pi* radius **2
perimeter_circle = 2 * pi * radius

print(f"The area and perimeter of a circle with radius: {radius}m is {area_circle}m^2, {perimeter_circle}m")

print("===================Eight===================")

#x1, x2, y1,y2 = map(int, input("Please enter the cordinates of the equation: ").split())

#m  = (y2-y1)/(x2-x1)
#y = y2
#x = x1
#c =  y-(m*x)
#y = 2*x - 2
slope1 =2
print(f"the slope is: {slope1}")
#x-intercept
y = 0
c= -2
m= 2
x = (y-c)/m
print( f"The x-intercept for equation{y} is {x}")

#y-intercept
x = 0
y = (m*x)+c

print( f"The y-intercept for equation{y} is {y}")

print("===================Nine===================")

x1= 2
x2 =6
y1 =2
y2 =10

slope2 = (y2-y1)/(x2-x1)

Euc_distance = ((y1-x1)**2+(y2-x2)**2)**0.5

print(f"The slope and the Euclidean distance between two points are: {slope2}, {Euc_distance}")

print("===================Ten===================")

print(f"Is the first slope greater and equals to slope2?:, {slope1>=slope2}")

print("===================Eleven===================")
y= x**2 + 6*x + 9

x = int(input("please kindly input a value: "))
print(f"if x ={x}, y= x**2 + 6*x + 9 is equal to {y}")

print("===================Twelve===================")

print(f"Python not equal to dragon {len('python')!=len('dragon')}")

print("===================Thirtheen===================")

print (("on" in "python") and ("on" in "dragon"))

print("===================Fourteen===================")
        
sentence = "I hope this course is not full of jargon"

check =( "jargon" in sentence)
print(check)

print("===================fiveteen===================")

print("on" in "dragon"and "python")

print("===================Sixteen===================")

len("python")
print(str(float(len("python"))))

print("===================Seventeen===================")
        
input_num = int(input("please input a random to check if its even number or not: "))
if (input_num%2)==0:
        print("This is a even number")
else:
    print("This is odd!")

print("===================Eighteen===================")

floor_division = 7//2
converted = int(2.7)

if (7//2) == int(2.7):
        print("They are equal")
else:
    print("Not equal!")
    
print("===================Nineteen===================")           

check_dtype1 = type("10")
check_dtype2 = type(10)

if check_dtype1 == check_dtype2:
    print("They are equal data type")
else:
    print("Not at all")

print("===================Twenty===================")

float_int = int(9.8)
int_num = 10

if float_int == int_num:
    print("They are equal data number!")
else:
    print("They are not similar")

print("===================Twenty One===================")

hours = int(input("Please enter a hours: "))
rate_per_hour = int(input("Please enter rate by hour: "))

payment = hours * rate_per_hour

print(f"Your weekly earning for {hours}hours at a rate of {rate_per_hour} per hour is {payment}dollars")


print("===================Twenty Two===================")

years = int(input("kindly enter the number of years: "))

if (years <= 100):
      lifespan_seconds = years * 3153600000
      print(f"You have lived for {lifespan_seconds} seconds.")

else:
    print("Exceeded lifespan")

print("===================Twenty Three===================")

print("1",1**0,1**1,1**2,1**3)
print("2",2**0,2**1,2**2,2**3)
print("3",3**0,3**1,3**2,3**3)
print("4",4**0,4**1,4**2,4**3)
print("5",5**0,5**1,5**2,5**3)
    









