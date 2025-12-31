#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = "regular"

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.plant_type = "flower"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.plant_type = "prize flower"

class GardenManager:
    count_garden = 0

    def add_garden(self, garden):
        self.garden = garden
        GardenManager.count_garden += 1

    def add_plant(self, plants):
        self.plants = plants
        for elem in self.plants:
            print(f"Added {elem.name} to {self.garden}'s garden")

    @classmethod
    def total_garden(cls):
            print(f"Total gardens managed: {GardenManager.count_garden}")

    def grow(self):
        print (f"{self.garden} is helping all plants grow...")
        for elem in self.plants:
            elem.height += 1
            print(f"{elem.name} grew 1cm")

    def height_valid(self):
        valid = True
        for elem in self.plants:
            if elem.height < 0:
                valid = False
                break
        print("Height validation test: ", valid)

    def get_score(self):
        score = 0
        for elem in self.plants:
            if elem.plant_type == "regular":
                score += 46
            elif elem.plant_type == "flower":
                score += 70
            else:
                score += 102
        return score

    class GardenStats:
        def get_list_len(plants):
            count = 0
            for i in plants:
                count += 1
            return count

        def total_plant(self):
            return GardenManager.GardenStats.get_list_len(self.plants)

        def get_types(self):
            regular = 0
            flower = 0
            prize_flower = 0
            for elem in self.plants:
                if elem.plant_type == "regular":
                    regular += 1
                elif elem.plant_type == "flower":
                    flower += 1
                else:
                    prize_flower += 1
            print(f"Plant types: {regular} regular, {flower} flowering, {prize_flower} prize flowers")

        def get_plant_status(self):
            print("Plants in garden:")
            for elem in self.plants:
                if elem.plant_type == "regular":
                    print (f" - {elem.name}: {elem.height}cm")
                elif elem.plant_type == "flower":
                    print (f" - {elem.name}: {elem.height}cm, {elem.color} flowers (blooming)")
                else:
                    print (f" - {elem.name}: {elem.height}cm, {elem.color} flowers (blooming), Prize points: {elem.prize_points}")

print ("=== Garden Management System Demo ===")
print()
garden = GardenManager()
garden.add_garden("Alic")
garden.add_plant([Plant("Oak Tree", 100, 1500), FloweringPlant("Rose", 25, 30, "red"), PrizeFlower("Sunflower", 50, 45, "yellow", 10)])
print()
garden.grow()
print()
print(f"=== {garden.garden}'s Garden Report ===")
GardenManager.GardenStats.get_plant_status(garden)
print()
print(f"Plants added: {GardenManager.GardenStats.total_plant(garden)}, Total growth: {GardenManager.GardenStats.total_plant(garden)}cm")
GardenManager.GardenStats.get_types(garden)
print()
garden.height_valid()
test = GardenManager()
test.add_garden("youness")
test.add_plant([Plant("Oak Tree", 100, 1500), Plant("Tree", 70, 300,)])
print()
print(f"Garden scores - {garden.garden}: {garden.get_score()}, {test.garden}: {test.get_score()}")
GardenManager.total_garden()