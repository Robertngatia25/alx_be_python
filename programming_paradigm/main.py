# main.py

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