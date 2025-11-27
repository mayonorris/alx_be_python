""" Create a Product catalog  class with a method to display product details """
class ProductCatalog:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display_product_details(self):
        print(f"Product: {self.product_name}, Price: ${self.price}, Quantity: {self.quantity}")
# create an instance and call the method
p = ProductCatalog("Laptop", 999.99, 10)
p.display_product_details()