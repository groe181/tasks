"""This program calculates the stock value in a cafe."""

#Create a list with the items the cafe has in stock.
#Create a dictionary which shows how much stock each item has.
#Create a dictionary which shows the value of each menu item.
#Loop through the items in the menu, calculating the stock value of each item,
#and adding this to a running total.
#Print this cost back to the user.


MENU = ["coffee", "tea", "scone", "toastie"]

STOCK = {
    'coffee': 18,
    'tea': 22,
    'scone': 5,
    'toastie': 9
}

PRICES = {
    'coffee': 4,
    'tea': 3,
    'scone': 5,
    'toastie': 6
}

total_cost = 0
for item in MENU:
    total_cost += STOCK[item] * PRICES[item]

print(f"The total cost is: £{total_cost}")
