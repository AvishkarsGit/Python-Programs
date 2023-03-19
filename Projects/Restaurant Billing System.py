import re

menu = {
    "pizza": 260,
    "burger": 160,
    "fries": 80,
    "salad": 50,
    "soda": 20,
    "water": 15,
    "coffee":40,
    "roll":70,
    "momos":80
}

orders = {}
update_order = []

def display_menu():
    print("--------------------------------")
    print("\t  SHIVBA RESTAURANT ")
    print("--------------------------------")
    print("Item Name\t\tPrice(INR)")
    print("--------------------------------")
    for item,value in menu.items():
        print(f"{item}\t\t\t {value:.2f}")
    print("--------------------------------")

def add_to_order():
    while True:
        item = input("Enter an item to add to your order (or 'done' to finish): ").lower()
        if item == 'done':
            break
        try:
            if not item:
                raise ValueError("No input provided")
        except ValueError:
            print("No input Provided")
            continue
        try:
            if not re.match("^[a-zA-Z_]*$", item):
                raise ValueError("Input cannot contain special characters")
        except ValueError:
            print("Input cannot contain special characters")
            continue
        try:
            if item not in menu:
                raise ValueError("this item is not in the menu list!!")
        except ValueError:
            print("this item is not in the menu list!!")
            continue
        try:
            quantity = int(input("Enter the quantity:"))
        except ValueError:
            print("Error! please don't enter point/decimal value")
            quantity = int(input("Enter the quantity:"))
        if quantity == 0:
            print("You have entered no quantity...")
            quantity = int(input("Enter the quantity:"))
        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity
        print(f"Added {quantity} {item} to your order.")

def update_order():
    while True:
        item = input("Enter an item to update (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item not in orders:
            print("Sorry, that item is not in your order.")
            continue
        quantity = int(input("Enter the new quantity: "))
        orders[item] = quantity
        print(f"Updated {item} to {quantity}.")

def view_order():
    total = 0
    if not orders:
        print("Your order is empty.")
        return
    print("------------------------------------")
    print("\t\tBill Invoice")
    print("------------------------------------")
    print("ITEM NAME\t\tQTY\t\tTOTAL PRICE")
    print("------------------------------------")
    for item, quantity in orders.items():
        price = menu[item] * quantity
        print(f"{item.title()}\t\t\t {quantity} \t \t{price:.2f}")
        total += price
    print("-------------------------------------")
    print(f"TOTAL\t\t\t\t    {total:.2f}/-")
    print("-------------------------------------")

def main():
    while True:
        print()
        print("Options:")
        print("1. Display Menu")
        print("2. Add to Order")
        print("3. Update Order")
        print("4. View Order")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            add_to_order()
        elif choice == '3':
            update_order()
        elif choice == '4':
            view_order()
        elif choice == '5':
            print("Thanks for using our software!...")
            exit()
        else:
            print("Invalid choice.")

main()
