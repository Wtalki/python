def greet():
    print("hello, world")
greet()

# function parameters 
def greet(name):
    print(f"hello,{name}")
greet("hello")

# default parameters 
def greet(name = "guest"):
    print(f"hello, {name}")
greet() #output default parameters
greet("zaw lay")

#return statement
def square(x):
    return x * x 
result = square(4)
print(result)

def divide_and_remainder(x,y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

result = divide_and_remainder(10,3)
print(result)
quotient, remainder = result
print(quotient, remainder)

# variable scope 
def local_example():
    x = 10
    print(x)

local_example()

# global virable eample 
y = 20
def global_example():
    print(y)
global_example()

#  *args and **kwargs 
def print_all(*args):
    for arg in args:
        print(arg)
print_all("apple","banana","cherry")


# using **kwargs 
def print_key_values(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_key_values(name = "alice", age = 23, city = "new york")


# lambda functions 
square = lambda x:x * x
print(square(5))

# using lambda with map 
numbers = [1,2,3,4]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# example: bulding a calculator function 
def calculator(a,b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a/ b if b !=0 else "cannot divide by zero"
    else:
        return "invalid operation"
print(calculator(3,3,"+"))
print(calculator(5,3,"-"))
        