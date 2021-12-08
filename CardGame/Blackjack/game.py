from signal import signal, SIGINT
from sys import exit

from .money import Money
from .person import Dealer, Player
from ..Cards.deck import Deck


class Game():
    def __init__(self, num_players: int = 1) -> None:
        if not isinstance(num_players, int):
            raise TypeError("'num_players' must be an integer")
        if num_players < 1:
            raise ValueError("'num_players' must be a positive value")
        signal(SIGINT, ctrl_C_handler)

        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.players = [Player(money=Money()) for i in range(num_players)]

        for player in self.players:
            player.addToHand(self.dealer.dealHand(2))

        self.dealer.hand = self.dealer.dealHand(1)

    def newRound(self) -> None:
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
            print("Dealer's hand: ", self.dealer.displayHand())
            print("Your hand: ", self.players[0].displayHand(), "\n")
            self.dealer.addCardToHand(self.dealer.dealCard())

            # Phase where player hits or stands
            hit = self.players[0].hit_stand()
            while hit == True:
                self.players[0].addCardToHand(self.dealer.dealCard())
                print("Your hand: ", self.players[0].displayHand())

                if self.players[0].getHandPoints() > 21:
                    print("You go bust!")
                    self.players[0].discardHand()
                    hit = False
                elif self.players[0].getHandPoints() == 21:
                    print("That's a blackjack!")
                    hit = False
                else:
                    hit = self.players[0].hit_stand()
            player_points = self.players[0].getHandPoints()

            # Dealer's turn to hit or stand now
            if player_points > 0 and player_points != 21:
                dealer_hit = self.dealer.hit_stand()
                while dealer_hit == True:
                    self.dealer.addCardToHand(self.dealer.dealCard())
                    dealer_hit = self.dealer.hit_stand()
            dealer_points = self.dealer.getHandPoints()
            
            # Finished dealing cards, not compare hand scores
            if player_points == dealer_points:
                print("Dealer's hand: ", self.dealer.displayHand())
                print("Your hand: ", self.players[0].displayHand())
                print("That's a tie. \n")
                self.players[0].money.payout(bet, 1)
            elif player_points == 21:
                print(f"You win ${1.5 * bet}")
                self.players[0].money.payout(bet, 2.5)
            elif player_points > dealer_points:
                print("Dealer's hand: ", self.dealer.displayHand())
                print("Your hand: ", self.players[0].displayHand())
                print(f"You won ${bet}! \n")
                self.players[0].money.payout(bet, 2)
            else:
                print("The dealer wins that round. \n")

            # Determine if whether game is won, lost, or still in progress
            if self.players[0].money.value <= 0:
                print(f"You have ${self.players[0].money.value}\nGame Over :(")
                self.players = [Player(money=Money()) for i in range(self.num_players)]
                live_table = False
            elif self.players[0].money.value >= Money.win_amount:
                print(f"You have ${self.players[0].money.value}\nYou win!")
                self.players = [Player(money=Money()) for i in range(self.num_players)]
                live_table = False

def ctrl_C_handler(signum, stack_frame):
    print("\n\nCtrl-C received. Ending program. Have a nice day! ")
    exit(0)