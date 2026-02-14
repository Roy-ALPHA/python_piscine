def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "allo", "earth", "air"]
    exists = True

    for word in ingredients.split():
        if word not in valid_ingredients:
            exists = False
            break

    if exists:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
