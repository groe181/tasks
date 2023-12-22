menu = ["coffee", "tea", "scone", "toastie"]

stock = {
    'coffee': 18,
    'tea': 22,
    'scone': 5,
    'toastie': 9
}

prices = {
    'coffee': 4,
    'tea': 3,
    'scone': 5,
    'toastie': 6
}

total_cost = 0

for item in menu:
    total_cost += stock[item] * prices[item]

print(f"The total cost is: £{total_cost}")

