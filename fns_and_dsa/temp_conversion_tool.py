# temp_conversion_tool.py

# Define Global Conversion Factors
# These variables are defined outside any function, making them global.
# They can be accessed (read) from anywhere in the script, including inside functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    # No 'global' keyword needed as we are only reading its value.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    # No 'global' keyword needed as we are only reading its value.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input) # Convert input to a float

    except ValueError:
        # If conversion to float fails, raise an error as per requirement
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt user for unit (C/F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    # This block ensures main() is called only when the script is executed directly
    # and not when it's imported as a module into another script.
    main()