#!/usr/bin/env python3
import sys


def print_av(av):
    if len(av) > 1:
        print(f"Arguments received: {len(av) - 1}")
        i = 1
        while i < len(av):
            print(f"Argument {i}: {av[i]}")
            i += 1
    print(f"Total arguments: {len(av)}")


print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
print(f"Program name: {sys.argv[0]}")
print_av(sys.argv)
