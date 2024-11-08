#tuples in pythons 

tuple1 = (1,2,3)
tuple2 = ("apple","banana","cherry")

tuple3 = 1,2,3
single_element_tuple = (5,)

# accessing tuple elements
fruits = ("apple","banana","cherry")
print(fruits[0])
print(fruits[-1])

numbers = 91,2,3,4,5
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuple operations
tuple_a = (1,2)
tuple_b = (3,4)

combine = tuple_a + tuple_b
print(combine)
repeated = tuple_a *3
print(repeated)


#checking for membership 
fruits = ("apple","banana","cherry")
print("apple" in fruits)
print("grape" not in fruits)

numbers = (1,2,3)
# numbers[0] = 10
# print(numbers) # tuple object does not support item assignment

mixed_tuple = (1,[2,3],4)
mixed_tuple[1][0] =20
print(mixed_tuple)


#common tuple methods
example = (1,2,3,2,4,2)
count_2 = example.count(2)
print(count_2)

index_of_3 = example.index(3)
print(index_of_3)

# tuple packing and unpacking
person = ("alice", 30, "engineer")

name,age,profession = person
print(name)
print(age)
print(profession)


# 3using * for extended unpacking 
numbers = (1,2,3,4,5)
first, *middle, last = numbers
print(first) #output 1
print(middle) #output [2,3,4]
print(last) #output 5

#example :using tuples in a dictionary
locations = {
    (0,0):"orange",
    (1,0):"point a",
    (0,1): "point b",
}
print(locations[(0,0)])
print(locations[(1,0)])




