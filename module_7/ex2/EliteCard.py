from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card, CardsError, Rarity


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: Rarity, health: int):
        super().__init__(name, cost, rarity)
        self.health = health
        self._mana = 8
        self.defense = 3
        self.attack = 5

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["player"]["mana"]):

            game_state["player"]["mana"] -= self.cost
            game_state["player"]["battlefield"].append(self)

            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'elite'
            }
        else:
            raise CardsError

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        valid_targets = [
            t for t in targets
            if isinstance(t, Combatable)
        ]

        if not valid_targets:
            raise CardsError

        mana_used = len(valid_targets) * 2

        if mana_used > self._mana:
            raise CardsError

        for t in valid_targets:
            t.defend(self.attack)

        self._mana -= mana_used

        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [t.name for t in valid_targets],
            'mana_used': mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self._mana += amount

        return {
            'channeled': amount,
            'total_mana': self._mana
        }

    def get_magic_stats(self) -> dict:
        infos = super().get_card_info()
        infos.update({
            "current_mana": self._mana,
        })
        return infos

    def attack(self, target) -> dict:
        if isinstance(target, Combatable):
            target.defend(self.attack)
            return {
                'attacker': self.name,
                'target': target.name,
                'damage': self.attack,
                'combat_type': 'melee'
            }

    def defend(self, incoming_damage: int) -> dict:
        damage = max(0, incoming_damage - self.defense)
        self.health -= damage

        return {
            'defender': self.name,
            'damage_taken': damage,
            'damage_blocked': self.defense,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        infos = super().get_card_info()
        infos.update({
            "attack": self.attack,
            "defense": self.defense
        })
        return infos

    def __str__(self):
        return "Elite Card"
