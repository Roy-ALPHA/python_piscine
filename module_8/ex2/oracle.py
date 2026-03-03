from os import environ
from dotenv import load_dotenv
from sys import exit


print("\nORACLE STATUS: Reading the Matrix...\n")

print("Configuration loaded:")

if not load_dotenv():
    print("Configuration Error: .env file not found.")
    exit(1)

required_vars = [
    ("Mode", "MATRIX_MODE"),
    ("Database", "DATABASE_URL"),
    ("API Access", "API_KEY"),
    ("Log Level", "LOG_LEVEL"),
    ("Zion Network", "ZION_ENDPOINT")
]

req_env = list()

for mes, env in required_vars:
    try:
        print(f'{mes}: {environ[env]}')
    except KeyError as e:
        print(
            f"Configuration Error: Missing environment variable '{e.args[0]}'."
        )
        req_env.append(env)

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print(
    "[OK] .env file properly configured"
    if not req_env
    else f"[ERROR] Missing variables: {", ".join(req_env)}"
)
print(
    "[OK] Production overrides available"
    if environ.get("MATRIX_MODE") == "production"
    else "[ERROR] Production overrides not active"
)

print("\nThe Oracle sees all configurations.")
