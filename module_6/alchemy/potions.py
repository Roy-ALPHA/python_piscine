from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with {elements.create_fire()} and"
        f" {elements.create_water}"
    )

print(healing_potion())
