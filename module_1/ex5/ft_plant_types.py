#!/usr/bin/env python
class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Height in centimeters.
        age (int): Age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The plant name.
            height (int): Height in centimeters.
            age (int): Age in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    """
    Represents a tree, which is a type of plant with a trunk diameter.
    """
    def __init__(self, name: str,
                 height: int, age: int, trunk_diameter: int) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): Tree name.
            height (int): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (int): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Display the amount of shade produced by the tree.
        """
        print(
            f"{self.name} provides {self.trunk_diameter * 1.56} "
            "square meters of shade"
            )


class Flower(Plant):
    """
    Represents a flowering plant with a color attribute.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): Flower name.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Display a message indicating the flower is blooming.
        """
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    """
    Represents a vegetable plant with harvest season and nutritional value.
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Vegetable name.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Season when the vegetable is harvested.
            nutritional_value (str): Main nutritional benefit.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self) -> None:
        """
        Display nutritional information about the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    tree = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 350, 1200, 40),
        ]
    flower = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 18, "yellow"),
        ]
    vegetable = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "spring", "vitamin A"),
        ]
    print(
        f"{flower[0].name} (Flower): "
        f"{flower[0].height}cm, {flower[0].age} days, "
        f"{flower[0].color} color"
        )
    flower[0].bloom()
    print()
    print(
        f"{tree[0].name} (Tree): "
        f"{tree[0].height}cm, {tree[0].age} days, "
        f"{tree[0].trunk_diameter}cm diameter"
        )
    tree[0].produce_shade()
    print()
    print(
        f"{vegetable[0].name} (Vegetable): "
        f"{vegetable[0].height}cm, {vegetable[0].age} days, "
        f"{vegetable[0].harvest_season} harvest"
        )
    vegetable[0].show_nutrition()
