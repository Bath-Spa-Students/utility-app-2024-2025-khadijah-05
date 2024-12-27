class Item:
    # Constructor to initialize item details.
    def __init__(self, no, code, items, price):
        self.no = no
        self.code = code
        self.name = items
        self.price = float(price)


# Defining a nested dictionary containing for snacks and drinks.
items = {
    "snacks": [
        Item("01", "FOX6601", "Cheetos", 4.50),
        Item("02", "FOX6602", "Doritos", 4.50),
        Item("03", "FOX6603", "Takis", 5.00),
        Item("04", "FOX6604", "Pringles", 7.50),
        Item("05", "FOX6605", "Snickers", 4.50),
        Item("06", "FOX6606", "Kitkat", 4.00),
        Item("07", "FOX6607", "Chocolate Chip Cookies", 4.00),
        Item("08", "FOX6608", "Oreo", 2.00),
        Item("09", "FOX6609", "Pistachios", 1.50),
        Item("10", "FOX6610", "Cashew", 1.50),
    ],
    "drinks": [
        Item("01", "FOX6701", "Bottle Water", 1.00),
        Item("02", "FOX6702", "Coca-Cola", 3.00),
        Item("03", "FOX6703", "Red Bull", 9.50),
        Item("04", "FOX6704", "Monster", 9.00),
        Item("05", "FOX6705", "Gatorade", 5.00),
        Item("06", "FOX6706", "Lipton", 4.50),
        Item("07", "FOX6707", "Cocktail Juice", 2.00),
        Item("08", "FOX6708", "Chocolate Milk", 2.50),
        Item("09", "FOX6709", "Strawberry Milk", 2.50),
        Item("10", "FOX6710", "Sparkling Water", 5.00),
    ]
}

# Displaying the items of the vending machine.
print("--- Welcome to Khadeeja's Python Vending Machine ---")

for category, item_list in items.items():
    print(f"---------------------- {category.capitalize()} -----------------------")
    print("No   | Code     | Items                       | Price")
    print("-----|----------|-----------------------------|------")
    for item in item_list:
        print(f"{item.no:<4} | {item.code:<8} | {item.name.ljust(27)} | ${item.price:.2f}")
    print()

# Initializing the user's balance.
balance = 0

# Allowing the user to load balance into the vending machine.
response = "yes"

while response.lower() != "no":
    try:
        loaded = float(input("Enter the your amount to load: $"))
        if loaded > 0:
            balance += loaded
            print(f"${loaded:.2f} has been added to your account. \nYour current balance is ${balance:.2f}.")
        else:
            print("Please enter a positive amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    response = input("Do you want to add more money? (yes/no): ").strip().lower()


# Allowing the user to select an item.
while True:
    selected_item_code = input("Enter the item's code: ").strip()
    item_found = None

    # Searching for the selected item in both categories.
    for category, item_list in items.items():
        for item in item_list:
            if item.code == selected_item_code:
                item_found = item
                break
        if item_found:
            break

    if not item_found:
        print("Selected item code is invalid, try again!")
        continue

    selected_item = item_found

    # Checking if the user has sufficient balance.
    if balance >= selected_item.price:
        print(f"Your item is {selected_item.name} (Price: ${selected_item.price:.2f}).")
        balance -= selected_item.price
        print(f"Your current balance is ${balance:.2f}.")
    else:
        print("You have insufficient balance!")

    another_purchase = input("Do you want to purchase another item? (yes/no): ").strip().lower()
    if another_purchase != "yes":
        break

# Displaying remaining balance.
print(f"Your remaining balance is ${balance:.2f}. Thank you for using the Khadeeja's Python Vending Machine!")