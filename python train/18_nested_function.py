#nested functions 
def outer_function():
    print("this is the ourter function.")
    def inner_function():
        print("this is the inner function.")
    inner_function()
outer_function()

# using varibles form the outer function 
def greet(name):
    def get_message():
        return f"hello, {name}!"
    message = get_message()
    print(message)

greet("zaw lay")

# returning a nested function 
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
print(double(5))

triple = make_multiplier(3)
print(triple(5))


# closures in python 

def outer_function(text):
    def inner_function():
        print(text)  # `text` is captured by the inner function
    return inner_function

# `my_func` is now a closure that "remembers" the `text` value "Hello!"
my_func = outer_function("Hello!")
my_func()  # Output: Hello!


# pracitcal example logging with nested functions 
def logger(prefix):
    def log_message(message):
        print(f"[{prefix}] {message}")
    return log_message

info_logger = logger("info")
error_logger = logger("error0")
info_logger("this is an information  messages")
error_logger("this is an error  messages")


# using nonlocal in nested functions 
def counter():
    count = 0  # Initial count

    def increment():
        nonlocal count  # Allows modification of `count` in the outer scope
        count += 1
        return count

    return increment

# Create a counter function
my_counter = counter()
print(my_counter()) 
print(my_counter()) # Output:
print(my_counter()) # Output:)


# example nested funcitons for data processing 
def make_fileter(conditon):
    def filter_data(data):
        return [x for x in data if conditon(x)]
    return filter_data

even_filter = make_fileter(lambda x : x % 2 == 0)
positive_filter = make_fileter(lambda x : x > 0)

numbers = [10, -5, 0 ,3, 3 -1]

print(even_filter(numbers))
print(positive_filter(numbers))