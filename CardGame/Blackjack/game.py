from .person import Dealer, Player
from ..Cards.deck import Deck

class Game():
    def __init__(self, num_players: int = 1) -> None:
        if not isinstance(num_players, int):
            raise TypeError("'num_players' must be an integer")
        if num_players < 1:
            raise ValueError("'num_players' must be a positive value")
        
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.players = [Player() for i in range(num_players)]

        for player in self.players:
            player.addToHand(self.dealer.dealHand(2))