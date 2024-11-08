text = "python"
print(text[0])
print(text[3])
print(text[-1])
print(text[-2])


#indexing with lists 
fruits = ["apple","banana","cherry","date"]
print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-3])

#indexing with tuples
numbers = (10,20,30,40,50)
print(numbers[1])
print(numbers[-1])

# indexing with nested data structures 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])
print(matrix[2][1])

# indexing with dictionaries 
student = {"name":"alice","age":25,"grade":"a"}
print(student["name"])
print(student["age"])


# using indexing in a loop 
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"index{i}:{colors[i]}")

