from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity, EffectType, EffectTypeForPlayer
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main():
    game_state = {
        "player": {
            "health": 20,
            "mana": 60,
            "battlefield": [],
        },
        "enemy": {
            "health": 18,
            "mana": 4,
            "battlefield": [],
        }
    }

    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    spell = SpellCard('Lightning Bolt', 3, Rarity.UNCOMMON, EffectType.DAMGAE)
    creature = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 7, 10)
    artifact = ArtifactCard(
        'Mana Crystal', 2, Rarity.UNCOMMON, 4, EffectTypeForPlayer.BUFF
    )

    cards = [spell, artifact, creature]

    deck = Deck()
    for card in cards:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_card_info()}")

    print("\nDrawing and playing cards:\n")

    while deck.cards:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card})")
        print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
