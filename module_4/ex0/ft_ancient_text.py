#!/usr/bin/env python3
print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
fil = "ancient_fragment.txt"
f = None
try:
    f = open(fil)
    print(f"Accessing Storage Vault: {fil}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(f.read())
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
finally:
    if f:
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
