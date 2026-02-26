from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    card1 = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 20, 1200)
    card2 = TournamentCard("Ice Wizard", 5, Rarity.RARE, 5, 15, 1150)

    tournament = TournamentPlatform()

    card1_id = tournament.register_card(card1)
    card2_id = tournament.register_card(card2)

    print(f"{card1.name} (ID: {card1_id}):")
    print("- Interfaces: ")
    print(f"- Rating: {card1.calculate_rating()}")
    wins = card1.get_rank_info()["wins"]
    losses = card1.get_rank_info()["losses"]
    print(f"- Record: {wins}-{losses}\n")

    print(f"{card2.name} (ID: {card2_id}):")
    print("- Interfaces: ")
    print(f"- Rating: {card2.calculate_rating()}")
    wins = card2.get_rank_info()["wins"]
    losses = card2.get_rank_info()["losses"]
    print(f"- Record: {wins}-{losses}\n")

    print("Creating tournament match...")
    print(f"Match result: {tournament.create_match(card1_id, card2_id)}\n")

    print("Tournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()

    i = 1
    for card in leaderboard:
        wins = card.get_rank_info()["wins"]
        losses = card.get_rank_info()["losses"]
        print(
            f"{i}. {card.name} - Rating: {card.calculate_rating()} "
            f"({wins}-{losses})"
        )
        i += 1

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
