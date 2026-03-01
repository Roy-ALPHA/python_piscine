#!/usr/bin/env python3
import sys
import os


if sys.prefix == sys.base_prefix:
    print(
        "\nMATRIX STATUS: You're still plugged in\n",

        f"Current Python: {sys.executable}",
        "Virtual Environment: None detected\n",

        "WARNING: You're in the global environment!",
        "The machines can see everything you install.\n",

        "To enter the construct, run:",
        "python -m venv matrix_env",
        "source matrix_env/bin/activate # On Unix",
        "matrix_env",
        "Scripts",
        "activate # On Windows\n",

        "Then run this program again.", sep="\n"
    )
else:
    print("# Should detect virtual environment and show details")
