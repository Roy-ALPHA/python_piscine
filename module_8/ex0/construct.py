#!/usr/bin/env python3
import sys
import os
import site


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
    print(
        "\nMATRIX STATUS: Welcome to the construct\n",

        f"Current Python: {sys.executable}",
        f"Virtual Environment: {os.environ['VIRTUAL_ENV_PROMPT']}",
        f"Environment Path: {sys.prefix}\n",

        "SUCCESS: You're in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.\n",

        "Package installation path:",
        f"{"".join(site.getsitepackages())}", sep="\n"
    )
