#!/usr/bin/env python3
def garden_operations():
    """
    Demonstrates common garden-related errors in Python:
    - ValueError when converting a bad string to int
    - ZeroDivisionError when dividing by zero
    - FileNotFoundError when opening a non-existing file
    - KeyError when accessing a missing key in a dictionary
    - Multiple errors caught together
    Each error is caught and explained, and the program continues.
    """
    try:
        num = int("abc")
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")

    try:
        res = 1 / 0
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        tmp1 = "test.txt"
        open(tmp1)
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print(f"Caught FileNotFoundError: No such file '{tmp1}'\n")

    try:
        d = {"name": "Ali"}
        tmp2 = "age"
        print(d[tmp2])
    except KeyError:
        print("Testing KeyError...")
        print(f"Caught KeyError: 'missing\\_{tmp2}'\n")

    try:
        int("xyz")
    except (ValueError, ZeroDivisionError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")

def test_error_types():
    """
    Runs all garden_operations error tests and prints a summary.
    Demonstrates that Python continues execution after each handled error.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")