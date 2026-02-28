def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    exists = False

    for word in valid_ingredients:
        if word in ingredients:
            exists = True

    if exists:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
