#!/usr/bin/env python
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter * 1.56} square meters of shade")
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print (f"{self.name} is blooming beautifully!")
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
print("=== Garden Plant Types ===\n")
tree = [Tree("Oak", 500, 1825, 50), Tree("Pine", 350, 1200, 40)]
flower = [Flower("Rose", 25, 30, "red"), Flower("Tulip", 20, 18, "yellow")]
vegetable = [Vegetable("Tomato", 80, 90, "summer", "vitamin C"), Vegetable("Carrot", 30, 70, "spring", "vitamin A")]
print(f"{flower[0].name} (Flower): {flower[0].height}cm, {flower[0].age} days, {flower[0].color} color")
flower[0].bloom()
print()
print(f"{tree[0].name} (Tree): {tree[0].height}cm, {tree[0].age} days, {tree[0].trunk_diameter}cm diameter")
tree[0].produce_shade()
print()
print(f"{vegetable[0].name} (Vegetable): {vegetable[0].height}cm, {vegetable[0].age} days, {vegetable[0].harvest_season} harvest")
vegetable[0].show_nutrition()