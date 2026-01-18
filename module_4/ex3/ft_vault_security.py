# !/usr/bin/env python3
print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
with open("classified_data.txt", "r+") as file:
    print(
        "Initiating secure vault access...",
        "Vault connection established with failsafe protocols\n",
        sep="\n"
    )
    print("SECURE EXTRACTION:")
    print(file.read())
    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", "r") as f:
        lines = f.read()
        print(lines)
    file.write(lines)
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
