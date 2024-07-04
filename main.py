class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def display_books(self):
        for book in self.books:
            print(book)

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Search for a book by title")
        print("3. Search for a book by author")
        print("4. Display all books")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")
        
        elif choice == '2':
            title = input("Enter title to search: ")
            results = library.search_by_title(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found with that title.")
        
        elif choice == '3':
            author = input("Enter author to search: ")
            results = library.search_by_author(author)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found by that author.")
        
        elif choice == '4':
            library.display_books()
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
