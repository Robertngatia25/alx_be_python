class Book:
    """
    Represents a book in the library.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): True if the book is checked out, False otherwise.
                                (Private attribute for encapsulation)
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, a book is not checked out

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as available (returned).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book): # Optional: ensure only Book objects are added
            self._books.append(book)
            # print(f"Added '{book.title}' to the library.") # Optional confirmation
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                found = True
                break
            elif book.title == title and not book.is_available():
                print(f"'{title}' is already checked out.")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                found = True
                break
            elif book.title == title and book.is_available():
                print(f"'{title}' is already in the library (not checked out).")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book object
                available_found = True
        if not available_found:
            print("No books currently available.")