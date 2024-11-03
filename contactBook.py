class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
            contact = Contact(name, phone)
            self.contacts.append(contact)
            print(f"Contact {name} added.")

    def view_contacts(self):
            if not self.contacts:
                print("No contacts available.")
            else:
                for contact in self.contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self,name):
            found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
            if found_contacts:
                for contact in found_contacts:
                    print(f"name: {contact.name}, Phone: {contact.phone}")
            else:
                print("no contacts found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\ncontact book menu:")
        print("1 add contact")
        print("2 view contacts")
        print("3.search contact")
        print("4 exit")
        choice = input("choose an option")

        if choice == '1':
            name = input("enter contact name: ")
            phone = input("enter contact phone:")
            contact_book.add_contact(name,phone)
        elif choice == '2':
            contact_book.view_contacts()
        elif  choice == '3':
            name = input("enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            print("exit contact book")
            break
        else:
            print("invalid choice.please try again")

if __name__ == "__main__":
    main()
        