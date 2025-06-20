import math

class Shape:
    """
    Base class for geometric shapes.
    Defines an 'area' method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Overrides the 'area' method to calculate the rectangle's area.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (length * width).
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Overrides the 'area' method to calculate the circle's area.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle (π * radius^2).
        """
        return math.pi * (self.radius ** 2)

