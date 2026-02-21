from .CreatureCard import CreatureCard
from .Card import Rarity


def main():

    game_state = {
        "player": {
            "health": 20,
            "mana": 6,
            "battlefield": [],
        },
        "enemy": {
            "health": 18,
            "mana": 4,
            "battlefield": [],
        }
    }

    fire_dragon = CreatureCard(
        'Fire Dragon', 5, Rarity.LEGENDARY, 7, 5
    )
    goblin_warrior = CreatureCard(
        'Goblin Warrior', 4, Rarity.RARE, 3, 10
    )

    print("\n=== DataDeck Card Foundation ===\n")

    print("\nTesting Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print(
        f"\nPlaying {fire_dragon.name} with "
        f"{game_state["player"]["mana"]} mana available:"
    )
    print(f"Playable: {fire_dragon.is_playable(game_state["player"]["mana"])}")
    print(f"Play result: {fire_dragon.play(game_state)}")

    print(f"\n{fire_dragon.name} attacks {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print("\nTesting insufficient mana (3 available):")
    print(
        f"Playable: {fire_dragon.is_playable(game_state["player"]["mana"])}\n"
    )

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
