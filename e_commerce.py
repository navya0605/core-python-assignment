all_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500,
    'Monitor': 10000,
    'Charger': 1500
}
cart = {}

def add_to_cart(item):
    if item in all_items:
        cart[item] = all_items[item]
        print(f"{item} has been added to your cart.")
    else:
        print("Item not found")

def remove_from_cart(item):
    if item in cart:
        del cart[item]  # Correct way to remove an item from a dictionary
        print(f"{item} has been removed from your cart.")
    else:
        print("Item not found")

def show_cart():
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        for item, price in cart.items():
            print(f"{item}: {price}")

def total_price(cart):
    if len(cart) == 0:
        print("Cart is empty.")
        return 0

    total_price = sum(cart.values())
    if len(cart) > 5:
        discount_amount = total_price * 10 / 100
        total_price -= discount_amount

    return total_price

print("Welcome to the e-commerce store!")
print("We have these items available:")
for item, price in all_items.items():
    print(f"{item}: {price}")

while True:
    print("\n1. Add to cart")
    print("2. Remove from cart")
    print("3. Show cart")
    print("4. Total price")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    if choice == 1:
        item = input("Enter item to add: ")
        add_to_cart(item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        remove_from_cart(item)
    elif choice == 3:
        show_cart()
    elif choice == 4:
        print(f"Total price: {total_price(cart)}")
    elif choice == 5:
        print("Exiting the store. Thank you!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")
