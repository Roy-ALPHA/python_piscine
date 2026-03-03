#!/usr/bin/env python3
"""
Construct - Virtual Environment Detection Script

This script detects whether Python is running inside a virtual environment
or in the global system environment, using a Matrix-themed metaphor.
"""
import sys
import os
import site


'''Environment Detection Logic:
sys.prefix: Path to the Python installation being used
    (could be venv or global)
sys.base_prefix: Path to the base Python installation (always the global one)

When running in the global environment:
  sys.prefix == sys.base_prefix (both point to system Python)

When running in a virtual environment:
  sys.prefix != sys.base_prefix
  sys.prefix points to the venv, sys.base_prefix points to system Python'''

if sys.prefix == sys.base_prefix:
    # Global environment detected - not in a virtual environment
    print(
        "\nMATRIX STATUS: You're still plugged in\n",

        # Show current Python executable path
        f"Current Python: {sys.executable}",
        "Virtual Environment: None detected\n",

        "WARNING: You're in the global environment!",
        "The machines can see everything you install.\n",

        # Instructions to create and activate a virtual environment
        "To enter the construct, run:",
        "python -m venv matrix_env",
        "source matrix_env/bin/activate # On Unix",
        "matrix_env",
        "Scripts",
        "activate # On Windows\n",

        "Then run this program again.", sep="\n"
    )
else:
    # Virtual environment detected - isolated from global system
    print(
        "\nMATRIX STATUS: Welcome to the construct\n",

        # Show current Python executable (points to venv's Python)
        f"Current Python: {sys.executable}",
        # VIRTUAL_ENV_PROMPT contains the venv name shown in shell prompt
        f"Virtual Environment: {os.environ['VIRTUAL_ENV_PROMPT']}",
        # sys.prefix shows the venv directory path
        f"Environment Path: {sys.prefix}\n",

        "SUCCESS: You're in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.\n",

        "Package installation path:",
        f"{"".join(site.getsitepackages())}", sep="\n"
    )
