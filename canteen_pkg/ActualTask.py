# ActualTask.py - functions for the Canteen Billing System
# Topics used: dictionary, list, tuple (return value), functions, if/else, loops

# Canteen menu: item number -> (item name, price)   [dictionary of tuples]
MENU = {
    1: ("Tea", 15),
    2: ("Coffee", 20),
    3: ("Samosa", 12),
    4: ("Veg Sandwich", 40),
    5: ("Masala Dosa", 60),
    6: ("Veg Biryani", 90),
    7: ("Cold Coffee", 50),
    8: ("Fresh Juice", 30),
}

TAX_PERCENT = 5   # tax is 5% of the amount after discount


def show_menu():
    """Print the canteen menu on the screen."""
    print("\n------------ CANTEEN MENU ------------")
    for number in MENU:
        name, price = MENU[number]          # tuple assignment
        print(number, "-", name, " : Rs.", price)
    print("0 - Finish and print bill")
    print("--------------------------------------")


def add_item(bill, choice, quantity):
    """Add the chosen menu item to the bill (a list).
    Returns a message telling what happened."""
    # Validation 1: item number must be on the menu
    if choice not in MENU:
        return "Invalid item number! Please choose from the menu."

    # Validation 2: quantity must be at least 1
    if quantity <= 0:
        return "Quantity must be 1 or more!"

    name, price = MENU[choice]

    # If the item is already in the bill, just increase its quantity
    for line in bill:
        if line[0] == name:
            line[2] = line[2] + quantity
            return "Added " + str(quantity) + " more " + name

    # Otherwise add a new line: [name, price, quantity]
    bill.append([name, price, quantity])
    return "Added " + str(quantity) + " x " + name


def apply_discount(subtotal):
    """Automatic discount based on the subtotal.
    Returns a tuple: (discount percent, discount amount)."""
    if subtotal >= 500:
        percent = 10
    elif subtotal >= 200:
        percent = 5
    else:
        percent = 0

    amount = subtotal * percent / 100
    return percent, amount


def calculate_bill(bill):
    """Calculate the bill.
    Returns a tuple: (subtotal, discount percent, discount, tax, final amount)."""
    subtotal = 0
    for line in bill:
        subtotal = subtotal + line[1] * line[2]      # price * quantity

    percent, discount = apply_discount(subtotal)
    after_discount = subtotal - discount
    tax = after_discount * TAX_PERCENT / 100
    final_amount = after_discount + tax

    return subtotal, percent, discount, tax, final_amount


def print_bill(bill):
    """Print the itemized bill with discount, tax and final amount."""
    subtotal, percent, discount, tax, final_amount = calculate_bill(bill)

    print("\n==============================================")
    print("                CANTEEN BILL")
    print("==============================================")
    print("Item               Price   Qty    Amount")
    print("----------------------------------------------")
    for line in bill:
        name = line[0]
        price = line[1]
        qty = line[2]
        print(name.ljust(18), str(price).rjust(5), str(qty).rjust(4),
              str(price * qty).rjust(8))
    print("----------------------------------------------")
    print("Subtotal".ljust(28), ": Rs.", format(subtotal, ".2f"))
    print(("Discount (" + str(percent) + "%)").ljust(28), ": Rs.", format(discount, ".2f"))
    print(("Tax (" + str(TAX_PERCENT) + "%)").ljust(28), ": Rs.", format(tax, ".2f"))
    print("==============================================")
    print("FINAL AMOUNT".ljust(28), ": Rs.", format(final_amount, ".2f"))
    print("==============================================")
    print("Thank you! Visit again.")
