# python module 

import math
result = math.sqrt(16)
print(result)


print(math.pi)

# import specific function or variables 
from math import sqrt,pi
print(sqrt(9))
print(pi)


# alias imports 
import math as m

print(m.sqrt(25))

from math import *
print(sin(.5))

# built in modules 
import math 
print(math.factorial(5))
import datetime 
now = datetime.datetime.now()
print(now)

import random 
print(random.randint(1,10))

import os
print(os.getcwd())

import sys 
print(sys.version)

import sys 
print(sys.version)


# creating a custom module 
def greet(name):
    return f"Hello, {name}"
pi = 3.14
print(greet("hello"))


# using the cstom module 

# installing third part module 
import requests 
response = requests.get("https://api.github.com/")
print(response.status_code)


def greet(name):
    return f"hello, {name}"

if __name__ == "__main__":
    print(greet("alice"))
    
# common module techiniques 
import math 
print(dir(math))

help(math.sqrt)



