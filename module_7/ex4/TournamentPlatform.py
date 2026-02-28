from .TournamentCard import TournamentCard
from ex0.Card import CardsError


class TournamentPlatform():

    def __init__(self):
        self.tr_cards: dict[str, TournamentCard] = dict()
        self.__matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise CardsError("Invalid card: must be a TournamentCard instance")

        id_name = card.name.split()
        counter = 1

        for key in self.tr_cards.keys():
            if key.startswith(id_name[-1].lower()):
                counter = int(key.split("_")[-1]) + 1

        card_id = f"{id_name[-1].lower()}_{counter:03d}"

        self.tr_cards.update({card_id: card})

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.tr_cards.get(card1_id)
        card2 = self.tr_cards.get(card2_id)
        if not card1 or not card2 or card1 == card2:
            raise CardsError("Invalid match: cards not found or same card")

        rounds = 0
        winner = None

        while not winner:
            if rounds % 2 == 0:
                action = card1.attack(card2)
                if not action["still_alive"]:
                    winner, loser = card1, card2
                    winner_id, loser_id = card1_id, card2_id
            else:
                action = card2.attack(card1)
                if not action["still_alive"]:
                    winner, loser = card2, card1
                    winner_id, loser_id = card2_id, card1_id
            rounds += 1

        winner.update_wins(1)
        loser.update_losses(1)

        self.__matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
            }

    def get_leaderboard(self) -> list:
        leaderboard = list(self.tr_cards.values())
        i = 0
        while i < len(leaderboard):
            j = i + 1
            while j < len(leaderboard):
                if (leaderboard[i].calculate_rating() <
                   leaderboard[j].calculate_rating()):
                    tmp = leaderboard[i]
                    leaderboard[i] = leaderboard[j]
                    leaderboard[j] = tmp
                j += 1
            i += 1
        return leaderboard

    def generate_tournament_report(self) -> dict:
        if self.tr_cards:
            avg_rating = sum(c.calculate_rating()
                             for c in self.tr_cards.values())
            avg_rating //= len(self.tr_cards)
        else:
            avg_rating = 0
        return {
            'total_cards': len(self.tr_cards),
            'matches_played': self.__matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
