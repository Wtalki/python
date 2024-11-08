#dictionaries in python 
students = {"name":"alice","age":25,"courses":["math","science"]}

person = dict(name = "john", age = 30, city = "new york")

print(students)
print(person)


#accessing dictionary elemnts
print(students["name"])
print(students.get("age"))
print(students.get("grade","not found"))


#adding and modifying elements 
students['grade'] = 'A'
print(students)

students["age"] = 26
print(students)

#removing elements 
del students['grade']
print(students)

age = students.pop("age")
print(age)
print(students)

last_item = students.popitem()
print(last_item)
print(students)


#dictionary methods 
student = {"name": "alice", "age":25, "courses":["math","science"]}

print(student.keys())
print(student.values())
print(student.items())

# iterating through a dictionary 
for key, value in student.items():
    print(f"{key}:{value}")
    
#dictionary comprehension
squares = {x:x**2 for x in range(1,6)}
print(squares)

# nested dictionares 
classroom = {
    "student1" : {"name" : "alice","age":25},
    "student2":{"name":"bob","age":22}
}
print(classroom["student1"]["name"])
print(classroom['student2']['name'])


# example:managing inventory with dictionares 
inventory = {
    "apple": 10,
    "banana":5,
    "orange":8
}

inventory["grape"] = 15
inventory["apple"] += 5

print(f"apples in stock:{inventory.get('apple')}")
print(f"peaches in stck:{inventory.get('peach',0)}")
print(f"peaches in stck:{inventory.get('apple',0)}")
