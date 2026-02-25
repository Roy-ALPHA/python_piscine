from .GameStrategy import GameStrategy
from ex0.Card import Card, EffectType
from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        if not hand:
            return {
                "cards_played": [],
                "mana_used": 0,
                "targets_attacked": [],
                "damage_dealt": 0
            }

        costs = [card.cost for card in hand]
        avg_cost = sum(costs) / len(hand)

        cards = [
            card
            for card in hand
            if card.cost <= avg_cost and isinstance(card, Card)
        ]

        targets = self.prioritize_targets(battlefield.copy())

        battlefield.extend(cards)

        damaged = list()
        total_dmg = 0
        for card in cards:
            for t in targets:
                is_damaged = False
                if isinstance(card, CreatureCard):
                    action = card.attack_target(t)
                    is_damaged = True
                elif isinstance(card, SpellCard):
                    action = card.resolve_effect([t])
                    is_damaged = True
                elif isinstance(card, ArtifactCard):
                    action = card.activate_ability()
                    is_damaged = True
                elif isinstance(card, EliteCard):
                    action = card.attack(t)
                    is_damaged = True

                if is_damaged and t not in damaged:
                    damaged.append(t)

                if isinstance(action, dict):
                    try:
                        action['damage_dealt']
                    except KeyError:
                        pass
                    else:
                        total_dmg += action['damage_dealt']

                    try:
                        action['effect']
                    except KeyError:
                        pass
                    else:
                        if EffectType.DAMAGE.value == action["effect"]:
                            total_dmg += 3

        return {
            'cards_played': [card.name for card in cards],
            'mana_used': sum(c.cost for c in cards),
            'targets_attacked': [d.name for d in damaged],
            'damage_dealt': total_dmg
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
