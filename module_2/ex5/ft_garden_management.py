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
    def __init__(self, name: str, height: int, age: int, sun: int,
                 water: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.sun = sun
        self.water = water


class GardenManager():
    """
    Manages garden operations such as adding plants,
    watering them, and checking their health.
    """
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
            elif pln.height < 0:
                raise PlantError(
                    "Error adding plant: Plant height can't be negtive!")
            elif pln.age < 0:
                raise PlantError(
                    "Error adding plant: Plant age can't be negtive!")
            else:
                print(f"Added {pln.name} successfully")
                self.plants += [pln]

    def water_plants(self) -> None:
        """
        Water all plants in the garden.

        Ensures cleanup using a finally block.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.name is None or not plant.name:
                    raise WaterError(
                        "Error: Cannot water None - invalid plant!")
                else:
                    print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        """
        Validate plant health parameters.

        Raises:
            HealthPlantError: If any health value is out of range.
        """
        if plant_name is None or not plant_name:
            raise HealthPlantError(f"Error checking {plant_name}: "
                                   "Plant name cannot be empty!")
        elif water_level > 10:
            raise HealthPlantError(f"Error checking {plant_name}: Water level "
                                   f"{water_level} is too high (max 10)")
        elif water_level < 1:
            raise HealthPlantError("Not enough water in tank")
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


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plants([Plant("tomato", 45, 67, 8, 5)])
        garden.add_plants([Plant("lettuce", 8, 2, 3, 15)])
        garden.add_plants([Plant("", 8, 67, 4, 7)])
    except PlantError as e:
        print(e)
    print()
    print("Watering plants...")
    try:
        garden.water_plants()
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
        garden.plants[0].water = 0
        garden.check_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")
