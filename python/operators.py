x = 10
y =3
print(x + y) # addition : 13
print(x - y) # subtraction : 7
print(x * y) # multiplication : 30
print(x / y) # division :3.3
print(x//y) # floor division (integer division: 3)
print(x %y) # modulus(remainder) :1
print(x ** y) #exponentiation (x to the power of y) : 1000

# comparison operators 
x = 10 
y = 20 
print(x == y) #equal to :False 
print(x != y) #equal to :True
print(x > y) #greater than :False 
print(x < y) # less than :True 
print(x >= y) #greater than or equal to :False
print(x <= y) #less than or equl to: True 

# logical operators 
x = True
y = False 
print(x and y)
print(x or y)
print(not x)

# assignment operators 
x = 5 # simple assignment 
x += 3
x -= 2
x *= 5
x /=3
x //=2
x %=3
x **=2 


# bitwise operatosrs 
x = 10 
y = 4

print(x & y)
print(x | y)


# membership operators 
fruits = ["apple", "banana", 'cherry']
print("banana" in fruits)
print("orange" not in fruits)


x = 10
y = 10
z = [1,3,4]

print(x is y)
print(x is not z)

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)

n = 10
if n > 5:
    print(n)
    
# with walrus operator 
    
if (n := 10 ) > 5:
    print(n)
    
    
result = 10 + 2 * 3 ** 2
print(result)

result = (10 + 2) * 3 ** 2 
print(result)


