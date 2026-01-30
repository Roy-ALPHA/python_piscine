#!/usr/bin/env python3
def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except:
        print(f"Error: '{temp_str}' is not a valid number")
