class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\n✅ Book added: {book}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"\n❌ Book removed: {book}")
                return
        print("\n⚠️ Book not found.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() 
                   or keyword.lower() in book.author.lower()]
        return results

    def list_books(self):
        if not self.books:
            print("\n📚 Your library is empty.")
        else:
            print("\n📚 Books in your library:")
            for book in self.books:
                print(f"  - {book}")


def main():
    library = Library()

    while True:
        print("\n--- Personal Library Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List All Books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            results = library.search_books(keyword)
            if results:
                print("\n🔍 Search Results:")
                for book in results:
                    print(f"  - {book}")
            else:
                print("\n😕 No books found.")

        elif choice == '4':
            library.list_books()

        elif choice == '5':
            print("👋 Exiting... Bye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
