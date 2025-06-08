# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    # Format the datetime object into a string
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date based on
    the current date, and prints it in YYYY-MM-DD format.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return # Exit the function if input is not an integer

    # Get the current date (without time for cleaner date calculation)
    # Alternatively, you could use datetime.now().date() if you only care about the date part
    current_datetime_for_future = datetime.now()
    
    # Calculate the future date using timedelta
    future_date = current_datetime_for_future + timedelta(days=days_to_add)
    
    # Format the future date to display only the date part
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    print("-" * 30) # Separator for clarity

    # Part 2
    calculate_future_date()