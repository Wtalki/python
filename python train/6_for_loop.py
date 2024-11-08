# # for loop 
# for vaiable insequence:
#     code block to eecute 

# basic for loop example 
fruits = ["apple",'banaan','cherry']

for fruit in fruits:
    print(fruit)
    
# using for loop with range() function 
for i in range(5):
    print(i)

for i in range(2,10,2):
    print(i) # 2 is start 10 is stop 2 is 2rd number  

word = "hello"
for char in word:
    print(char) # for loop with strings 
    
# nested for loops

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item,end=" ") #print a newline after each row
    print()

# using else with for loop 
for i in range(3):
    print(i)
else:
    print("loop finished")

# example with break

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("loop finished")

person = {"name": "alice","age":30,"city":"new york"}

for key in person:
    print(key)
    
for key, value in person.items():
    print(key,":",value)
    
squares = [x**2 for x in range(5)]
print(squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)



#practical examples of for loops
numbers = [1,2,3,4,5]
total = 0
for num in numbers:
    total += num
    print("sum:", total)
    
sentence = "hello world"
char_count = 0
for char in sentence:
    if char == "l":
        char_count += 1

print(f"'0' appears {char_count} times")        
    
#flattening a nested list
nested_list = [[1,2],[3,4],[5,6]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
    