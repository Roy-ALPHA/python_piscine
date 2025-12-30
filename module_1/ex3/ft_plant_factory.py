#!/usr/bin/env python3
from ex1.ft_garden_data import Plant
print("=== Plant Factory Output ===")
list_plants = [Plant("Rose", 25, 30), Plant("Oak", 200, 365), Plant("Cactus", 5, 90), Plant("Sanflower", 80, 45), Plant("Fern", 15, 120)]
for plant in list_plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
print("\nTotal plants created: 5")
