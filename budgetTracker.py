import math

def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):

    if b == 0:
        return "error division by zero"
    return a/b

def exponentiate(a,b):
    return a**b

def square_root(a):
    if a < 0:
        return "error cannot find the square root of a negative number"
    return math.sqrt(a)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input ! Please enter a number")

def get_operation():
    print("\nselect operation")
    print("1addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 exponentiation")
    print("6 exponentiation")

    while True:
        operation = input("enter your choice(1-6)")
        if operation in ['1','2','3','4','5','6','7','8','9']:
            return operation
        print("invalid choice please choose a valid operation")

def calculator():
    while True:
        operation = get_operation()
        if operation == '6':
            a = get_number("enter the number")
            result = square_root(a)
        else:
            a= get_number("enter the first number")
            b = get_number("enter the second number")

            if operation == '1':
                result = add(a,b)
            elif operation == '2':
                result = subtract(a,b)
            elif operation == '3':
                result = multiply(a,b)
            elif operation == '4':
                result = divide(a,b)
            elif operation == '5':
                result = exponentiate(a,b)
        print ("result: ", result)

        cont = input("do you want to perform another calculation? (y/n)").lower()
        if cont != "y":
            break

calculator()

