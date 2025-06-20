# library_system.py

class Book:
    """
    Base class representing a generic book with a title and an author.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a human-readable string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds a file_size attribute.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a human-readable string representation of the EBook,
        including its file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and adds a page_count attribute.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a human-readable string representation of the PrintBook,
        including its page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class representing a library, demonstrating composition by
    managing a collection of various types of books.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to store books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (can be Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        self.books.append(book)
       # print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
      #  print("\n--- Books in the Library ---")
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                # The __str__ method of each book object will be automatically called here
                print(book)
 #       print("----------------------------")

