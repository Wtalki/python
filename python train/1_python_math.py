# import math
# x = -10
# result = abs(x) #get the absolute value of  x
# print(result)

# y = 2
# z = 3
# result = pow(y,z) #calculate 2 raise to the power of 3
# print(result)
# # Comment: `pow` (or `x ** y`) is helpful for exponential calculations, such as compound interest or scientific formulas.

# x = 1.14159
# print(round(x,2)) # rounds x to 2 decimal places


# x =16
# result = math.sqrt(x) #calculates the square root of x
# print(result)

# x = 5
# result = math.factorial(x) #calculates the factorial of x
# print(result)


# x = 48 
# y = 18 
# result = math.gcd(x,y) # finds the greatest common divisor of x and y
# print(result)

# x = 2
# result = math.exp(x) # calculates e raised to the power of x
# print(result)

# x = 100
# result = math.log(x,10) #calculates the logarithm of x with base 10
# print(result)

# x = 2.1
# result = math.ceil(x) # rounds x up to the nearest integer
# print(result)

# x = 2.9
# result = math.floor(x) # round x down to the nearest integer
# print(result)

# x = math.pi /2
# result = math.sin(x) #calculates the sine of x
# print(result)

# x = math.pi
# degrees = math.degrees(x) #converts radians to degrees
# print(degrees)

# angle = 180
# radians  = math.radians(angle)
# print(radians)

# import statistics
# data = [1,2,3,4,5]
# mean_value = statistics.mean(data) # calculates the mean (average) of data
# print(mean_value)

# data = [1,2,3,4,5]
# median_value = statistics.median(data) # finds the median of data
# print(median_value)

# data = [1,2,2,3,4]
# mode_value = statistics.mode(data)
# print(mode_value)


# import random
# result = random.randint(1,100)
# print(result)

# sequence = ['apple','banana','cherry']
# result = random.choice(sequence) # picks a random element from te sequence
# print(result)

# x = -3
# y = 10
# result = math.copysign(x,y) # copies the sign of y to x
# print(result)

# a = .1 + .2
# b = .3

# result = math.isclose(a,b) # checks if a is approximately equal to b
# print(result)

# x = 7
# y =2
# result = math.fmod(x,y) #returns the remainder of x divided by y
# print(result)


# import math 
# x= 1
# print(math.sinh(x)) #hyperbolic sine of x
# print(math.cosh(x))# hperbolic cosine of x
# print(math.tanh(x))#hperbolic tangent of x

# x =10
# y=3

# quotient, remainder = divmod(x,y) # divides x by y and returns the quotient and remainder
# print(quotient,remainder)


# print(math.inf) # positive infinity
# print(-math.inf) # negative infinity
# print(math.nan) # not a number


# import statistics
# data = [1,2,3,4,5]
# stdev_value = statistics.stdev(data) # calculates standard diviation of data
# print(stdev_value)

# import random
# sequence = ['apple','banana','dherry','data']
# sample = random.sample(sequence,2) #selects 2 random elements from the sequence
# print(sample)


# import random
# sequence = ['apple','banana','cherry']
# random.shuffle(sequence) # shuffles the elements of the sequencein place
# print(sequence)


x = -10
result = abs(x)
print(result)


x = 2
y = 3
result = pow(x,y)
print(result)

x = 3.14159
result = round(x,2)
print(result)

import math 
x = 16 
result = math.sqrt(x)
print(result)

import math 
x = 5
result = math.factorial(x)
print(result)

import math 
x = 48
y = 18
result = math.gcd(x,y)
print(result)

import math
x = 2
result = math.exp(x)
print(result)

x = 100
result = math.log(x,10)
print(result)

x = 2.1
result = math.ceil(x)
print(result)

import math 
x = 2.9
result = math.floor(x)
print(result)

x = math.pi / 2
result = math.sin(x)
print(result)

import math
x = math.pi
degrees = math.degrees(x)

print(degrees)


import statistics
data = [1,2,3,4,5,6,7]
mean_value = statistics.mean(data)

print(mean_value)


data = [1,2,3,4,5]
median_value = statistics.median(data)
print(median_value)


import statistics
data = [1,2,2,3,4]
mode_value = statistics.mode(data)
print(mode_value)


import random 
result = random.randint(1,10)
print(result)

sequence = ['apple', 'orange', 'banana']
result = random.choice(sequence)
print(result)
# sone lin thaw sit say mu nit ywar chal mu a  twat a thone pyu nai pr thi 


import math
x = -4
y = 10
resutl = math.copysign(x,y)
print(resutl)

import math 
x= 7 
y = 2
result = math.fmod(x,y)
print(result)

import math 
x = 1
print(math.sinh(x))
print(math.cosh(x))
print(math.tanh(x))

x = 10
y = 3
quotient,remainder = divmod(x,y)
print(quotient,remainder)

import math 
print(math.inf)
print(-math.inf)
print(math.nan)

import statistics 
data = [1,2,10]
variance_value = statistics.variance(data)
print(variance_value)


data = [1,2,3,4,5]
stdev_value = statistics.stdev(data)
print(stdev_value)



import random
sequence = [ 'apple','banana','cherry','data']
sample = random.sample(sequence,2)
print(sample)

sequence = ['apple','banana','cherry','data']
random.shuffle(sequence)

print(sequence)





