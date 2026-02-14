def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validator_res = validate_ingredients(ingredients)
    if "VALID" in validator_res and spell_name:
        return f"Spell recorded: {spell_name} ({validator_res})"
    else:
        return f"Spell rejected: {spell_name} ({validator_res})"
