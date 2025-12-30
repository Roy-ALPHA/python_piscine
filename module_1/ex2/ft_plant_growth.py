#!/usr/bin/env python3
from ex1.ft_garden_data import Plant
def grow(plant, x):
    plant.height += x
def age(plant, x):
    plant.age += x
def get_info(plant):
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]
print("=== Day 1 ===")
print(f"{plants[0].name}: {plants[0].height}cm, {plants[0].age} days old")
for elem in plants:
    grow(elem, 6)
    age(elem, 6)
print("=== Day 7 ===")
get_info(plants[0])
print("Growth this week: +6cm")