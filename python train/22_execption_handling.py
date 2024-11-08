try:
    risky_operation = 10 /0
    
except ZeroDivisionError:
    print("cannot divide by zero")


try:
    value = int("abc")
    result = 10 / value 
except ValueError:
    print("invalid format number")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as e:
    print(f"an unexpected error occurred: { e}")
    

# using finallly 
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("file not found!")
finally:
    print("closing file.")
    if "file" in locals():
        file.close()
        

def divide(a,b):
    if b == 0:
        raise ValueError("denominator cannot be zero")
    return a / b
try:
    result = divide(10,0)
except ValueError as e:
    print(e)
        
        
# custom exceptions 
class NegativeNumberError(Exception):
    pass
def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return x ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(e)


# exception handling in afunciton 
def calculate_average(numbers):
    try:
        average = sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("cannot calculate the average of an empty list.")
    except TypeError:
        print("the list must contain only numbers.")
    else:print("average is:", average)
calculate_average([])
calculate_average(["a", "b"])
calculate_average([1,3])