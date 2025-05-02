class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must great than zero")
        self.quantity = quantity

    def add_inventory(self, amount):
        if amount < 0:
            raise ValueError("Amount to add great than zero")
        self.quantity += amount

    def remove_inventory(self, amount):
        if amount < 0:
            raise ValueError("Amount to remove cannot be negative")
        if amount > self.quantity:
            raise ValueError("insuficient inventory amount")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f" Price: {self.price}")
        print(f" Quantity: {self.quantity}")
        print(f"Total Value: {self.total_value()}")

        #ask use to product inform
try:
    name=input("Enter product name: ")
    price=float(input("Enter product price: "))
    quantity=int(input("Enter product quantity: "))
    
    product=Product(name, price, quantity)
    product.display_info()
    # option one add
    add=int(input("Enter amount to add to inventory: "))
    product.add_inventory(add)
    product.display_info()
    # option two remove

    remove=int(input("Enter amount to remove from inventory: "))
    product.remove_inventory(remove)
    product.display_info()
except ValueError as e:
    print(f"ValueError: {e}")
