#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda spl: (spell1(spl), spell2(spl))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda base_spl: base_spell(base_spl) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda spl: spell(spl) if condition(spl) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda effect: [spl(effect) for spl in spells]
