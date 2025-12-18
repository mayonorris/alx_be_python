"""Define a base class Shape with a method area() and derived classes Rectangle and Circle, 
each overriding the area() method to calculate their respective areas.
"""

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        import math
        return math.pi * (self.radius ** 2)

        
