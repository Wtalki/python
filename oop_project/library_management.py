class Book:
    def __init__(self, book_id, title, author, description=""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.description = description  # Add description attribute

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return f"Book checked out: {self.title}"
        else:
            return "Book is currently unavailable."

    def return_book(self):
        self.is_available = True
        return f"Book returned: {self.title}"

    def display(self):
        return f"Id: {self.book_id}, Title: {self.title}, Description: {self.description}, available : {'yes' if self.is_available else 'no'}"
