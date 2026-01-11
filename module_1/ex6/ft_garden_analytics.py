#!/usr/bin/env python3
class Plant:
    """Represents a basic plant with name, height, and age."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = "regular"


class FloweringPlant(Plant):
    """Represents a flowering plant with color, inherits from Plant."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a FloweringPlant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
            age (int): Age of the plant in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color
        self.plant_type = "flower"


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flower with prize points, inherits from
        FloweringPlant."""
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        """
        Initialize a PrizeFlower instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
            age (int): Age of the plant in days.
            color (str): Color of the flower.
            prize_points (int): Prize points awarded to this flower.
        """
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.plant_type = "prize flower"


class GardenManager:
    """Manages a garden and its collection of plants."""
    gardens = []  # Class-level list tracking all gardens
    total_growth = 0  # Class-level total growth of all plants

    def add_garden(self, garden: str) -> None:
        """
        Assign a name to this garden.

        Args:
            garden (str): Name of the garden.
        """
        self.garden = garden

    def add_plant(self, plants: list, tba3: bool) -> None:
        """
        Add plants to the garden and optionally print info.

        Args:
            plants (list): List of Plant, FloweringPlant, or PrizeFlower
            instances.
            tba3 (bool): If True, prints info about added plants.
        """
        self.plants = plants
        if tba3 is True:
            for elem in self.plants:
                print(f"Added {elem.name} to {self.garden}'s garden")
        GardenManager.gardens += [self]

    def grow(self) -> None:
        """
        Grow all plants in the garden by 1cm and update total growth.
        """
        grew = 1
        tmp = 0
        print(f"{self.garden} is helping all plants grow...")
        for elem in self.plants:
            elem.height += grew
            tmp += grew
            print(f"{elem.name} grew {grew}cm")
        GardenManager.total_growth = tmp

    def height_valid(self) -> None:
        """
        Validate that all plant heights are non-negative.
        Prints the result.
        """
        valid = True
        for elem in self.plants:
            if elem.height < 0:
                valid = False
                break
        print("Height validation test: ", valid)

    def get_score(self) -> int:
        """
        Calculate the garden's score based on plant types.

        Returns:
            int: Total score of the garden.
        """
        score = 0
        for elem in self.plants:
            if elem.plant_type == "regular":
                score += 46
            elif elem.plant_type == "flower":
                score += 70
            else:
                score += 102
        return score

    @staticmethod
    def print_tt_gardens(count: int) -> None:
        """
        Print the total number of gardens managed.

        Args:
            count (int): Number of gardens.
        """
        print(f"Total gardens managed: {count}")

    @classmethod
    def create_garden_network(cls) -> None:
        """
        Class-level method to display scores for all gardens and total count.
        """
        count = 0
        print("Garden scores -", end=' ')
        for elm in cls.gardens:
            print(f"{elm.garden}: {cls.get_score(elm)}", end=', ')
            count += 1
        print()
        cls.print_tt_gardens(count)

    class GardenStats:
        """Helper class to provide statistics about a garden."""
        def __init__(self, inst) -> None:
            """
            Initialize GardenStats for a specific GardenManager instance.

            Args:
                inst (GardenManager): The garden instance to analyze.
            """
            self.obj = inst

        @staticmethod
        def get_list_len(li: list) -> int:
            """
            Utility method to count items in a list.

            Args:
                li (list): List of items.

            Returns:
                int: Number of items in the list.
            """
            count = 0
            for i in li:
                count += 1
            return count

        def total_plant(self) -> int:
            """
            Return the total number of plants in the garden.

            Returns:
                int: Number of plants.
            """
            return GardenManager.GardenStats.get_list_len(self.obj.plants)

        def get_types(self) -> None:
            """
            Print counts of each type of plant in the garden.
            """
            regular = 0
            flower = 0
            prize_flower = 0
            for elem in self.obj.plants:
                if elem.plant_type == "regular":
                    regular += 1
                elif elem.plant_type == "flower":
                    flower += 1
                else:
                    prize_flower += 1
            print(
                f"Plant types: {regular} regular, {flower} flowering, "
                f"{prize_flower} prize flowers"
                )

        def track_growth(self) -> int:
            """
            Return total growth for this garden session.

            Returns:
                int: Total growth in cm.
            """
            return GardenManager.total_growth

        def get_plant_status(self) -> None:
            """
            Print detailed status of all plants in the garden.
            """
            print("Plants in garden:")
            for elem in self.obj.plants:
                if elem.plant_type == "regular":
                    print(f" - {elem.name}: {elem.height}cm")
                elif elem.plant_type == "flower":
                    print(
                        f" - {elem.name}: {elem.height}cm, {elem.color} "
                        "flowers (blooming)"
                        )
                else:
                    print(
                        f" - {elem.name}: {elem.height}cm, {elem.color} "
                        f"flowers (blooming), Prize points: "
                        f"{elem.prize_points}"
                        )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    garden = GardenManager()
    garden.add_garden("Alic")
    garden.add_plant([
        Plant("Oak Tree", 100, 1500),
        FloweringPlant("Rose", 25, 30, "red"),
        PrizeFlower("Sunflower", 50, 45, "yellow", 10)], True)
    print()
    garden.grow()
    print()
    print(f"=== {garden.garden}'s Garden Report ===\n")
    stat = GardenManager.GardenStats(garden)
    stat.get_plant_status()
    print()
    print(
        f"Plants added: {stat.total_plant()}, "
        f"Total growth: {stat.track_growth()}cm"
        )
    stat.get_types()
    print()
    garden.height_valid()
    garden2 = GardenManager()
    garden2.add_garden("Bob")
    garden2.add_plant([
        Plant("Oak Tree", 100, 1500),
        Plant("Tree", 70, 300)
        ], False)
    GardenManager.create_garden_network()
