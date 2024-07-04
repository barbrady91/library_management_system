class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.book_id} | {self.title} | {self.author} | {self.year}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def view_books(self):
        for book in self.books:
            print(book)
    
    def search_books_by_title(self, title):
        return [book for book in self.books if book.title == title]
    
    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book by title")
        print("4. Remove a book by ID")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = int(input("Enter publication year: "))
                book = Book(book_id, title, author, year)
                library.add_book(book)
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Please enter correct values.")
        
        elif choice == '2':
            library.view_books()
        
        elif choice == '3':
            title = input("Enter book title to search: ")
            results = library.search_books_by_title(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found with that title.")
        
        elif choice == '4':
            try:
                book_id = int(input("Enter book ID to remove: "))
                library.remove_book(book_id)
                print("Book removed successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid book ID.")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
