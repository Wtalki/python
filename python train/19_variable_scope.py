# # variable scope ?
# def my_function():
#     x = 10
#     print(x)

# my_function()
# print(x)

def outer_function():
    y = 20
    def inner_function():
        nonlocal y #allows modification of the enclosing variable
        y += 5
        print("inner:", y)
    inner_function()
    print("outer", y)
    
outer_function()


# global scope 
x = 50 # globla varialbe
def update_global():
    global x #allows modification of the flobal variable 
    x += 10 
    print("inside function:", x)
    
update_global()
print("outside function", x)


# buld in scope 
print(len("hello"))
len = 5
print(len)


# legb rule 
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
# Output:
# Inner: local
# Outer: enclosing
# Global: global


# examples of global and nonlocal keywords 
count = 0
def increment():
    global count 
    count += 1
increment()
print(count)

def outer():
    count =10
    def inner():
        nonlocal count
        count += 5
        print("inner count", count)
    
    inner()
    print("outer count:", count)

outer()

