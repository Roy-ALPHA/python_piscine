#!/usr/bin/env python3
def water_plants(plant_list):
    error_occurred = False
    print ("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        error_occurred = True
        print(f"{e}")
    finally:
        print(f"Closing watering system (cleanup)")
        if error_occurred is False:
            print(f"Watering completed successfully!")
def test_watering_system():
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print()
        print("Testing with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as e:
        print (f"\n{e}")
    finally:
        print ("\nCleanup always happens, even with errors!")
