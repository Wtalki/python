class User:
    def __init__(self,email):
        if User.is_valid_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email format")
        
        
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email
    
try:
    user = User("hello243@gmail.com")
    print("User created with email:", user.email)
except ValueError as e:
    print(e)

try:
    invalid_user = User("invalid-email")
except ValueError as e:
    print(e)