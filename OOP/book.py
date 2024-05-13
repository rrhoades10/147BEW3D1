class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available: #is it true that the book is available
            self.is_available = False # set availability to False because we're checking it out
            return True # because it is true that we are able to check out the book
        return False # return false if self.is_available is false and we arent able to check it out
    
    def return_book(self):
        self.is_available = True