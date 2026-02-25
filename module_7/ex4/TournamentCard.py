from ex2.Combatable import Combatable
from ex0.Card import Card, CardsError, Rarity
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self, name: str, cost: int, rarity: Rarity, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.defense = 3
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["player"]["mana"]):

            game_state["player"]["mana"] -= self.cost
            game_state["player"]["battlefield"].append(self)

            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'rarity': self.rarity
            }
        else:
            raise CardsError

    def attack(self, target) -> dict:
        if isinstance(target, Combatable):
            target.defend(self.attack_power)
            return {
                'attacker': self.name,
                'target': target.name,
                'damage': self.attack_power,
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
            "attack": self.attack_power,
            "defense": self.defense
        })
        return infos

    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }
