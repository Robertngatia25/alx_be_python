class Book:
    """
    Represents a book with a title, author, and publication year.

    This class demonstrates the use of Python's magic methods:
    - __init__: for object initialization.
    - __del__: for object destruction (cleanup).
    - __str__: for informal, human-readable string representation.
    - __repr__: for official, unambiguous string representation that could
                recreate the object.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' by {self.author} created.") # Optional: confirm creation


    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed (garbage collected).
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")


    def __str__(self):
        """
        Returns the informal (user-friendly) string representation of the Book object.
        This is typically what you see when you print an object directly.

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"


    def __repr__(self):
        """
        Returns the official (unambiguous) string representation of the Book object.
        This string should ideally be a valid Python expression that could
        recreate the object. It's useful for debugging and development.

        Returns:
            str: A string in the format "Book('title', 'author', year)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

