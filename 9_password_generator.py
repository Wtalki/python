import random
import string 

def generate_password(length,use_letters=True,use_numbers=True,use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters 
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("no character types selected please select at lease one character type.")
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password 

def main():
    print("welcome to the password generator!")

    while True:
        try:
            length = int(input("enter the length of the password: "))
            if length <= 0:
                print("please enter a positive number.")
            else:
                break
        except ValueError:
            print("invalid input. please enter a number")

    use_letters = input("include letters (y/n): ").strip().lower() == 'y'
    use_numbers = input("include numbers (n): ").strip().lower() == 'y'
    use_symbols = input("include symbols (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters,use_numbers,use_symbols)
    print(f"your generated password is : { password}")

main()