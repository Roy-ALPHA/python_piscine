#!/usr/bin/env python3
class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_water(water):
    if water <= 0:
        raise WaterError(f"Not enough water in the tank!")

def check_wilting(plant, last_day_for_irrigation):
    if last_day_for_irrigation > 15:
        raise PlantError(f"The {plant} plant is wilting!")

def test_errors():
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
        print(f"Caught PlantError: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught WaterError: {e}\n")
    print("All custom error types work correctly!")
