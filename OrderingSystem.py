class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_total(self):
        return self.menu_item.price * self.quantity

class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, order_item):
        self.order_items.append(order_item)

    def remove_item(self, order_item):
        self.order_items.remove(order_item)

    def calculate_total(self):
        total = 0
        for order_item in self.order_items:
            total += order_item.calculate_total()
        return total

    def display_order(self):
        print("Order:")
        for index, order_item in enumerate(self.order_items, start=1):
            print(f"{index}. {order_item.menu_item.name} x{order_item.quantity}")
        print(f"Total: ${self.calculate_total():.2f}")

def display_menu(menu):
    print("Menu:")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item.name} - ${item.price:.2f}")

def main():
    menu = [
        MenuItem("Burger", 5.99),
        MenuItem("Pizza", 8.99),
        MenuItem("Fries", 2.49),
        MenuItem("Soda", 1.99)
    ]

    current_order = Order()

    while True:
        display_menu(menu)
        choice = input("Enter the item number to add to your order (0 to finish): ")

        if choice == '0':
            break
        elif choice.isdigit():
            item_number = int(choice)
            if 1 <= item_number <= len(menu):
                quantity = int(input("Enter the quantity: "))
                menu_item = menu[item_number - 1]
                order_item = OrderItem(menu_item, quantity)
                current_order.add_item(order_item)
                print(f"{quantity} {menu_item.name}(s) added to your order.")
            else:
                print("Invalid item number. Please try again.")
        else:
            print("Invalid input. Please enter a valid item number or 0 to finish.")

    current_order.display_order()
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
