#!/usr/bin/env python3
def water_plants(plant_list: list) -> None:
    """
    Simulates watering plants while ensuring cleanup always happens.

    Args:
        plant_list (list[str]): List of plant names to water.

    Raises:
        ValueError: If an invalid plant (None) is encountered.
    """
    error_occurred = False
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        error_occurred = True
        print(e)
    finally:
        print("Closing watering system (cleanup)")
        if error_occurred is False:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the watering system with valid and invalid inputs.
    Demonstrates that cleanup always happens.
    """
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print()
        print("Testing with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as e:
        print(f"\n{e}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
