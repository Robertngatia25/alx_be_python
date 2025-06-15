# main.py
'''
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]   # Get numerator as string from command line
    denominator = sys.argv[2] # Get denominator as string from command line

    result = safe_divide(numerator, denominator) # Call the safe_divide function
    print(result) # Print the result or error message returned by safe_divide

if __name__ == "__main__":
    main()
    '''
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald")) # Added for more robust testing

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n--- Checking out '1984' ---")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    print("\n--- Attempting to check out '1984' again (should be unavailable) ---")
    library.check_out_book("1984")

    print("\n--- Attempting to check out a non-existent book ('Moby Dick') ---")
    library.check_out_book("Moby Dick")

    # Simulate returning a book
    print("\n--- Returning '1984' ---")
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    print("\n--- Attempting to return 'Brave New World' (should already be in library) ---")
    library.return_book("Brave New World")

    print("\n--- Attempting to return a non-existent book ('The Hobbit') ---")
    library.return_book("The Hobbit")


if __name__ == "__main__":
    main()