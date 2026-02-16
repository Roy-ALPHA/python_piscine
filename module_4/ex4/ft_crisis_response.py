#!/usr/bin/env python3


def crisis_management(file_name: str) -> tuple[bool, str | None]:
    try:
        with open(file_name, "r") as file:
            lines = file.read()
        return True, lines
    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Archive not found in storage matrix",
            "STATUS: Crisis handled, system stable\n",
            sep="\n"
        )
        return False, None
    except PermissionError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: Security protocols deny access",
            "STATUS: Crisis handled, security maintained\n",
            sep="\n"
        )
        return False, None
    except Exception:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...",
            "RESPONSE: An unexpected system anomaly occurred",
            "STATUS: Crisis handled, system stable\n",
            sep="\n"
        )
        return False, None


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
files = [
    'lost_archive.txt', 'classified_vault.txt', 'standard_archive.txt'
    ]
for file_name in files:
    success, lines = crisis_management(file_name)
    if success:
        print(
            f"ROUTINE ACCESS: Attempting access to '{file_name}'...",
            f"SUCCESS: Archive recovered - ``{lines}''",
            "STATUS: Normal operations resumed\n",
            sep="\n"
        )
print("All crisis scenarios handled successfully. Archives secure.")
