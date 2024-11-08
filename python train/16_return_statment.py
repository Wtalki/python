# return statement in python 
def add(a,b):
    return a + b
result = add(3,5)
print(result)

# returning multiple value 
def get_person_info():
    name = "alice"
    age = 24
    city = "new york"
    return name ,age ,city

info = get_person_info()
print(info)
name,age,city = info
print(name,age,city)

# returning differnet types of vlaues 
def get_even_numbers(limit):
    even_numbers = [num for num in range(limit) if num % 2 == 0]
    return even_numbers
print(get_even_numbers(10))

def create_user_porfile(name,age):
    return {"name":name,"age":age}
user_profile = create_user_porfile("alice,30",30)
print(user_profile)

# returning none 
def say_hello():
    print("hello")
result = say_hello()
print(result)


def check_positive(number):
    if number <= 0:
        return
    print(f"{number} is a positive number")
# check_positive(-1)
check_positive(3)

# returning conditional values 
def absolut_value(number):
    if number < 0:
        return -number
    return number

print(absolut_value(-5))
print(absolut_value(5))


# return n recursive functions 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)
print(factorial(5))

# returning lambda functions 
def multiplier(n):
    return lambda x:x*n
double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(5))

# examples using return statements ?

def cehck_even_odd(number):
    if number % 2 == 0:
        return "even"
    return "odd"

print(cehck_even_odd(4))
print(cehck_even_odd(3))


import math
def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 *math.pi * radius 
    return area, circumference
area, circumference = circle_properties(5)
print(area,circumference)


def contains_number(numbers,target):
    for num in numbers:
        if num == target:
            return True
    return False
print(contains_number([1,2,3,4,],3))
print(contains_number([1,2,3,4,],5))
     