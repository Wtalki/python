# Function to encrypt the message
def encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, add it as-is
            encrypted_message += char
            
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, shift):
    decrypted_message = ""
    
    for char in encrypted_message:
        # Check if character is an uppercase letter
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # If it's not a letter, add it as-is
            decrypted_message += char
            
    return decrypted_message

# Main function to run the program
def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ").lower()
    
    if choice not in ('e', 'd'):
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number (e.g., 3 for Caesar cipher): "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

# Run the program
main()
