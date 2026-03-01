from ex0.Card import Card, Rarity, CardsError
from .Combatable import Combatable
from .Magical import Magical
from .EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    card_mtds = list()

    for mtd in Card.__dict__.keys():
        if not mtd.startswith(("__", "_")):
            card_mtds.append(mtd)

    print(f"- Card: {card_mtds}")

    comba_mtds = list()

    for mtd in Combatable.__dict__.keys():
        if not mtd.startswith(("__", "_")):
            comba_mtds.append(mtd)

    print(f"- Combatable: {comba_mtds}")

    magic_mtds = list()

    for mtd in Magical.__dict__.keys():
        if not mtd.startswith(("__", "_")):
            magic_mtds.append(mtd)

    print(f"- Magical: {magic_mtds}")

    arcane = EliteCard('Arcane Warrior', 10, Rarity.LEGENDARY, 20)
    target = EliteCard("Enemy", 10, Rarity.LEGENDARY, 20)

    print(f"\nPlaying {arcane.name} ({arcane}):\n")

    try:
        print(
            "Combat phase:",
            f"Attack result: {arcane.attack(target)}",
            f"Defense result: {arcane.defend(5)}\n",
            sep="\n"
        )
    except CardsError as e:
        print(f"Combat failed: {e}")

    target1 = EliteCard("Enemy1", 10, Rarity.LEGENDARY, 20)
    target2 = EliteCard("Enemy2", 10, Rarity.LEGENDARY, 20)

    try:
        print(
            "Magic phase:",
            f"Spell cast: {arcane.cast_spell('Fireball', [target1, target2])}",
            f"Mana channel: {arcane.channel_mana(3)}\n",
            sep="\n"
        )
    except CardsError as e:
        print(f"Magic failed: {e}")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
