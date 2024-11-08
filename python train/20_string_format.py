name = "alice"
age = 30

formatted_string = "my name is %s and i am %d years old" % (name,age)
print(formatted_string)


price = 19.99
item = "book"
formatted_string = "the %s costs $%.2f" %(item,price)
print(formatted_string)

# str.format() method 

name = "bob"
age = 25 
formatte_string = "my name is {}, and i am {} years old".format(name,age)
print(formatte_string)

formatted_string = "my name is {1} and i am {0} years oold".format(age,name)
print(formatted_string)


# formattin numbers an alignment 
pi = 3.141589
formatted_string = "pi si apporximately {:.2f}".format(pi)
print(formatted_string)


formatted_string = "{:<10} is left-aligned, {:>10} is right-aligned, {:^10} is ceenter".format("left","right","center")

print(formatted_string)

name = "diana"
age = 27
formatted_string = f"my name is {name}, and i am {age} years old."
print(formatte_string)

x = 5
y = 10
formatte_string = f"the sum of { x} and {y} is {x + y}"
print(formatte_string)


value = 1234.5678
formatted_string = f"the value is {value:.2f}"
print(formatte_string)

# Padding and alignment
formatted_string = f"{'left':<10} | {'center':^10} | {'right':>10}"
print(formatted_string)

#template strings 
from string import Template

# Define a template
template = Template("My name is $name, and I am $age years old.")

# Substitute values using a dictionary
formatted_string = template.substitute(name="Eve", age=22)
print(formatted_string)  # Output: My name is Eve, and I am 22 years old.

# Using safe_substitute
template = Template("My name is $name, and I live in $country.")
formatted_string = template.safe_substitute(name="Frank")
print(formatted_string)  # Output: My name is Frank, and I live in $country.
