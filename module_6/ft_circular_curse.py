#!/usr/bin/env python3
from alchemy.grimoire import record_spell, validate_ingredients

print("\n=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
print(
    'validate_ingredients("dragon scales"): '
    f'{validate_ingredients("dragon scales")}\n'
)

print("Testing spell recording with validation:")
print(
    'record_spell("Fireball", "fire air"): '
    f'{record_spell("Fireball", "fire air")}'
)
print(
    'record_spell("Dark Magic", "shadow"): '
    f'{record_spell("Dark Magic", "shadow")}\n'
)

print("Testing late import technique:")
print(
    'record_spell("Lightning", "air"): '
    f'{record_spell("Lightning", "air")}\n'
)

print(
    "Circular dependency curse avoided using late imports!",
    "All spells processed safely!", sep='\n'
)
