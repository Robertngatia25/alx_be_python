import sys
from bank_account import BankAccount

def main():
    # Example starting balance for the account
    # You can change this for your testing scenarios
    account = BankAccount(100) 

    # Check if enough command-line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>") # Corrected script name in usage
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and amount from command line arguments
    # sys.argv[1] would be something like "deposit:50" or "display"
    command_arg = sys.argv[1]
    
    # Split the command and parameters by ':'
    parts = command_arg.split(':')
    command = parts[0].lower() # Convert command to lowercase for consistent checking
    
    amount = None
    if len(parts) > 1: # Check if an amount part exists
        try:
            amount = float(parts[1])
        except ValueError:
            print("Error: Amount must be a numeric value.")
            sys.exit(1)

    # Perform the requested operation
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}") # Format output for consistency
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}") # Format output for consistency
        else:
            print("Insufficient funds.")
    elif command == "display" and amount is None: # Display command should not have an amount
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()