# if statement
#if condition:
    # code block to be executed if condition is True
#elif another condition
    # code block to be executed if the first condition is False and this condition is True
#else:
    # code to execute if all previous conditions are false


x = 10
if x > 5:
    print("x is greater than 5")
# checks if x is greater than 5 if true, it excutes the print statement



#if else
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")
# checks if y is even: if not, it defaults to printing that y is odd


z =0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")
# checks if z is positive, negative, or zero , and prints accordingly 


# comparsion operators in if statements

a = 15
b =20

if a ==b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")
# comment: compares the values of a and b and prints base on the result.

#LOGICAL OPERATORS IN IF STATEMETS

age = 25
income = 50000
if age> 18 and income > 3000:
    print("eligible for the loan")

#checks if both age and income meet the conditions for eligiblility.

#using (or) operator

day = "saturday"
if day == "saturday" or day == "sunday":
    print("it's the weekend")
    # checks if the day is saturday or sundary . if either conditions is true it excutes the code.
    

is_member = False
if not is_member:
    print("you need to register") 
    # not reverses the condition, so it only prints if 'is_menber' is false
    
#nested if statements

temperature = 30
humidity = 70

if temperature > 25:
    if humidity > 60:
        print("it's hot and humid")
    else:
        print("it;s hot but not too humid")
    # checks if it's hot, then futher checks humidity levler


# if with dictionary keys
person = {"name":"Alice","age":30}

if "name" in person:
    print("name is available")
    #checks if 'name key exitst in the dictionary person
    
    
#ternary if statements (conditional expressions)

number = 4
result = "Even" if number % 2 == 0 else f"{number}"
print(result)
# sets 'result' to even if the number is even, otherwise to odd

name = ""
if not name:
    print("name is empty")
    
marks = 25

if marks >= 90:
    grade = "a"
elif marks >= 80:
    grade = "b"
elif marks >= 70:
    grade = "c"
else:
    grade = "f"
print("grade:", grade)
    



