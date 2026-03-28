# inventory_app.py

# Add product to inventory
def add_product(inventory, name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)


# Show all products
def show_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty\n")
        return

    for p in inventory:
        print(f"{p['name']} | {p['price']} | {p['quantity']}")
    print()


# Find product by name
def find_product(inventory, name):
    for p in inventory:
        if p["name"] == name:
            return p
    return None


# Update product
def update_product(inventory, name, new_price, new_quantity):
    product = find_product(inventory, name)

    if product:
        product["price"] = new_price
        product["quantity"] = new_quantity
        return True

    return False


# Delete product
def delete_product(inventory, name):
    product = find_product(inventory, name)

    if product:
        inventory.remove(product)
        return True

    return False


# Main function
def main():
    inventory = []
    running = True

    # Main loop
    while running:
        print("1. Add")
        print("2. Show")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        option = input("Select option: ")

        # Add
        if option == "1":
            try:
                name = input("Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                if price < 0 or quantity < 0:
                    print("Values must be non negative")
                else:
                    add_product(inventory, name, price, quantity)

            except:
                print("Invalid input")

        # Show
        elif option == "2":
            show_inventory(inventory)

        # Search
        elif option == "3":
            name = input("Name: ")
            product = find_product(inventory, name)
            print(product if product else "Not found")

        # Update
        elif option == "4":
            try:
                name = input("Name: ")
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))

                if price < 0 or quantity < 0:
                    print("Values must be non negative")
                else:
                    updated = update_product(inventory, name, price, quantity)
                    print("Updated" if updated else "Not found")

            except:
                print("Invalid input")

        # Delete
        elif option == "5":
            name = input("Name: ")
            deleted = delete_product(inventory, name)
            print("Deleted" if deleted else "Not found")

        # Exit
        elif option == "6":
            running = False

        else:
            print("Invalid option")


main()