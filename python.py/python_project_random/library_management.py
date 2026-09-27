books = {}

def add_book():
    book_id = input("Enter book id: ")
    if book_id in books:
        print("Book already exists!")
        return
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    books[book_id] = {
        "name": name,
        "author": author,
        "available": True
    }
    print("Book added successfully 🤗")
def view_books():
    if len(books) == 0:
        print("No books available 😥")
        return
    print("\n== Books List ==")
    for book_id, book in books.items():
        print("\nBook ID:", book_id)
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
def issue_book():
    book_id = input("Enter book id: ")
    if book_id not in books:
        print("Book not found 😥")
        return
    if books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued successfully 😁🤗")
    else:
        print("Book is already issued 🙂")
def return_book():
    book_id = input("Enter Book ID: ")
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully!")
    else:
        print("Book not found!")
# Main Program
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
