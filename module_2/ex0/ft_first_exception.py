#!/usr/bin/env python3
def check_temperature(temp_str: str) -> int | None:
    """
    Validate a temperature value received as a string.

    The function attempts to convert the input string into an integer
    and checks whether it falls within a safe range for plants.

    Args:
        temp_str (str): Temperature value provided as a string.

    Returns:
        int | None:
            - The temperature if it is valid.
            - None if the value is invalid or out of range.

    Errors handled:
        - Non-numeric input (ValueError)
        - Temperature too high (> 40)
        - Temperature too low (< 0)
    """
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")
    return None


def test_temperature_input() -> None:
    """
    Test the check_temperature function with various inputs.

    Demonstrates:
        - Valid input
        - Non-numeric input
        - Extremely high temperature
        - Extremely low temperature

    Shows that the program continues running even after errors.
    """
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
    print("All tests completed - program didn't crash!")
