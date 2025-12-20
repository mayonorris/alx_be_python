""" define a class Calculator that includes both a class method and a static method to perform calculations. This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, 
highlighting their differences and practical applications.
class_static_methods_demo.py"""

class Calculator:
    calculation_type = "Arithmetic Operations"
    
    @classmethod
    def add(cls, a, b):
        """Class method to add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers."""
        return a * b