#!/usr/bin/env python3
import sys
import math

print("=== Game Coordinate System ===\n")
try:
    lis_args = sys.argv[1].split(",")
    lis_args[0] = int(lis_args[0])
    lis_args[1] = int(lis_args[1])
    lis_args[2] = int(lis_args[2])
    origin = (0, 0, 0)
    position = (10, 20, 5)
    x1, y1, z1 = origin
    x2, y2, z2 = position
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Position created: {position}")
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")
    position = tuple(lis_args)
    x2, y2, z2 = position
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f'Parsing coordinates: "{x2},{y2},{z2}"')
    print(f"Parsed position: {position}")
    print(f"Distance between {origin} and {position}: "
          f"{distance:.1f}\n")
    print("Unpacking demonstration: ")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
except ValueError as e:
    try:
        print(f'Parsing invalid coordinates: '
              f'"{lis_args[0]},{lis_args[1]},{lis_args[2]}"')
        print(f"Error parsing coordinates: {e}")
        (error_msg,) = e.args
        print(f'Error details - Type: ValueError, Args: ("{error_msg}",)')
    except IndexError:
        print("Invalid format!")

except IndexError:
    print("No arguments provided!")
