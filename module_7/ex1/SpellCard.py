from ex0.Card import Card, Rarity, CardsError, EffectType
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):

    def __init__(
        self, name: str, cost: int, rarity: Rarity, effect_type: EffectType
    ) -> None:
        super().__init__(name, cost, rarity)

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["player"]["mana"]):

            game_state["player"]["mana"] -= self.cost

            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect_type.value
            }
        else:
            raise CardsError

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            if isinstance(target, CreatureCard):
                if self.effect_type == EffectType.DAMAGE:
                    target.health -= 3
                elif self.effect_type == EffectType.HEAL:
                    target.health += 3
                elif self.effect_type == EffectType.DEBUFF:
                    target.attack -= 3
                elif self.effect_type == EffectType.BUFF:
                    target.attack += 3

        return {
            "spell": self.name,
            "targets": [
                t.name for t in targets if isinstance(t, CreatureCard)
            ],
            "effect": self.effect_type.value
        }

    def get_card_info(self):
        infos = super().get_card_info()
        infos.update({
            "effect_type": self.effect_type.value
        })
        return infos

    def __str__(self):
        return "Spell"
