from .Card import Card, CardsError, Rarity


class CreatureCard(Card):

    def __init__(
        self, name: str, cost: int, rarity: Rarity, attack: int, health: int
    ) -> None:

        if attack < 0 or health < 0 or cost < 0:
            raise CardsError

        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["player"]["mana"]):

            try:
                game_state["player"]["mana"] -= self.cost
                game_state["player"]["battlefield"].append(self)
            except KeyError:
                raise CardsError

            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
        else:
            raise CardsError

    def attack_target(self, target) -> dict:
        if isinstance(target, CreatureCard):
            target.health -= self.attack
            return {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': True
            }
        else:
            raise CardsError

    def get_card_info(self) -> dict:
        infos = super().get_card_info()
        infos.update({
            "type": 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return infos

    def __str__(self):
        return "Creature"
