float_value = 2.2
int_value = int(float_value)

string_number = "20"
int_value = int(string_number)

# Integer to Float
int_value = 5
float_value = float(int_value)  # float_value is 5.0
print(float_value)

# String to Float
string_number = "3.14"
float_value = float(string_number)  # float_value is 3.14
print(float_value)

# Integer to String
int_value = 123
string_value = str(int_value)  # string_value is "123"
print(string_value)

# Float to String
float_value = 3.14159
string_value = str(float_value)  # string_value is "3.14159"
print(string_value)

# Boolean to String
bool_value = True
string_value = str(bool_value)  # string_value is "True"
print(string_value)

# Integer to Boolean
print(bool(1))  # True
print(bool(0))  # False

# String to Boolean
print(bool("Hello"))  # True
print(bool(""))       # False

# List to Boolean
print(bool([1, 2, 3]))  # True
print(bool([]))         # False

# list,tuple,and set convesion 
text = "hello"
list_value = list(text)
print(list_value)

# tuple 
tuple_value = (1,2,3)
list_value = list(tuple_value)
print(list_value)


# list to set 
list_value = [1,2,3]
tuple_value = tuple(list_value)
print(tuple_value)


# List of tuples to Dictionary
list_of_pairs = [("name", "Alice"), ("age", 25)]
dict_value = dict(list_of_pairs)  # dict_value is {'name': 'Alice', 'age': 25}
print(dict_value)

# List of lists to Dictionary
list_of_lists = [["name", "Bob"], ["age", 30]]
dict_value = dict(list_of_lists)  # dict_value is {'name': 'Bob', 'age': 30}
print(dict_value)

# Real number to Complex
real = 5
complex_number = complex(real)  # complex_number is (5+0j)
print(complex_number)

# Real and Imaginary parts
real = 3
imaginary = 4
complex_number = complex(real, imaginary)  # complex_number is (3+4j)
print(complex_number)

age = input("Enter your age: ")         # Takes input as string
age = int(age)                          # Convert to integer

height = input("Enter your height: ")
height = float(height)                  # Convert to float

is_student = input("Are you a student? (yes/no): ")
is_student = bool(is_student == "yes")  # Convert to boolean based on response

print(f"Age: {age}, Height: {height}, Student: {is_student}")


