class Calculator:
    """
    A simple Calculator class demonstrating the use of static methods and class methods.
    """

    # Class attribute accessible by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method that returns the sum of two numbers.
        Static methods do not receive an implicit first argument (like self or cls).
        They behave like regular functions but are part of the class's namespace.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method that returns the product of two numbers.
        Class methods receive the class itself as the first implicit argument (cls).
        This allows them to access and modify class-level attributes.

        Args:
            cls: The class itself (Calculator in this case).
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        # Accessing the class attribute 'calculation_type' using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

