#!/usr/bin/env python3
class GardenError(Exception):
    """
    Base exception class for all garden-related errors.

    This class allows catching all garden-specific problems
    with a single exception type.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related problems.

    Inherits from GardenError so it can be caught
    either specifically or as a general garden error.
    """
    pass


class HealthPlantError(GardenError):
    """
    Raised when a plant's health parameters
    (water or sunlight) are invalid.
    """
    pass


class WaterError(GardenError):
    """
    Exception raised for watering-related problems.

    Inherits from GardenError so it can be caught
    either specifically or as a general garden error.
    """
    pass


class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant
        height (int): Height of the plant
        age (int): Age of the plant
        sun (int): Daily sunlight hours
        water (int): Water level
    """
    def __init__(self, name: str, sun: int, water: int) -> None:
        self.name = name
        self.sun = sun
        self.water = water


class GardenManager():
    """
    Manages garden operations such as adding plants,
    watering them, and checking their health.
    """
    water_in_tank = 2

    def __init__(self):
        """Initialize an empty garden."""
        self.plants = []

    def add_plants(self, plant: list) -> None:
        """
        Add plants to the garden.

        Raises:
            PlantError: If plant data is invalid.
        """
        for pln in plant:
            if pln.name is None or not pln.name:
                raise PlantError(
                    "Error adding plant: Plant name cannot be empty!")
            else:
                print(f"Added {pln.name} successfully")
                self.plants += [pln]

    def water_plants(self, print_er: bool) -> None:
        """
        Water all plants in the garden.

        Ensures cleanup using a finally block.
        """
        if print_er:
            print("Opening watering system")
        try:
            for plant in self.plants:
                if GardenManager.water_in_tank == 0:
                    raise WaterError(
                        "Not enough water in tank")
                else:
                    print(f"Watering {plant.name} - success")
                    GardenManager.water_in_tank -= 1
        finally:
            if print_er:
                print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        """
        Validate plant health parameters.

        Raises:
            HealthPlantError: If any health value is out of range.
        """
        if water_level > 10:
            raise HealthPlantError(f"Error checking {plant_name}: Water level "
                                   f"{water_level} is too high (max 10)")
        elif water_level < 1:
            raise HealthPlantError(f"Error checking {plant_name}: Water level "
                                   f"{water_level} is too low (max 1)")
        elif sunlight_hours > 12:
            raise HealthPlantError(
                f"Error checking {plant_name}: Sunlight hours {sunlight_hours}"
                " is too high (max 12)"
                )
        elif sunlight_hours < 2:
            raise HealthPlantError(f"Error checking {plant_name}: Sunlight "
                                   f"hours {sunlight_hours} is too low (min 2)"
                                   )
        else:
            print(f"{plant_name}: healthy (water: "
                  f"{water_level}, sun: {sunlight_hours})")

    def check_health(self) -> None:
        """
        Check health for all plants in the garden.
        """
        for plant in self.plants:
            GardenManager.check_plant_health(plant.name,
                                             plant.water, plant.sun)


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plants(
            [Plant("tomato", 8, 5),
             Plant("lettuce", 3, 15),
             Plant("", 4, 7)])
    except PlantError as e:
        print(e)
    print()
    print("Watering plants...")
    try:
        garden.water_plants(True)
    except WaterError as e:
        print(e)
    print()
    print("Checking plant health...")
    try:
        garden.check_health()
    except HealthPlantError as e:
        print(e)
    print()
    print("Testing error recovery...")
    try:
        garden.water_plants(False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
