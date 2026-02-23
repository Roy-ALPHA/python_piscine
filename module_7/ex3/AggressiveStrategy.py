from .GameStrategy import GameStrategy
from ex0.Card import CardsError, Card
from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        cards_costs = [card.cost for card in hand]
        avg_cost = sum(cards_costs) / len(hand)

        cards = [
            card
            for card in hand
            if card.cost <= avg_cost and isinstance(card, Card)
        ]

        targets = self.prioritize_targets(battlefield.copy())

        battlefield.extend(cards)

        damaged = list()
        for card in cards:
            for t in targets:
                if isinstance(t, EliteCard):
                    t.defend(card.attack)
                    damaged.append(t)
                elif isinstance(t, CreatureCard):
                    t.health -= card.attack
                    damaged.append(t)

        return {
            'cards_played': cards,
            'mana_used': sum(c.cost for c in cards),
            'targets_attacked': damaged,
            'damage_dealt': sum(c._attack for c in cards)
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:

        i = 0
        while i < len(available_targets):
            j = i + 1
            while j < len(available_targets):
                try:
                    if (available_targets[i].health >
                            available_targets[j].health):
                        tmp = available_targets[i]
                        available_targets[i] = available_targets[j]
                        available_targets[j] = tmp
                except AttributeError:
                    pass
                j += 1
            i += 1

        return available_targets
