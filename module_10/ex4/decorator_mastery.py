#!/usr/bin/env python3
from functools import wraps
from time import time, sleep


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args) -> any:
        print(f"Casting {func.__name__}...")

        start = time()

        result = func(*args)

        end = time()

        print(f"Spell completed in {(end - start):.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> callable:

    def dec(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args) -> any:
            if args[-1] >= min_power:
                return func(*args)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return dec


def retry_spell(max_attempts: int) -> callable:

    if max_attempts <= 0:
        return "max_attempts must be positive integer > 0"

    def dec(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args) -> any:

            n = 1
            while n <= max_attempts:
                try:
                    res = func(*args)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {n}/{max_attempts})"
                    )

                    if n == max_attempts:
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
                else:
                    return res

                n += 1

        return wrapper
    return dec


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        for char in name:
            if not char.isalpha() and not char == " ":
                return False

        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if MageGuild.validate_mage_name(spell_name):
            return f"Successfully cast {spell_name} with {power} power"
        else:
            return "Invalid spell name"


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.101)
        return f"Result: {fireball.__name__.capitalize()} cast!"

    print(fireball())

    print("\nTesting MageGuild...")
    mage = MageGuild()

    print(MageGuild.validate_mage_name("Fireball"))
    print(MageGuild.validate_mage_name("Fire\tball"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("hello", 3))


if __name__ == "__main__":
    main()
