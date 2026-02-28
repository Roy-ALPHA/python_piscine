from ex0.Card import Card, CardsError
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from random import shuffle


class Deck:

    def __init__(self):
        self.cards = list()

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise CardsError("Invalid card: must be a Card instance")

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise CardsError("Cannot draw: deck is empty")

    def get_deck_stats(self) -> dict:
        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

            total_cost += card.cost

        avg_cost = round(total_cost / len(self.cards), 1) if self.cards else 0
        return {
            'total_cards': len(self.cards),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
