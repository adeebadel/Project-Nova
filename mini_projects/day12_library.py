books = []


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if title and author:
        books.append({
            "title": title,
            "author": author,
            "available": "Yes"
        })
        print("Book added successfully!\n")
    else:
        print("Title and author cannot be empty.\n")


def view_books():
    if not books:
        print("No books in the library yet.\n")
        return

    print("Library Books:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} by {book['author']} | Available: {book['available']}")
    print()


def borrow_book():
    if not books:
        print("No books available to borrow.\n")
        return

    view_books()
    try:
        choice = int(input("Enter the number of the book to borrow: "))
        if 1 <= choice <= len(books):
            book = books[choice - 1]
            if book["available"] == "Yes":
                book["available"] = "No"
                print(f"You borrowed '{book['title']}'.\n")
            else:
                print("This book is already borrowed.\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("Library Menu")
        print("1. Add a book")
        print("2. View books")
        print("3. Mark a book as borrowed")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
