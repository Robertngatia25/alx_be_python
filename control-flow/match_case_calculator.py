# match case calculator 

# match_case_calculator.py

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero!"
            else:
                return num1 / num2
        case _:
            return "Invalid operation!"

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        result = calculate(num1, num2, operation)
        print(f"The result is {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")