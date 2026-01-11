#!/usr/bin/env python3
class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self) -> None:
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increase the plant's age by 1 day.
        """
        self.plant_age += 1

    def get_info(self) -> None:
        """
        Print the current status of the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        ]
    print("=== Day 1 ===")
    plants[0].get_info()
    for elem in plants:
        i = 0
        while i < 6:
            elem.grow()
            elem.age()
            i += 1
    print("=== Day 7 ===")
    plants[0].get_info()
    print("Growth this week: +6cm")
