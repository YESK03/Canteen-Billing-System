
A simple menu-driven **Python** program that prepares an itemized canteen bill, calculates the discount and tax automatically, and shows the final amount.

> **Course:** Python Programming (25BCA3C03) | **Activity 2:** Python Package Development
> **Department:** CS and IT, JAIN (Deemed-to-be University) | **Semester:** 3rd
> **Submitted to:** Dr. Ramkumar Krishnamoorthy

---

## Team Members

| S. No. | USN | Name |
|:------:|-----|------|
| 1 | 25BCAR0637 | Shuvam Kunwar |
| 2 | 25BCAR0548 | Srujan S Gowda |
| 3 | 25BCAR0493 | Shivam Kumar Gupta|

---

## Problem Statement

Prepare an itemized bill for a canteen, calculate tax and discount, and show the final amount.

## Features

- Shows a numbered **menu** of 8 canteen items with prices
- The user simply types the **item number** and **quantity**, and the item is added automatically
- Adding the same item again increases its quantity (no duplicate lines)
- **Automatic discount** based on the bill amount
- **5% tax** calculated on the amount after discount
- Prints a neat **itemized bill** with the final amount
- **Input validation:** wrong item number, letters instead of numbers, zero/negative quantity, and finishing with an empty bill are all handled

### Discount Rules

| Subtotal | Discount |
|----------|----------|
| Less than Rs. 200 | 0% |
| Rs. 200 or more | 5% |
| Rs. 500 or more | 10% |

**Calculation:**
```
discount     = subtotal x discount%
after_disc   = subtotal - discount
tax          = after_disc x 5%
final amount = after_disc + tax
```

---

## Project Structure

```
canteen-billing-system/
├── canteen_pkg/            # user-defined Python package
│   ├── __init__.py         # makes the folder a package, exposes the functions
│   └── ActualTask.py       # function definitions
├── main.py                 # executable program (run this file)
├── sample_output.txt       # sample run of the program
├── README.md
└── .gitignore
```

### Functions in `canteen_pkg/ActualTask.py`

| Function | Purpose |
|----------|---------|
| `show_menu()` | Prints the canteen menu |
| `add_item(bill, choice, quantity)` | Validates the choice and quantity, then adds the item to the bill |
| `apply_discount(subtotal)` | Returns `(discount percent, discount amount)` |
| `calculate_bill(bill)` | Returns `(subtotal, discount percent, discount, tax, final amount)` |
| `print_bill(bill)` | Prints the itemized bill |

---

## How to Run

**Requirements:** Python 3 installed. No extra libraries are needed.

```bash
# 1. Clone the repository
git clone https://github.com/YESK03/Canteen-Billing-System/tree/main

# 2. Go into the project folder
cd canteen-billing-system

# 3. Run the program
python main.py
```

(On some systems use `python3 main.py` instead.)

### How to use the program

1. The menu appears. Type the **item number** and press Enter.
2. Type the **quantity** and press Enter. The item is added.
3. Repeat for more items.
4. Type **`0`** to finish. The final bill is printed.

---

## Sample Output

```
------------ CANTEEN MENU ------------
1 - Tea  : Rs. 15
2 - Coffee  : Rs. 20
3 - Samosa  : Rs. 12
4 - Veg Sandwich  : Rs. 40
5 - Masala Dosa  : Rs. 60
6 - Veg Biryani  : Rs. 90
7 - Cold Coffee  : Rs. 50
8 - Fresh Juice  : Rs. 30
0 - Finish and print bill
--------------------------------------
Enter item number: 5
Enter quantity: 2
Added 2 x Masala Dosa
        ... (more items added) ...
Enter item number: 0

==============================================
                CANTEEN BILL
==============================================
Item               Price   Qty    Amount
----------------------------------------------
Masala Dosa           60    2      120
Veg Biryani           90    1       90
Tea                   15    3       45
----------------------------------------------
Subtotal                     : Rs. 255.00
Discount (5%)                : Rs. 12.75
Tax (5%)                     : Rs. 12.11
==============================================
FINAL AMOUNT                 : Rs. 254.36
==============================================
Thank you! Visit again.
Different items ordered: 3
```

A full test run (including invalid inputs) is saved in [`sample_output.txt`](sample_output.txt).

---

## Test Cases

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Normal bill, no discount | Tea x2 | Subtotal 30.00, discount 0%, tax 1.50, **final 31.50** |
| 2 | Bill with 5% discount | Masala Dosa x2, Veg Biryani x1, Tea x3 | Subtotal 255.00, discount 12.75, tax 12.11, **final 254.36** |
| 3 | Same item added twice | Tea x2, then Tea x3 | One line: Tea, quantity 5 |
| 4 | Edge: finish with empty bill | `0` before ordering | "You have not ordered anything yet!" |
| 5 | Invalid item number | `99` | "Invalid item number! Please choose from the menu." |
| 6 | Invalid text input | `abc` | "Please type a number only!" |
| 7 | Invalid quantity | `-2` | "Quantity must be 1 or more!" |

---

## Python Concepts Used

- **Unit 1:** `print`, `input`, `if/elif/else`, `while` and `for` loops, strings, functions
- **Unit 2:** lists (the bill), dictionaries (the menu), tuples (menu entries and multiple return values), sets (counting different items)
- **Unit 3:** exception handling (`try/except`)
- **Package development:** a user-defined package (`canteen_pkg`) with `__init__.py` and a module, imported in `main.py`

---

*Developed as part of Activity 2 - Python Package Development, JAIN (Deemed-to-be University).*
