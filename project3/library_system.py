import json

library = []

# Function to display the menu
def display_menu():
    print("\n1. Add a book\n2. Remove a book\n3. Search a book\n4. Display all books\n5. Statistics\n6. Exit")
    return input("Choose an option: ")

# Add a book
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    genre = input("Enter genre: ")
    read = input("Read (yes/no): ").lower() == 'yes'
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    print("Book added!")

# Remove a book
def remove_book():
    title = input("Enter book title to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print("Book removed!")

# Search for a book
def search_books():
    term = input("Search by (1) Title or (2) Author: ")
    query = input("Enter search term: ").lower()
    results = [book for book in library if (query in book["title"].lower() if term == '1' else query in book["author"].lower())]
    for book in results:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display all books
def display_books():
    if library:
        for book in library:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("Library is empty.")

# Display statistics
def display_statistics():
    total = len(library)
    read = sum(1 for book in library if book["read"])
    print(f"Total books: {total}, Read: {read}, Unread: {total - read}, Read %: {read/total*100 if total else 0:.2f}%")

# Save library to a file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file)
    print("Library saved.")

# Load library from a file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main function
def main():
    global library
    library = load_library()
    
    while True:
        choice = display_menu()
        if choice == '1': add_book()
        elif choice == '2': remove_book()
        elif choice == '3': search_books()
        elif choice == '4': display_books()
        elif choice == '5': display_statistics()
        elif choice == '6':
            save_library()
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
