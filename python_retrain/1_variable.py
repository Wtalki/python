# creatin g variables 
name = "alice"
age = 25
height = 5.6 #float
is_student = True #boolean variable 

#variable naming rules 
first_name = "john"
_age = 30
height_in_meters = 1.34 #valid 

# data types of variables 
score = 95 #integer 
price = 12.34 #float 
message = "hello" #string 
is_active = False #boolean 


# 4 ressingning variables 
count = 10 
count = 20 
count += 5 
print(count)


# printing variables ?
name = "alice"
age = 25
print(name)
print("Age:", age)

# 6 combining variables 
first_name = "john"
last_name = "doe"
fullname = first_name + " " + last_name
print(fullname)

# 7 geting user input and storing in variables 
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# print("Hello", name, "you are", age, "years old")


# variable scope 
x = 10 
def my_function():
    y = 5
    print("inside function , x: ", x)
    print("inside function , y:", y)
my_function()
print("outside function,x:", x)

# constants convention 
