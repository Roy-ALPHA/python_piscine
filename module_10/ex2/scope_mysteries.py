#!/usr/bin/env python3


def mage_counter() -> callable:
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> callable:

    def acc_power(amount):
        nonlocal initial_power
        initial_power += amount
        return initial_power

    return acc_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchante(item_name):
        return f"{enchantment_type} {item_name}"
    return enchante


def memory_vault() -> dict[str, callable]:
    memory = dict()

    def store(key, value) -> None:
        memory.update({key: value})

    def recall(key):
        return memory.get(key) if key in memory else "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()

    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming_enchant = enchantment_factory("Flaming")
    print(flaming_enchant("Sword"))

    frozen_enchant = enchantment_factory("Frozen")
    print(frozen_enchant("Shield"))


if __name__ == "__main__":
    main()
