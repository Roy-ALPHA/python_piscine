#!/usr/bin/env python3
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Checks whether a plant's health conditions are valid.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level (1 to 10).
        sunlight_hours (int): Sunlight hours per day (2 to 12).

    Raises:
        ValueError: If any of the values are invalid.

    Returns:
        str: Success message if the plant is healthy.
    """
    if plant_name is None or not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         " is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         " is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         " is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         " is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Tests the check_plant_health function with valid and invalid inputs.
    Demonstrates raising and catching ValueError.
    """
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(e)
    print()
    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e)
    print()
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(e)
    print()
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    print()
    print("All error raising tests completed!")
