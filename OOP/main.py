from library import Library
from book import Book

def run():
    # create an instance of the library class
    library = Library()

    while True:
        action = input("Enter an action: (add, lend, return, search, exit)").lower()
        
        if action == "exit":
            break

        try:
            if action == "add":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(title, author)
                library.add_book(book)
                print(f"Added book, {title}")
            elif action == "lend":
                title = input("Enter book title to lend: ")
                library.lend_book(title)
            elif action == "return":
                title = input("Enter a book to return: ")
                library.return_book(title)
            elif action == "search":
                title = input("Enter book title to search: ")
                book = library.find_book(title)
                if book:
                    availability = "available" if book.is_available else "not available"
                    print(f"{title} by {book.author} is {availability}")
                else:
                    print(f"Book {title} not found")
            else:
                print("Please choose from the options above")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run()