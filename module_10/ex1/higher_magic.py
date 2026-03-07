#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *targets: (spell1(*targets), spell2(*targets))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *spls: spell(*spls) if condition(*spls) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda effect: [spl(effect) for spl in spells]


def main() -> None:

    def spell1(target: str) -> str:
        return f"Fireball hits {target}"

    def spell2(target: str) -> str:
        return f"Heals {target}"

    print("\nTesting spell combiner...")
    combiner = spell_combiner(spell1, spell2)
    print(f"Combined spell result: {", ".join(combiner("Dragon"))}")

    print("\nTesting power amplifier...")

    def spell_dmg() -> int:
        return 10

    mega_spell = power_amplifier(spell_dmg, 3)
    print(f"Original: {spell_dmg()}, Amplified: {mega_spell()}")


if __name__ == "__main__":
    main()
