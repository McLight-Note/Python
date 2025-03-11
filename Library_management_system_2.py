# 2025.03.11
# Mavzu: Library management system
# MUallif: Muhammadsodiq

print('Library management')

books = {
    "Python": 7,
    "Clean Code": 2,
    "Computer Science: An overview": 4,
    "Neural Networks": 5
}

def display_books():
    print("\nAvailable Books:")
    for book, quantity in books.items():
        if quantity > 0:
            print(f"{book} ({quantity} copies)")

def take_book(book_name):
    if book_name in books and books[book_name] > 0:
        books[book_name] -= 1
        print(f"You borrowed '{book_name}'")
    else:
        print("Sorry, this book is not available.")

def return_book(book_name):
    if book_name in books:
        books[book_name] += 1
        print(f"You returned '{book_name}'")
    else:
        print("This book does not belong to our library.")

while True:
    print("1. View Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        display_books()
    elif choice == '2':
        book = input("Enter the book name: ")
        take_book(book)
    elif choice == '3':
        book = input("Enter the book name: ")
        return_book(book)
    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")