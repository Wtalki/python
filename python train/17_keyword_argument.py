# keyword arguments in pyuthon 

# basid usage of keyword arguments 
def intorduce(name, age, city):
    print(f"my name is {name}, I am {age} years old, and i live in {city}")
intorduce(name = "alice", age = 34, city= "new york")

intorduce(city="losanglses", name = "zaw", age= 25)

# using default parameters  with keyword arguments 
def greet(name, greeting = "hello"):
    print(f"{greeting}", name)
greet("zaw lay")
greet("zaw win","welcome")


# using **kwargs to accept arbitrary keyword arguments 
def display_profile(name,**kwargs):
    print(f"name:{name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

display_profile("alice", age= 20,city="new york", jop = "engineero")


# combining #args and **kwargs in afunction 
def order_summary(order_id,*items,**details):
    print(f"order id : {order_id}")
    print("items:")
    for item in items:
        print(f"- {item}")
    print("details:")
    for key,value in details.items():
        print(f"{key.capitalize()}: {value}")

order_summary(12345,"laptop","mouse",customer = "alice", address = "123 mai")


# using **kwargs to pass arguments to other functions 
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def welcome_user(**kwargs):
    greet(**kwargs)

welcome_user(name="Alice", greeting="Hi")  # Output: Hi, Alice!

# example building a flexible functio with **kwargs 
def create_profile(name, **details):
    profile = {"name":name}
    profile.update(details)
    return profile

profile1 = create_profile("alice", age= 30, city= "new york", job = "engineer")
print(profile1)
profile2 = create_profile("alice", age= 30, city= "new york", job = "engineer")
print(profile2)