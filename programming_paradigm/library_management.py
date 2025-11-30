"""Library Management: Book and Library classes."""

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    """Manage a collection of books and their availability."""

    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Add a Book instance to the collection."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out the first available book matching title."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return True
        return False

    def return_book(self, title: str):
        """Return the first checked-out book matching title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all available books as '<title> by <author>'."""
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
