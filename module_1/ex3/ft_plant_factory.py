#!/usr/bin/env python3
class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """
    plants = []

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
        self.age = age
        Plant.plants += [self]
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def total_plants() -> int:
        """
        Count total plants created
        :rtype: int
        """
        count = 0
        for plant in Plant.plants:
            count += 1
        print(f"Total plants created: {count}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print()
    Plant.total_plants()
