""" An Animal class representing a generic animal. The goaol is to demonstrate
inheritance in Python."""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden by subclasses

#Inheritance

class Lion(Animal):
    def speak(self, name):
        return f"{self.name} the lion roars!"
        
