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
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        ]
    print("=== Garden Plant Registry ===")
    for elem in plants:
        print(f"{elem.name}: {elem.height}cm, {elem.age} days old")
