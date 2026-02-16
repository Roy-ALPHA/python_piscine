#!/usr/bin/env python3
import sys


def sort_dict(inventory) -> dict:

    items = list(inventory.values())
    items.sort(reverse=True)
    inventory_sorted = dict()

    i = 0
    while len(inventory_sorted) != len(inventory):

        for item, quantity in inventory.items():
            if item not in inventory_sorted.keys() and quantity == items[i]:
                inventory_sorted.update({item: quantity})

        i += 1

    return inventory_sorted


if len(sys.argv) < 2:
    print("Error: No arguments provided!")
    sys.exit(1)

inventory = dict()
for arg in sys.argv[1:]:

    if arg.count(":") != 1:
        print(
            f"Error: '{arg}' Invalid format!\n"
            "(expected KEY:VALUE)"
        )
        sys.exit(1)

    key, value = arg.split(":")

    key = key.strip(" ")
    value = value.strip(" ")

    try:
        value = int(value)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    inventory.update({key: value})

print("=== Inventory System Analysis ===")

total_items = sum(inventory.values())
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {len(set(inventory.keys()))}\n")

print("=== Current Inventory ===\n")
inventory_sorted = sort_dict(inventory)
for item, quantity in inventory_sorted.items():
    print(f"{item}: {quantity} units ({quantity / total_items * 100:.1f}%)")

print("\n=== Inventory Statistics ===")
for item, quantity in inventory_sorted.items():
    if quantity == max(inventory_sorted.values()):
        print(f"Most abundant: {item} ({quantity} "
              f"{"units" if quantity > 1 else "unit"})")
    elif quantity == min(inventory_sorted.values()):
        print(f"Least abundant: {item} ({quantity} "
              f"{"units" if quantity > 1 else "unit"})")
        break

print("\n=== Item Categories ===")

abundance = dict()
moderate = dict()
scarce = dict()

for item, quantity in inventory.items():
    if quantity < 4:
        scarce.update({item: quantity})
    elif quantity >= 5:
        moderate.update({item: quantity})

abundance.update({"Moderate": moderate})
abundance.update({"Scarce": scarce})

print(f"Moderate: {abundance.get('Moderate')}")
print(f"Scarce: {abundance.get('Scarce')}")

print("\n=== Management Suggestions ===")

restock_needed = list()
min_item = min(inventory.values())
for item, quantity in inventory.items():
    if quantity == min_item:
        restock_needed += [item]

print(f"Restock needed: {restock_needed}")

print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(inventory.keys())}")
print(f"Dictionary values: {list(inventory.values())}")
print(f"Sample lookup - 'sword' in inventory: "
      f"{"True" if "sword" in inventory.keys() else "False"}")
