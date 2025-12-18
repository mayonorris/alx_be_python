# polymorphism_demo.py
"""Polymorphism via method overriding: Shape -> Rectangle, Circle."""

import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Compute area. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Rectangle with length and width."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Circle with radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)