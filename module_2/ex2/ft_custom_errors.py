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


class WaterError(GardenError):
    """
    Exception raised for watering-related problems.

    Inherits from GardenError so it can be caught
    either specifically or as a general garden error.
    """
    pass


def check_water(water: int) -> None:
    """
    Check if there is enough water available.

    Args:
        water (int): Amount of water available.

    Raises:
        WaterError: If the water amount is zero or negative.
    """
    if water <= 0:
        raise WaterError("Not enough water in the tank!")


def check_wilting(plant: str, last_day_for_irrigation: int) -> None:
    """
    Check if a plant is wilting due to lack of irrigation.

    Args:
        plant (str): Name of the plant.
        last_day_for_irrigation (int): Days since last irrigation.

    Raises:
        PlantError: If the plant has not been irrigated for too long.
    """
    if last_day_for_irrigation > 15:
        raise PlantError(f"The {plant} plant is wilting!")


def test_errors() -> None:
    """
    Demonstrates the use of custom garden-related exceptions.

    Shows:
    - Raising and catching PlantError
    - Raising and catching WaterError
    - Catching all garden-related errors using GardenError
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    plant = "tomato"
    try:
        check_wilting(plant, 16)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        check_wilting(plant, 16)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")
