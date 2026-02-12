#!/usr/bin/env python3
def crisis_management(file_name):
    try:
        with open(file_name, "r") as file:
            try:
                lines = file.read()
            except PermissionError:
                return False, print(
                    f"CRISIS ALERT: Attempting access to '{file_name}'...",
                    "RESPONSE: Security protocols deny access",
                    "STATUS: Crisis handled, security maintained\n",
                    sep="\n"
                )
    except FileNotFoundError:
        return False, print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Archive not found in storage matrix",
            "STATUS: Crisis handled, system stable\n",
            sep="\n"
            )
    except Exception:
        return False, print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: An unexpected system anomaly occurred",
            "STATUS: Crisis handled, system stable\n",
            sep="\n"
        )
    return True, lines


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
files = [
    'lost_archive.txt', 'classified_vault.txt', 'standard_archive.txt'
    ]
for file_name in files:
    error, lines = crisis_management(file_name)
    if error is True:
        print(
            f"ROUTINE ACCESS: Attempting access to '{file_name}'...",
            f"SUCCESS: Archive recovered - ``{lines}''",
            "STATUS: Normal operations resumed",
            sep="\n"
        )
print("All crisis scenarios handled successfully. Archives secure.")
