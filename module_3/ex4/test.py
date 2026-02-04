import sys


if len(sys.argv) < 1:
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
print(f"Total items in inventory: {sum(inventory.values())}")
print(f"Unique item types: {len(set(inventory.keys()))}\n")

print("=== Current Inventory ===\n")
