x  = 10
y = 3.14
name = "Alice" # string
is_student = False #Boolean 


print("Hello,Wrold")

print(x)
print("my neame is ", name) # prints multiple values separated by a space

if X > 5:
    print("x is greater than 5") #Indentation defines the block of code
else:
    print("x is less than or equal to 5")
    
    
# conditonal statements
if x > 10:
    print("x is greate than 10 ") #excutes if condition is true
elif x == 10:
    print ("x is equal to 10") #excutes if the first conditon is false
else:
    print("x is less than 10") #excutes if all conditions are false
    
    
for i in range(5):
    print(i)  #range(5) generates numbers 0 to 4
    
#while loop:repeats as long as the condition is true
count = 0
while count < 5:
    print(count)
    count +=1 #ncrement count by 1
    
    
# functions
def greet(name): #define a function with a parameter
    print("Hello,",name)
greet("Alice") #call the function with an argoument

fruits = ["apple","banana","cherry"] # create a list
print(fruits[0]) #access the first elelement: "apple"
fruits.append('oragne') #add an elem ent to the end
print(fruits) #output:['apple',banana','cherr','orange']

# dictionaries
person = {
    "name":"Alice", #key value pairs
    "age":25,
    "is_student":True
}

print(person["name"]) #access value using Key:"Alice"
person["age"] = 26 # Update value 
print(person) # output {"name":"Alice","age":26,"is_student":True}

# tuples 
coordinates = (10,20) #create a tuple
print(coordinates[0]) # access the first element:10
#tuples are immutable, so you cannot change their values 

# sets 
unique_numbers = {1,2,3,3,4} # create a set (duplicates are removed)
print(unique_numbers) # output : {1,2,3,4}

# input
name = input("Enter you name: ") # get user input 
print("Hello,",name) # get user input

age = 25 # get user age
print(age) # get user age

# importing Modules 
import math # Improt the math module
print(math.sqrt(16)) # use a function from the module:4.0

# error handling 
try:
    result = 10/ 0 #this will raise a zerodivisionError 
except ZeroDivisionError:
    print("Cannot Divide by zero") #handle the error 

# classes and objects 
class Dog: #define a class
    def __init__(self,name): #constructor method 
        self.name = name #instance variable 
    def bark(self): #method 
        print(f"{self.name} say woodf!")

my_dog = Dog("Buddy") #create an object 
my_dog.bark() #call a method: "Buddy says woof!"



# file handling 
#writing to a file 
with open("example.txt", "w") as file: #Open file in write mode 
    file.write("Hello, Wrold!") #write content to the file
    
# Reading from a file 
with open("example.txt", "r") as file #open file in read mode 
    content = file.read() #read content from the file
    print(content)
    
# list comprehensions 
squares = [x**2 for x in range(10)] #create a list of squares 
print(squares) # output: [0,1,4,9,16,25,36,49,64,81]


# lambda functions 
add = lambda x,y:x+y #define a lambda function 
print(add(5,3)) #output:8


# modules and packages 

#my_module.py
def greet(name):
    print(f"Hello, {name}")
    
#main.py
import my_module #Import the module
my_module.greet("Alice") #use a function from the module 

#slicing 
text = "Hello, Wrold"
print(text[0:5]) #Slice from index 0 to 4: "Hello, Wrold" 
print(text[7:]) #slice from index 7 to the end: "World!" 


#string methods 
text = "Python programmming"  
print(text.strip()) # remove leading/trailing spaces: "python programming"
print(text.lower()) #convert to lowercase: "python programming"


# list methods 
fruits = ["apple", "banana"]
fruits.append("cherry") # add to the end
fruits.remove("banana") # remove an element 
print(fruits) # output:['appple','cherry']

# dicitionary methods 
person = {"name":"Alice","age":25}
print(person.keys()) #output: dict_keys(['name','age'])
print(person.get("name")) #output:alice 

# tuple unpacking 
coordinates = (10,20)
x,y = coordinates # unpack into varables 
print(x,y)