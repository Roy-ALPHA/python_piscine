#!/usr/bin/env python3
print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

try:
    with open("classified_data.txt", "r+") as file:
        print(
            "Initiating secure vault access...",
            "Vault connection established with failsafe protocols\n",
            sep="\n"
        )
        print("SECURE EXTRACTION:")
        print(file.read())

        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "r") as f:
            lines = f.read()
            print(lines)
            file.write(lines)
            print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
except PermissionError:
    print("ERROR: Access denied. Insufficient security clearance for vault.")
