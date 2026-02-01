#!/usr/bin/env python3
def garden_operations() -> None:
    """
    Demonstrates common garden-related errors in Python:
    - ValueError when converting a bad string to int
    - ZeroDivisionError when dividing by zero
    - FileNotFoundError when opening a non-existing file
    - KeyError when accessing a missing key in a dictionary
    - Multiple errors caught together
    Each error is caught and explained, and the program continues.
    """
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        test = {"name": "Ali"}
        print(test["plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("xyz")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """
    Runs all garden_operations error tests and prints a summary.
    Demonstrates that Python continues execution after each handled error.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")
