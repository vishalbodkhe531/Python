fruits = ["apple", "banana","apple", "mango", "orange", "grape","mango"]

unique_items = set()

for item in fruits:
    if item in unique_items:
        print(f"{item}")
    else:
        unique_items.add(item)