#!/usr/bin/env python3
from importlib import import_module
from importlib.metadata import version
import numpy as np


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
    mtp = import_module("matplotlib")
    print(f"[OK] matplotlib ({version("matplotlib")}) - Visualization ready")
except ModuleNotFoundError as e:
    print("[KO] " + e.args[0])

print("\nAnalyzing Matrix data...")
time = np.arange(100)
sig = np.random.normal(50, 5, 100)

df = pd.DataFrame({
    "time": time,
    "signal": sig
})

mtp.pyplot.plot(df["time"], df["siganl"])
mtp.pyplot.title("ALLO")
mtp.pyplot.xlabel("time")
mtp.pyplot.ylabel("signal")

mtp.pyplot.savefig("matrix_analysis.png")
mtp.pyplot.close()
