from abc import ABC, abstractmethod
from enum import Enum


class CardsError(Exception):
    pass


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class EffectType(Enum):
    DAMAGE = 'Deal 3 damage to target'
    HEAL = "Restore 3 health to target"
    BUFF = "Increase target's attack by 3"
    DEBUFF = "Decrease target's attack by 3"


class EffectTypeForPlayer(Enum):
    DAMGAE = "Increase player's attack by 3"
    HEAL = "Restore 3 health to player"
    BUFF = 'Permanent: +1 mana per turn'


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
