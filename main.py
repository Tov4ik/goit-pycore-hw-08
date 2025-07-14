import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def list_contacts(self):
        return self.contacts

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    print("Welcome to the Address Book!")

    while True:
        command = input("Enter command (add/list/exit): ").strip().lower()

        if command == "add":
            name = input("Name: ")
            phone = input("Phone: ")
            book.add_contact(name, phone)
            print(f"Added contact: {name}")

        elif command == "list":
            contacts = book.list_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")

        elif command in ("exit", "close"):
            save_data(book)
            print("Address book saved. Goodbye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
