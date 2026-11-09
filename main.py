# main.py - Canteen Billing System
# Run this file:  python main.py

from canteen_pkg import MENU, show_menu, add_item, print_bill

print("###### WELCOME TO THE COLLEGE CANTEEN ######")

bill = []              # list that stores the ordered items
ordered_items = set()  # set of different items ordered (no repeats)

while True:
    show_menu()

    # Step 1: ask the item number (try/except handles letters like "abc")
    try:
        choice = int(input("Enter item number: "))
    except ValueError:
        print("Please type a number only!")
        continue

    # 0 means the customer has finished ordering
    if choice == 0:
        if len(bill) == 0:
            print("You have not ordered anything yet!")
            continue
        break

    # Wrong item number -> ask again from the menu
    if choice not in MENU:
        print("Invalid item number! Please choose from the menu.")
        continue

    # Step 2: ask the quantity
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please type a number only!")
        continue

    # Step 3: add the item automatically
    message = add_item(bill, choice, quantity)
    print(message)
    if message.startswith("Added"):
        ordered_items.add(choice)

# Show the final bill
print_bill(bill)
print("Different items ordered:", len(ordered_items))
