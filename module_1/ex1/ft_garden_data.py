#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]
print("=== Garden Plant Registry ===")
for elem in plants:
    print(f"{elem.name}: {elem.height}cm, {elem.age} days old")