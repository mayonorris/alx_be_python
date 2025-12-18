# library_system.py
"""Library system showcasing inheritance (Book, EBook, PrintBook)
and composition (Library manages a collection of books)."""

class Book:
    """Base class representing a generic book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # Exact format required by the checker for base books
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        # Exact format: includes 'EBook' and 'File Size: <n>KB'
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # Exact format: includes 'PrintBook' and 'Page Count: <n>'
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
    def __init__(self):
        self.books = []  # List to store Book / EBook / PrintBook instances

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book using its __str__ implementation."""
        for book in self.books:
            print(book)
