class BankAccount:
    """
    Represents a simple bank account with deposit, withdraw, and display balance functionalities.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        if initial_balance < 0:
            print("Initial balance cannot be negative. Setting to 0.")
            self.__account_balance = 0 # Using __ for name mangling (basic encapsulation)
        else:
            self.__account_balance = initial_balance # Using __ for name mangling (basic encapsulation)

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds or invalid amount).
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")