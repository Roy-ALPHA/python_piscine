#!/usr/bin/env python3
from importlib import import_module
from importlib.metadata import version


print("\nLOADING STATUS: Loading programs...\n")

print("Checking dependencies:")
try:
    pd = import_module("pandas")
    print(f"[OK] pandas ({version("pandas")}) - Data manipulation ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

try:
    req = import_module("requests")
    print(f"[OK] requests ({version("requests")}) - Network access ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

try:
    plt = import_module("matplotlib.pyplot")
    print(f"[OK] matplotlib ({version("matplotlib")}) - Visualization ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

try:
    np = import_module("numpy")
except ModuleNotFoundError:
    pass

print("\nAnalyzing Matrix data...")

try:
    print("Processing 1000 data points...")
    time = np.arange(1000)
    sig = np.random.normal(50, 5, 1000)

    df = pd.DataFrame({
        "time": time,
        "signal": sig
    })

    print("Generating visualization...")
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal")
    plt.xlabel("time")
    plt.ylabel("signal")

    print(
        "\nAnalysis complete!",
        "Results saved to: matrix\\_analysis.png}", sep="\n"
    )
    plt.savefig("matrix_analysis.png")
except Exception:
    print("\n[KO] One or more required dependencies are missing.")
    print("This program cannot run without the necessary packages.")
    print("To install dependencies:")
    print("    pip install -r requirements.txt")
    print("or")
    print("    poetry install")
