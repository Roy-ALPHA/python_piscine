from ex0.Card import Card, Rarity, CardsError


class ArtifactCard(Card):
    def __init__(
       self, name: str, cost: int, rarity: Rarity, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

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
                'effect': self.effect
            }
        else:
            raise CardsError

    def activate_ability(self) -> dict:
        self.durability -= 1

        return {
            "artifact": self.name,
            "durability_left": self.durability,
            "effect": self.effect
        }

    def get_card_info(self) -> dict:
        infos = super().get_card_info()
        infos.update({
            "durability": self.durability,
            "effect": self.effect
        })
        return infos
