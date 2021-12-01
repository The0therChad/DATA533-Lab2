from CardGame.Blackjack.money import Money
from .person import Dealer, Player
from ..Cards.deck import Deck


class Game:
    def __init__(self, num_players: int = 1) -> None:
        if not isinstance(num_players, int):
            raise TypeError("'num_players' must be an integer")
        if num_players < 1:
            raise ValueError("'num_players' must be a positive value")

        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.players = [Player(money=Money()) for i in range(num_players)]

        for player in self.players:
            player.addToHand(self.dealer.dealHand(2))

        self.dealer.hand = self.dealer.dealCard()

    def newRound(self, num_players: int = 1):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)

        for player in self.players:
            player.hand = self.dealer.dealHand(2)

        self.dealer.hand = self.dealer.dealCard()

    def run(self):
        live_table = True
        while live_table == True:
            self.newRound()
            print(self.players[0].showMoney())
            bet = self.players[0].money.bet()
            print("Dealer's hand: ", self.dealer.hand)
            print("Your hand: ", self.players[0].hand)
            self.dealer.addToHand(self.dealer.dealCard())
            if self.players[0].hand.getTotalPoints() == 21:
                self.players[0].money.blackjack(bet)
                continue
            hit = True
            while hit == True:
                hit = self.players[0].hit_stand(self.dealer.dealCard(), bet)
