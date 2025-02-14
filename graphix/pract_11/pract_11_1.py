class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return f"{self.title} has now been borrowed"
        else:
            return f"{self.title} is currently unavailable"

    def return_book(self):
        if not self.available:
            self.available = True
            return f"{self.title} has now been returned"
        else:
            return f"{self.title} has already been returned"

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class DigitalBook(Book):

    def __init__(self, title, author, isbn, compatibility=None):
        super().__init__(title, author, isbn)
        self.compatibility = compatibility or {'Kindle'}

    def borrow_book(self):
        # Digital books don't change availability upon borrowing
        return f"{self.title} has been borrowed (no change in availability)"

    def return_book(self):
        # Digital books don't change availability upon returning
        return f"{self.title} has been returned (no change in availability)"

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Compatibility: {', '.join(self.compatibility)}"


class Library:

    books = []

    def __init__(self):
        pass

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow_book()
        return f"Book with title {title} not found in the library"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return f"Book with title {title} not found in the library"

    def __str__(self):
        return "\n".join(str(book) for book in self.books)


# Test Functions

def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    print(book)
    print(book.borrow_book())
    print(book.return_book())
    print(book.return_book())  # Attempt to return again


def test_digital_book():
    digital_book = DigitalBook('Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    print(digital_book)
    print(digital_book.borrow_book())
    print(digital_book.return_book())


def test_library():
    # Create a Library instance
    library = Library()

    # Add Books and DigitalBooks to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"))
    library.add_book(Book("1984", "George Orwell", "978-0451524935"))
    library.add_book(Book("Jane Eyre", "Charlotte Bronte", "978-0141441146"))
    library.add_book(DigitalBook("Orlando: A Biography", "Virginia Woolf", "978-0156031516"))

    # Print library details
    print("Library contents:")
    print(library)

    # Borrowing and Returning books
    print("\nTrying to borrow '1984' (physical book):")
    print(library.borrow_book("1984"))


    print("\nLibrary contents after actions:")
    print(library)


# Running the test functions
test_book()
test_digital_book()
test_library()
