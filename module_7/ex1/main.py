from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity, EffectType, EffectTypeForPlayer
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    spell = SpellCard('Lightning Bolt', 3, Rarity.EPIC, EffectType.DAMGAE)
    creature = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 7, 10)
    artifact = ArtifactCard(
        'Mana Crystal', 2, Rarity.EPIC, 4, EffectTypeForPlayer.BUFF
    )

    cards = [spell, creature, artifact]

    deck = Deck()
    for card in cards:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_card_info()}")

if __name__ == "__main__":
    main()
