class Memory:
    def __init__(self):
        self.value = 0  # Initialize memory to store a value

    def store(self, value):
        self.value = value

    def recall(self):
        return self.value

    def clear(self):
        self.value = 0


class Calculator:
    def __init__(self):
        self.memory = Memory()  # Create an instance of Memory class

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

    def exponentiate(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            return "Error! Square root of a negative number is not real."
        return a ** 0.5

    def run(self):
        while True:
            # Display menu
            print("\nSelect Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Square Root")
            print("7. Store Result in Memory")
            print("8. Recall Memory")
            print("9. Clear Memory")
            print("0. Exit")

            # Get user choice
            choice = input("Choose an operation (0-9): ")

            # Exit if the user chooses 0
            if choice == '0':
                print("Exiting calculator.")
                break

            # Perform selected operation
            if choice in ['1', '2', '3', '4', '5']:
                # For binary operations, get two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = self.add(num1, num2)
                elif choice == '2':
                    result = self.subtract(num1, num2)
                elif choice == '3':
                    result = self.multiply(num1, num2)
                elif choice == '4':
                    result = self.divide(num1, num2)
                elif choice == '5':
                    result = self.exponentiate(num1, num2)
                
                print("Result:", result)

            elif choice == '6':
                # For square root, get one number
                num = float(input("Enter a number for square root: "))
                result = self.square_root(num)
                print("Result:", result)

            elif choice == '7':
                # Store last result in memory
                try:
                    self.memory.store(result)
                    print("Stored in memory:", result)
                except NameError:
                    print("No result available to store in memory.")

            elif choice == '8':
                # Recall memory
                print("Recalled from memory:", self.memory.recall())

            elif choice == '9':
                # Clear memory
                self.memory.clear()
                print("Memory cleared.")

            else:
                print("Invalid choice! Please select a valid operation.")

            # Option to continue or exit
            cont = input("Do you want to perform another calculation? (y/n): ").lower()
            if cont != 'y':
                print("Exiting calculator.")
                break


# Create an instance of Calculator and run it
calculator = Calculator()
calculator.run()
