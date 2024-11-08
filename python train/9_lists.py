numbers = [1,2,3,4,5]
words = ["apple","banana","cherry"]
mixed = [1,"hello",3.5,True]

fruits = ["apple","banana","cherry"]

print(fruits[0]) #output apple
print(fruits[-1]) #output cherry

#modifying list elements 
fruits = ["apple","banana","cherry"]
fruits[1] = "blueberry"
print(fruits) #output ['apple','blueberry','banana','cherry']

#list slicing

numbers = [1,2,3,4,5,6,7,]
print(numbers[1:5])
print(numbers[:4])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])

list = [1,2,3]
list2 = [4,5,6]
print(list + list2)
print(list * 3)

fruits = ["apple","banana","cherry"]
print("apple" in fruits)
print("grape" not in fruits)

fruits.append("orange")
print(fruits)

fruits.insert(1,"blueberry")
print(fruits)

fruits.remove("banana")
print(fruits)

last_fruit = fruits.pop()
print(fruits)

pos = fruits.index("apple")
print(pos)

count_banan = fruits.count("cherry")
print(count_banan)


numbers = [3,1,3,4,6,2,6]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

fruits.clear()
print(fruits)

# loopint through lists

fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

#list comprehensions

# new_list = [expression for item in terable if conditon]

squares = [x**2 for x in range(1,6)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# nested lists 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(matrix[0][1])

for row in matrix:
    for element in row:
        print(element, end = " ")
    print()

#common pitfalls with lists 
def append_to_list(item,my_list=[]):
    my_list.append(item)
    return my_list

original_list = [1,2,3]
new_list = original_list
new_list.append(4)
print(new_list)

original_list = [1,2,3]
new_list = original_list.copy()
new_list = original_list[1:]
print(new_list)