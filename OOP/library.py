class Library:

    def __init__(self):
        self.books = [] # stores instances of the Book class

    # add a book object to self.books
    def add_book(self, book):
        self.books.append(book)



    # searching for a book
    def find_book(self, title):
        for book in self.books:
            # checking if the title attribute from our book object
            # is equal to the title we're passing into the function
            if book.title == title:
                return book #returns the book object where the title matches
        return None # if no title matches we return none
    
    def lend_book(self, title):
        book = self.find_book(title)
        # if we are able to find the book in our list and successfully check the book out - is_available == True
        if book and book.check_out():
            print(f"Book {title} has been lent out")
        else:
            print(f"Book {title} is unavailable!")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book() # sets self.is_available for a specific book object back to True
        else:
            print(f"Book {title} is not found in the library")


    

    
