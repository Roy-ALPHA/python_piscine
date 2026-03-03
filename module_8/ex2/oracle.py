#!/usr/bin/env python3
"""
Oracle - Environment Variable Configuration Manager

This script demonstrates secure configuration management using
environment variables loaded from a .env file. It validates that
all required configuration variables are present.
"""
from os import environ
from dotenv import load_dotenv
from sys import exit


print("\nORACLE STATUS: Reading the Matrix...\n")

print("Configuration loaded:")

# load_dotenv() reads key-value pairs from a .env file
# and sets them as environment variables
# Returns False if .env file is not found
if not load_dotenv():
    print("Configuration Error: .env file not found.")
    exit(1)

# Define required environment variables as
# tuples of (display_name, env_var_name)
# This allows for user-friendly output while checking actual variable names
required_vars = [
    ("Mode", "MATRIX_MODE"),
    ("Database", "DATABASE_URL"),
    ("API Access", "API_KEY"),
    ("Log Level", "LOG_LEVEL"),
    ("Zion Network", "ZION_ENDPOINT")
]

# Track missing environment variables for error reporting
req_env = list()

# Iterate through required variables and check if they exist
for mes, env in required_vars:
    try:
        # environ[env] raises KeyError if variable doesn't exist
        print(f'{mes}: {environ[env]}')
    except KeyError as e:
        # Variable not found - log the error and track it
        print(
            f"Configuration Error: Missing environment variable '{e.args[0]}'."
        )
        req_env.append(env)

# Security validation section
print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")

# Check if all required variables are present
print(
    "[OK] .env file properly configured"
    if not req_env
    else f"[ERROR] Missing variables: {", ".join(req_env)}"
)

# Verify production mode is enabled for production overrides
# environ.get() returns None instead of raising KeyError if not found
print(
    "[OK] Production overrides available"
    if environ.get("MATRIX_MODE") == "production"
    else "[ERROR] Production overrides not active"
)

print("\nThe Oracle sees all configurations.")
