from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available copies: {self.copies}"

    def is_available(self):
        return self.copies > 0

    def borrow_book(self):
        if self.is_available():
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

    def borrow_book(self, book, library):
        if book.is_available():
            if library.loan_book(book, self):
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book.title}.")
            else:
                print(f"{self.name} could not borrow {book.title}.")
        else:
            print(f"{book.title} is not available for borrowing.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            library.return_book(book, self)
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title} to return.")


class Loan:
    def __init__(self, book, member, due_date):
        self.book = book
        self.member = member
        self.due_date = due_date
        self.returned = False

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.name}, due on {self.due_date.strftime('%Y-%m-%d')}"

    def mark_returned(self):
        self.returned = True


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member {member.name}.")

    def loan_book(self, book, member):
        if book.borrow_book():
            due_date = datetime.now() + timedelta(days=14)  # Loan period of 14 days
            loan = Loan(book, member, due_date)
            self.loans.append(loan)
            return True
        return False

    def return_book(self, book, member):
        for loan in self.loans:
            if loan.book == book and loan.member == member and not loan.returned:
                loan.mark_returned()
                book.return_book()
                print(f"Book {book.title} returned by {member.name}.")
                return True
        print(f"No active loan found for {book.title} by {member.name}.")
        return False

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available():
                print(book)

    def list_loans(self):
        print("Current Loans:")
        for loan in self.loans:
            if not loan.returned:
                print(loan)


# Example Usage with Input
def main():
    library = Library()

    # Add some books to the library
    book1 = Book("1984", "George Orwell", "123456789", 3)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 2)
    library.add_book(book1)
    library.add_book(book2)

    # Add some members to the library
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    library.add_member(member1)
    library.add_member(member2)

    # Main loop for user input
    while True:
        print("\nLibrary Management System")
        print("1. List available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List current loans")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.list_available_books()
        
        elif choice == "2":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to borrow: ")

            # Find the member and book
            member = next((m for m in library.members if m.name == member_name), None)
            book = next((b for b in library.books if b.title == book_title), None)

            if member and book:
                member.borrow_book(book, library)
            else:
                print("Invalid member or book title.")
        
        elif choice == "3":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to return: ")

            # Find the member and book
            member = next((m for m in library.members if m.name == member_name), None)
            book = next((b for b in library.books if b.title == book_title), None)

            if member and book:
                member.return_book(book, library)
            else:
                print("Invalid member or book title.")
        
        elif choice == "4":
            library.list_loans()

        elif choice == "5":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
