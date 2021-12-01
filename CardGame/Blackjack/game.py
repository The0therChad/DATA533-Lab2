from CardGame.Blackjack.money import Money
from .person import Dealer, Player
from ..Cards.deck import Deck


class Game:
    def __init__(self, num_players: int = 1) -> None:
        if not isinstance(num_players, int):
            raise TypeError("'num_players' must be an integer")
        if num_players < 1:
            raise ValueError("'num_players' must be a positive value")

        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.players = [Player(money=Money()) for i in range(num_players)]

        for player in self.players:
            player.addToHand(self.dealer.dealHand(2))

        self.dealer.hand = self.dealer.dealCard()

    def newRound(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)

        for player in self.players:
            player.hand = self.dealer.dealHand(2)

        self.dealer.hand = self.dealer.dealHand(1)

    def run(self):
        live_table = True
        while live_table == True:
            self.newRound()
            print(self.players[0].showMoney())
            bet = self.players[0].money.bet()
            print("Dealer's hand: ", self.dealer.hand)
            print("Your hand: ", self.players[0].hand)
            self.dealer.hand.addCard(self.dealer.deck.drawCard())
            while self.players[0].hit_stand(self.dealer.deck.drawCard()) == True:
                pass
            if (
                self.players[0].hand.getTotalPoints() > 0
                and self.players[0].hand.getTotalPoints() != 21
            ):
                while self.dealer.hit_stand(self.dealer.deck.drawCard()) == True:
                    pass
            if (
                self.players[0].hand.getTotalPoints()
                == self.dealer.hand.getTotalPoints()
            ):
                print("Dealer's hand: ", self.dealer.hand)
                print("Your hand: ", self.players[0].hand)
                print("That's a tie.")
                self.players[0].money.payout(bet, 1)
            elif self.players[0].hand.getTotalPoints() == 21:
                self.players[0].money.blackjack(bet)
            elif (
                self.players[0].hand.getTotalPoints()
                > self.dealer.hand.getTotalPoints()
            ):
                print("Dealer's hand: ", self.dealer.hand)
                print("Your hand: ", self.players[0].hand)
                print(f"You won ${bet}!")
                self.players[0].money.payout(bet, 2)
            else:
                print("The dealer wins that round.")

            if self.players[0].money.value <= 0:
                print(f"You have ${self.players[0].money.value}\nGame Over")
                self.players = [Player(money=Money()) for i in range(self.num_players)]
                live_table = False
            elif self.players[0].money.value >= self.players[0].money.win:
                print(f"You have ${self.players[0].money.value}\nYou win!")
                self.players = [Player(money=Money()) for i in range(self.num_players)]
                live_table = False
