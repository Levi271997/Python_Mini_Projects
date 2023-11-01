import os

# Function to display the menu
def display_menu():
    print("\nInventory System Menu:")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. List all items")
    print("4. Search for an item")
    print("5. Exit")

def add_item(inventory, item_name, quantity):
    inventory[item_name] = quantity

def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def list_items(inventory):
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} units")


def search_item(inventory, item_name):
    if item_name in inventory:
        print(f"{item_name}: {inventory[item_name]} units")
    else:
        print(f"{item_name} not found in the inventory.")

inventory_file = "inventory.txt"
inventory = {}

if os.path.exists(inventory_file):
    with open(inventory_file, "r") as file:
        for line in file:
            item, quantity = line.strip().split(":")
            inventory[item] = int(quantity)

while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        add_item(inventory, item_name, quantity)
    elif choice == "2":
        item_name = input("Enter the item name to remove: ")
        remove_item(inventory, item_name)
    elif choice == "3":
        list_items(inventory)
    elif choice == "4":
        item_name = input("Enter the item name to search for: ")
        search_item(inventory, item_name)
    elif choice == "5":
        # Save the inventory data to a file before exiting
        with open(inventory_file, "w") as file:
            for item, quantity in inventory.items():
                file.write(f"{item}:{quantity}\n")
        print("Inventory data saved. Exiting.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
