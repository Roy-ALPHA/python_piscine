#!/usr/bin/env python3
import sys
import math
def get_error(lis):
    try:
        lis[0] = int(lis[0])
    except:
        return lis[0]

    try:
        lis[1] = int(lis[1])
    except:
        return lis[1]

    try:
        lis[2] = int(lis[2])
    except:
        return lis[2]
print("=== Game Coordinate System ===\n")
try:
    lis_args = sys.argv[1].split(",")
    lis_args[0] = int(lis_args[0])
    lis_args[1] = int(lis_args[1])
    lis_args[2] = int(lis_args[2])
    x, y, z = tuple(lis_args)
    print(f'Parsing coordinates: "{x}, {y}, {z}"')
    print(f"Parsed position: ({x}, {y}, {z})")
    print(f"Distance between (0, 0, 0) and ({x}, {y}, {z}): {float(math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2))}\n")
    print("Unpacking demonstration: ")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
except:
    print(f'Parsing invalid coordinates: "{lis_args[0]}", "{lis_args[1]}", "{lis_args[2]}"')
    print(f"Error parsing coordinates: invalid literal for int() with base 10: '{get_error(lis_args)}'")
    print(f'Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: \'{get_error(lis_args)}\'",)')
