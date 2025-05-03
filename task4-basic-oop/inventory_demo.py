"""
This script demonstrates importing the Product class from the product module
and using it to create a product object, set its price and quantity,
and display its information.
"""

from product import Product

def main():
    # Ask user for product information
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        
        # Create a Product object
        product = Product(name, price, quantity)
        
        # Display product information
        product.display_info()
        
        # Option one: Add inventory
        add = int(input("Enter amount to add to inventory: "))
        product.add_inventory(add)
        product.display_info()
        
        # Option two: Remove inventory
        remove = int(input("Enter amount to remove from inventory: "))
        product.remove_inventory(remove)
        product.display_info()
    except ValueError as e:
        print(f"Error: Invalid input. Please enter the correct data type. Details: {e}")

# Call the main function
if __name__ == "__main__":
    main()