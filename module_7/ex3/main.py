from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from ex0.Card import EffectType


def main():
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    engine.player1.add_card(factory.create_creature("Fire Dragon"))
    engine.player1.add_card(factory.create_creature("Goblin Warrior"))
    engine.player1.add_card(factory.create_spell("Lightning Bolt"))

    engine.player2.add_card(factory.create_creature("Enemy Player"))

    engine.player1.cards[1].cost -= 3
    engine.player1.cards[2].effect_type = EffectType.DAMAGE

    print(
        "Hnad: "
        f"[{engine.player1.cards[0].name} ({engine.player1.cards[0].cost}), "
        f"{engine.player1.cards[1].name} ({engine.player1.cards[1].cost}), "
        f"{engine.player1.cards[2].name} ({engine.player1.cards[2].cost})]"
        )

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn()}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
