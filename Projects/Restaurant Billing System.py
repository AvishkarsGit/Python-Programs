#Restaurant Billing system

# Create a dictionary of items and their prices
order = {
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

def print_menu():
    print("--------------------------------")
    print("\t  SHIVBA RESTAURANT ")
    print("--------------------------------")
    print("Item Name\t\tPrice(INR)")
    print("--------------------------------")
    for item,value in order.items():
        print(f"{item}\t\t\t {value:.2f}")
    print("--------------------------------")

tax_rate = 0.05

# Initialize the total cost and the list of items purchased
total_cost = 0.0
purchased_items = []

# Ask the user to input the items and their quantities
while True:
    print_menu()
    item = input("Enter the item you want to order (or 'done' to finish): ")
    if item == 'done':
        print("Your Order Placed Successfully..")
        break
    if item not in order:
        print("Item not found. Please try again.")
        continue
    try:
        quantity = int(input("Enter the quantity:"))
    except ValueError:
        print("Quantity could not be in decimal!! Please enter valid number")
        quantity = int(input("Enter the quantity:"))
    if quantity == 0:
        print('You have entered no quantity...')
        quantity = int(input("Enter the quantity: "))
    confirm = input("you want to confirm the order ?..(yes/no)")
    if confirm == 'yes':
        print("OK")
    elif confirm == 'no':
        quantity = int(input("Enter quantity again:"))
    else:
        print("Enter valid choice...")
    purchased_items.append((item, quantity))
    total_cost += order[item] * quantity

# Calculate the tax and the final cost
tax = total_cost * tax_rate
final_cost = total_cost + tax

# Print the bill
enter = input("Please enter '0' to print Bill invoice :")
if enter == '0':
    print("------------------------------------")
    print("\t\tBill Invoice")
    print("------------------------------------")
    print("ITEM NAME\t\tQTY\t\tTOTAL PRICE")
    print("------------------------------------")
    for item, quantity in purchased_items:
        print(f"{item.capitalize()}\t\t\t {quantity} \t \t {quantity * order[item]:.2f}")
    print("------------------------------------")
    print(f"Total cost\t\t\t\t {total_cost:.2f}")
    print(f"Tax\t\t\t\t\t\t {tax:.2f}")
    print("-------------------------------------")
    print(f"Final cost\t\t\t\t ₹{final_cost:.2f}/-")
    print("-------------------------------------")