#!/usr/bin/env python3
"""
Loading - Dynamic Module Import and Dependency Checker

This script demonstrates dynamic module importing using importlib
and checks if required dependencies are installed before running.
"""
from importlib import import_module
from importlib.metadata import version


print("\nLOADING STATUS: Loading programs...\n")

# Check and load required dependencies dynamically
# import_module() allows importing modules by name at runtime
# version() retrieves the installed package version from metadata
print("Checking dependencies:")
try:
    # Dynamically import pandas for data manipulation
    pd = import_module("pandas")
    print(f"[OK] pandas ({version("pandas")}) - Data manipulation ready")
except ModuleNotFoundError as e:
    # Module not installed - print error message
    print("[KO] " + e.args[0])

try:
    # Dynamically import requests for HTTP/network operations
    req = import_module("requests")
    print(f"[OK] requests ({version("requests")}) - Network access ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

try:
    # Dynamically import matplotlib.pyplot for data visualization
    plt = import_module("matplotlib.pyplot")
    print(f"[OK] matplotlib ({version("matplotlib")}) - Visualization ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

try:
    # Dynamically import numpy for numerical operations
    np = import_module("numpy")
except ModuleNotFoundError:
    # Silently pass - error will be caught in the analysis block
    pass

print("\nAnalyzing Matrix data...")

try:
    # Generate sample data using numpy
    print("Processing 1000 data points...")
    time = np.arange(1000)  # Create array of 0-999 for x-axis
    sig = np.random.normal(50, 5, 1000)  # Generate random signal data

    # Create a pandas DataFrame to organize the data
    df = pd.DataFrame({
        "time": time,
        "signal": sig
    })

    # Create and configure the plot using matplotlib
    print("Generating visualization...")
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal")
    plt.xlabel("time")
    plt.ylabel("signal")

    print(
        "\nAnalysis complete!",
        "Results saved to: matrix\\_analysis.png}", sep="\n"
    )
    # Save the plot to a file
    plt.savefig("matrix_analysis.png")
except Exception:
    # Handle case where dependencies are missing or analysis fails
    print("\n[KO] One or more required dependencies are missing.")
    print("This program cannot run without the necessary packages.")
    print("To install dependencies:")
    print("    pip install -r requirements.txt")
    print("or")
    print("    poetry install")
