#!/usr/bin/env python3
def get_key(dic: dict, value: int) -> str:
    """
    Return the first key in the dictionary that has the given value.

    Parameters:
        dic (dict): The dictionary to search.
        value (int): The value to match.

    Returns:
        str: The key corresponding to the given value, or None if not found.
    """
    for item in dic:
        if dic.get(item) == value:
            return item


def fill_dics(moderate: dict, scarce: dict, dic: dict) -> None:
    """
    Categorize items into 'moderate' and 'scarce' based on quantity.

    Parameters:
        moderate (dict): Dictionary to store items with quantity > 3.
        scarce (dict): Dictionary to store items with quantity <= 3.
        dic (dict): Inventory dictionary to analyze.

    Returns:
        None: Updates moderate and scarce dictionaries in place.
    """
    for item in dic:
        if dic.get(item) <= 3:
            scarce.update({item: dic.get(item)})
        elif dic.get(item) > 3:
            moderate.update({item: dic.get(item)})


def restock_items(restock: list, dic: dict) -> list:
    """
    Identify items that need restocking (quantity 0 or 1).

    Parameters:
        restock (list): List to store items needing restock.
        dic (dict): Inventory dictionary to analyze.

    Returns:
        list: Updated restock list containing items with quantity 0 or 1.
    """
    for item in dic:
        if dic.get(item) == 1 or dic.get(item) == 0:
            restock += [item]
    return restock


print("=== Inventory System Analysis ===")
inventory = {
    "sword": 1,
    "potion": 5,
    "shield": 2,
    "armor": 3,
    "helmet": 1
}
total_items = sum(list(inventory.values()))
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {len(inventory)}\n")
print("=== Current Inventory ===")
print(
      f"potion: {inventory.get("potion")} units "
      f"({inventory.get("potion") / total_items * 100:.1f}%)"
      )
print(
      f"armor: {inventory.get("armor")} units "
      f"({inventory.get("armor") / total_items * 100:.1f}%)"
      )
print(
      f"shield: {inventory.get("shield")} units "
      f"({inventory.get("shield") / total_items * 100:.1f}%)"
      )
print(
      f"sword: {inventory.get("sword")} units "
      f"({inventory.get("sword") / total_items * 100:.1f}%)"
      )
print(
      f"helmet: {inventory.get("helmet")} units "
      f"({inventory.get("helmet") / total_items * 100:.1f}%)\n"
      )
print("=== Inventory Statistics ===")
values = list(inventory.values())
print(
    f"Most abundant: {get_key(inventory, max(values))} "
    f"({max(values)} {"unit" if max(values) == 1 else "units"})"
)
print(
    f"Least abundant: {get_key(inventory, min(values))} "
    f"({min(values)} {"unit" if min(values) == 1 else "units"})\n"
)
print("=== Item Categories ===")
moderate = dict()
scarce = dict()
fill_dics(moderate, scarce, inventory)
print(f"Moderate: {moderate}")
print(f"Scarce: {scarce}\n")
print("=== Management Suggestions ===")
restock = list()
print(f"Restock needed: {restock_items(restock, inventory)}\n")
print("=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(inventory.keys())}")
print(f"Dictionary values: {list(inventory.values())}")
print(
    "Sample lookup - 'sword' in inventory: "
    f"{"True" if "sword" in inventory.keys() else "False"}"
)
