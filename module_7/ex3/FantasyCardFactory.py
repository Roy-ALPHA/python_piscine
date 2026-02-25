from .CardFactory import CardFactory
from ex0.Card import Card, Rarity, EffectType, EffectTypeForPlayer
from ex0.CreatureCard import CreatureCard
from random import choice
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.__creatures = ['dragon', 'goblin']
        self.__spells = ['fireball']
        self.__artifacts = ['mana_ring']

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        CRT_COST = 5
        CRT_ATTACK = 5
        CRT_HEALTH = 20

        if isinstance(name_or_power, int):
            return CreatureCard(
                choice(self.__creatures), CRT_COST,
                choice(list(Rarity)), name_or_power, CRT_HEALTH
            )
        elif isinstance(name_or_power, str):
            return CreatureCard(
                name_or_power, CRT_COST,
                choice(list(Rarity)), CRT_ATTACK, CRT_HEALTH
            )
        else:
            return CreatureCard(
                choice(self.__creatures), CRT_COST,
                choice(list(Rarity)), CRT_ATTACK, CRT_HEALTH
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        SPL_COST = 3

        if isinstance(name_or_power, int):
            return SpellCard(
                choice(self.__spells), name_or_power,
                choice(list(Rarity)), choice(list(EffectType))
            )
        elif isinstance(name_or_power, str):
            return SpellCard(
                name_or_power, SPL_COST,
                choice(list(Rarity)), choice(list(EffectType))
            )
        else:
            return SpellCard(
                choice(self.__spells), SPL_COST,
                choice(list(Rarity)), choice(list(EffectType))
            )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        ART_COST = 3
        ART_DURABILITY = 6

        if isinstance(name_or_power, int):
            return ArtifactCard(
                choice(self.__artifacts), name_or_power, choice(list(Rarity)),
                ART_DURABILITY, choice(list(EffectTypeForPlayer))
            )
        elif isinstance(name_or_power, str):
            return ArtifactCard(
                name_or_power, ART_COST, choice(list(Rarity)),
                ART_DURABILITY, choice(list(EffectTypeForPlayer))
            )
        else:
            return ArtifactCard(
                choice(self.__artifacts), ART_COST, choice(list(Rarity)),
                ART_DURABILITY, choice(list(EffectTypeForPlayer))
            )

    def create_themed_deck(self, size: int) -> dict:
        fantasy_deck = Deck()

        creators = [
            self.create_artifact, self.create_creature, self.create_spell
        ]

        for _ in range(size):
            factory = choice(creators)
            fantasy_deck.add_card(factory())

        return {
            "deck": fantasy_deck
        }

    def get_supported_types(self) -> dict:
        return {
                "creatures": self.__creatures,
                "spells": self.__spells,
                "artifacts": self.__artifacts
            }

    def __str__(self):
        return "FantasyCardFactory"
