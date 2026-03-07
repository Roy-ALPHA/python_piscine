#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(lambda x, y: max(x, y), spells)
    elif operation == "min":
        return reduce(lambda x, y: min(x, y), spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire_enchant"),
        "ice_enchant": partial(base_enchantment, 50, "ice_enchant"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning_enchant")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


@singledispatch
def spell_dispatcher(spell):
    return "Unknown spell type"


@spell_dispatcher.register(str)
def _(spell: str) -> str:
    return f"{spell} enchanted"


@spell_dispatcher.register(int)
def _(dmg: int) -> str:
    return f"Spell deals {dmg} damage"


@spell_dispatcher.register(list)
def _(spells: list) -> str:
    return f'{", ".join(spells)} cast together'


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [20, 30, 10, 40]
    print(
        f"Sum: {spell_reducer(spells, "add")}",
        f"Product: {spell_reducer(spells, "multiply")}",
        f"Max: {spell_reducer(spells, "max")}", sep='\n'
    )

    print("\nTesting memoized fibonacci...")
    print(
        f"Fib(10): {memoized_fibonacci(10)}",
        f"Fib(15): {memoized_fibonacci(15)}",
        sep='\n'
    )


if __name__ == "__main__":
    main()
