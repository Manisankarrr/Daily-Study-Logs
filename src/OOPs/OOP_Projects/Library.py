class Books:
    def __init__(self, name, is_available):
        self.name = name
        self.is_available = is_available
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book {self.name} has been borrowed")
        else:
            print(f"Book {self.name} is already borrowed")
        
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book {self.name} has been returned")
        else:
            print(f"Book {self.name} is already available")
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book_name):
        book = Books(book_name)
        self.books.append(book)

    def display_book(self):
        available_books = [book.name for book in self.books if book.is_available]
        if available_books:
            print(f"Available books in the library: {', '.join(available_books)}")

    






class Users:
    pass

