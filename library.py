class Book:
    def __init__(self, book_id, title, author, is_checked_out=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author}, {'Checked out' if self.is_checked_out else 'Available'}"

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.book_id in self.books:
            raise Exception("This book ID already exists.")
        else:
            self.books[book.book_id] = book

    def update_book(self, book_id, title=None, author=None):
        if book_id not in self.books:
            raise Exception("Book not found.")
        else:
            if title:
                self.books[book_id].title = title
            if author:
                self.books[book_id].author = author

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise Exception("Book not found.")

    def list_books(self):
        return list(self.books.values())  # Return list of books

    def search_books(self, query):
        found_books = [book for book in self.books.values() if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        return found_books  # Return found books

    def check_out_book(self, book_id):
        if book_id not in self.books:
            raise Exception("Book not found.")
        elif self.books[book_id].is_checked_out:
            raise Exception("Book is already checked out.")
        else:
            self.books[book_id].is_checked_out = True

    def check_in_book(self, book_id):
        if book_id not in self.books:
            raise Exception("Book not found.")
        elif not self.books[book_id].is_checked_out:
            raise Exception("Book is not checked out.")
        else:
            self.books[book_id].is_checked_out = False


def main():
    library_manager = LibraryManager()

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. List all books")
        print("5. Search for books")
        print("6. Check out a book")
        print("7. Check in a book")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library_manager.add_book(Book(book_id, title, author))
        elif choice == '2':
            book_id = input("Enter book ID: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            library_manager.update_book(book_id, title, author)
        elif choice == '3':
            book_id = input("Enter book ID to delete: ")
            library_manager.delete_book(book_id)
        elif choice == '4':
            library_manager.list_books()
        elif choice == '5':
            query = input("Enter search query (title or author): ")
            library_manager.search_books(query)
        elif choice == '6':
            book_id = input("Enter book ID to check out: ")
            library_manager.check_out_book(book_id)
        elif choice == '7':
            book_id = input("Enter book ID to check in: ")
            library_manager.check_in_book(book_id)
        elif choice == '8':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()