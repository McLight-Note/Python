# 2025.03.11
# Mavzu: Library management system
# Muallif: Muhammadsodiq

class Library:
    def __init__(self):
        self.books = {
            "Python Basics": 3,
            "Machine Learning": 2,
            "Data Science": 4,
            "Algorithms": 5
        }

    def display_books(self):
        print("\nAvailable Books:")
        for book, quantity in self.books.items():
            if quantity > 0:
                print(f"{book} ({quantity} copies)")

    def borrow_book(self, book_name):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(f"You have borrowed '{book_name}'")
        else:
            print("Sorry, this book is not available.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
            print(f"You have returned '{book_name}'")
        else:
            print("This book does not belong to our library.")

library = Library()

while True:
    print("\nLibrary Management System")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        library.display_books()
    elif choice == '2':
        book = input("Enter the book name: ")
        library.borrow_book(book)
    elif choice == '3':
        book = input("Enter the book name: ")
        library.return_book(book)
    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
