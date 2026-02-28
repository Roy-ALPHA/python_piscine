from .GameStrategy import GameStrategy
from .CardFactory import CardFactory
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.Card import CardsError


class GameEngine():

    @staticmethod
    def update_cards(cards: list) -> None:
        for card in cards:
            if isinstance(card, SpellCard):
                cards.remove(card)
            elif isinstance(card, ArtifactCard):
                if card.get_card_info()["durability"] <= 0:
                    cards.remove(card)

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        if not isinstance(factory, CardFactory):
            raise CardsError("Invalid factory: must be a CardFactory instance")
        if not isinstance(strategy, GameStrategy):
            raise CardsError(
                "Invalid strategy: must be a GameStrategy instance"
            )

        self.__factory = factory
        self.__strategy = strategy
        self.player1 = factory.create_themed_deck(0)["deck"]
        self.player2 = factory.create_themed_deck(0)["deck"]
        self.__turns = 0
        self.__total_dmg = 0
        self.battlefield = list()

    def simulate_turn(self) -> dict:
        if self.__turns % 2 == 0:
            self.battlefield = self.player2.cards.copy()
            action = self.__strategy.execute_turn(
                self.player1.cards, self.battlefield
            )
        else:
            self.battlefield = self.player1.cards.copy()
            action = self.__strategy.execute_turn(
                self.player2.cards, self.battlefield
            )
        self.__turns += 1

        self.__total_dmg += action['damage_dealt']

        self.update_cards(self.player1.cards)
        self.update_cards(self.player2.cards)

        return action

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.__turns,
            'strategy_used': self.__strategy.get_strategy_name(),
            'total_damage': self.__total_dmg,
            'cards_created': len(self.player1.cards) + len(self.player2.cards)
            }
