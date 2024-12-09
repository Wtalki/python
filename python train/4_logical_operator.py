# x  =10
# y =20
# if x > 5 and y > 15:
#     print("both conditions are true")

# # both conditions x > 5 and y > 15 are ture , so the code inside the block prints


# x = 10
# y = 5

# if x > 10 and y > 15:
#     print("both conditions are true")
# else:
#     print("at lease one condiiton is false")
#     # since y > 15 is false the entire condition evaluates to false triggering the condition
    
# # or operator

# x = 10
# y = 20
# if x > 5 or y < 15:
#     print("at least one condition is true")
#     # since x > 5 is true the entire condition evaluates to true triggering the condition

# # when or returns false 

# x = 3
# y =2 
# if x > 5 or y > 10:
#     print("at least one condition is true")
# else:
#     print("both conditions are false")
#     # BOTH CONDITION ARE FALSE SO THE EXPRESSIN EVALUATES TO FALSE

# # 3 nto operator 

# is_reading = True
# if not is_reading:
#     print("it is not reading")
# else:
#     print("it is reading")
#     # NOT operator returns true when the operand is false, so this condition evaluates to true

# #using not with comparisons

# x = 10 
# if not (x < 5):
#     print("x is not less than 5")
#     # the conditions x < 5 is false, and not reerse it to true so the statement is printed

# #combinig logical operators

# x = 10
# y = 5
# z = 3

# if (x> 5 and y < 10) or z > 2:
#     print("complex condition is ture  ")
# # the first part (x>5 and y<10) is true and the seconde part z > is also true sot the entire condition evaluates to true

# x = 10
# y =20
# if not(x < 5) and not (y > 25):
#     print("both conditions are false")
#     # x < 5 is false so no makes it true and y > 25 is false so not makdes it true hence, the condition is true
    
# # short-circuit evluation

# x = 10
# y =5
# if x > 5 and y > 10:
#     print("this will not print")
#     # the first condition x > 5 is true, so the second condition is not checked so will not print

# x = 10
# y = 5
# if x > 5 or y > 10:
#     print("this will print")

# age = 20
# is_student =False

# if age> 10 and not is_student:
#     print("you are an adult, but not a student")

# password = 'Zaw123456'

# if len(password) >=8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
#     print("password is valid")
# else:print("passwod is invalid")    
    

x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")

x = 10
y = 5
if x > 5 and y > 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")

x = 10
y = 20
if x > 5 or y < 15:
    print("At least one condition is true")

x = 10
y = 20
if x > 5 or y < 15:
    print("at least one condition is true")
    
x = 3
y = 2
if x > 5 or y > 10:
    print("At least one ondition is true")
else:
    print("Both conditions are false")

is_raining = True
if not is_raining:
    print("it is not raining")
else:
    print("it is raining")

x = 10
if not (x < 5):
    print("x is not less than 5")
    
x = 10
y = 5
z = 3

if (x > 5 and y < 10) or z > 2:
    print("complex condition is true")
    
x = 10
y = 20
if not (x < 5) and not (y > 25):
    print("Both conditions are false")
    
x = 10
y =5
if x > 5 and y > 10:
    print("this will not print")

x = 10 
y = 5
if x > 5 or y > 10:
    print("this will print")

age = 20 
is_student = False

if age > 18 and not is_student:
    print("you are an adult,but nto a student")

password = "myPassword123"
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("password is valid")
else:
    print("password is invalid")






    
    
    