# book_class.py
"""Book class demonstrating __init__, __del__, __str__, and __repr__.

This class models a book with a title, author, and publication year, and
implements key magic methods for construction, destruction, and string
representations.
"""

class Book:
    # Constructor: initialize a new Book instance with required attributes.
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # User-friendly string: used by print() and str().
    # Must match: "<title> by <author>, published in <year>"
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
        
    # Official string: used by repr().
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # Destructor: called when the object is about to be destroyed.
    # Prints the required deletion message.
    def __del__(self):
        print(f"Deleting {self.title}")
