#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print (f"{self.name} is blooming beautifully!")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

class GardenManager:
    def __init__(self, garden, plants):
        self.garden = garden
        self.plants = plants

