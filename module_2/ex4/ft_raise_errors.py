#!/usr/bin/env python3
def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None or not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(f"{e}")
    print()
    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"{e}")
    print()
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 0, 6)
    except ValueError as e:
        print(f"{e}")
    print()
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"{e}")
    print()
    print("All error raising tests completed!")